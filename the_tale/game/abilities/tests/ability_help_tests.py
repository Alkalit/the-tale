# coding: utf-8
import mock

from common.utils import testcase

from accounts.prototypes import AccountPrototype
from accounts.logic import register_user

from game.logic_storage import LogicStorage
from game.logic import create_test_map

from game.balance import constants as c
from game.actions import prototypes as actions_prototypes
from game.heroes.logic import create_mob_for_hero
from game.abilities.deck.help import Help
from game.prototypes import TimePrototype

from game.pvp.prototypes import Battle1x1Prototype
from game.pvp.models import BATTLE_1X1_STATE

class HelpAbilityTest(testcase.TestCase):

    def setUp(self):
        super(HelpAbilityTest, self).setUp()
        self.p1, self.p2, self.p3 = create_test_map()


        result, account_id, bundle_id = register_user('test_user_1', 'test_user_1@test.com', '111111')

        self.account = AccountPrototype.get_by_id(account_id)
        self.storage = LogicStorage()
        self.storage.load_account_data(self.account)
        self.hero = self.storage.accounts_to_heroes[self.account.id]
        self.action_idl = self.hero.actions.current_action

        self.ability = Help()

    @property
    def use_attributes(self):
        return {'data': {'hero_id': self.hero.id},
                'step': None,
                'main_task_id': 0,
                'storage': self.storage,
                'pvp_balancer': None}

    def test_none(self):
        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: None):
            self.assertEqual(self.ability.use(**self.use_attributes), (False, None, ()))

    def test_help_when_battle_waiting(self):
        battle = Battle1x1Prototype.create(self.account)
        self.assertTrue(battle.state._is_WAITING)
        self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))

    def test_help_when_battle_not_waiting(self):
        battle = Battle1x1Prototype.create(self.account)
        battle.state = BATTLE_1X1_STATE.PREPAIRING
        battle.save()

        self.assertFalse(battle.state._is_WAITING)
        self.assertEqual(self.ability.use(**self.use_attributes), (False, None, ()))

    def test_heal(self):
        self.hero.health = 1
        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: c.HELP_CHOICES.HEAL):
            self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))
            self.assertTrue(self.hero.health > 1)

    def test_start_quest(self):
        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: c.HELP_CHOICES.START_QUEST):
            self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))
            self.assertTrue(self.action_idl.percents >= 1)

    def test_money(self):
        old_hero_money = self.hero.money
        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: c.HELP_CHOICES.MONEY):
            self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))
            self.assertTrue(self.hero.money > old_hero_money)

    @mock.patch('game.balance.constants.BATTLES_PER_TURN', 0)
    def test_teleport(self):
        move_place = self.p3
        if move_place.id == self.hero.position.place.id:
            move_place = self.p1

        current_time = TimePrototype.get_current_time()

        action_move = actions_prototypes.ActionMoveToPrototype.create(hero=self.hero, destination=move_place)

        current_time.increment_turn()
        self.storage.process_turn()

        old_road_percents = self.hero.position.percents
        old_percents = action_move.percents

        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: c.HELP_CHOICES.TELEPORT):
            self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))

        self.assertTrue(old_road_percents < self.hero.position.percents)
        self.assertTrue(old_percents < action_move.percents)
        self.assertEqual(self.hero.actions.current_action.percents, action_move.percents)


    def test_lighting(self):
        current_time = TimePrototype.get_current_time()
        action_battle = actions_prototypes.ActionBattlePvE1x1Prototype.create(hero=self.hero, mob=create_mob_for_hero(self.hero))

        current_time.increment_turn()
        self.storage.process_turn()

        old_mob_health = action_battle.mob.health
        old_percents = action_battle.percents

        self.assertTrue(c.HELP_CHOICES.LIGHTING in action_battle.help_choices)

        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: c.HELP_CHOICES.LIGHTING):
            self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))

        self.assertTrue(old_mob_health > action_battle.mob.health)
        self.assertEqual(self.hero.actions.current_action.percents, action_battle.percents)
        self.assertTrue(old_percents < action_battle.percents)

    def test_lighting_when_mob_killed(self):
        current_time = TimePrototype.get_current_time()
        action_battle = actions_prototypes.ActionBattlePvE1x1Prototype.create(hero=self.hero, mob=create_mob_for_hero(self.hero))

        current_time.increment_turn()
        self.storage.process_turn()

        action_battle.mob.health = 0

        self.assertFalse(c.HELP_CHOICES.LIGHTING in action_battle.help_choices)

    def test_resurrect(self):
        current_time = TimePrototype.get_current_time()

        self.hero.kill()
        action_resurrect = actions_prototypes.ActionResurrectPrototype.create(hero=self.hero)

        old_percents = action_resurrect.percents

        with mock.patch('game.heroes.actions.ActionBase.get_help_choice', lambda x: c.HELP_CHOICES.RESURRECT):
            current_time.increment_turn()
            self.assertEqual(self.ability.use(**self.use_attributes), (True, None, ()))
            self.storage.process_turn()

        self.assertEqual(self.hero.health, self.hero.max_health)
        self.assertEqual(self.hero.is_alive, True)
        self.assertTrue(old_percents < action_resurrect.percents)
        self.assertEqual(self.hero.actions.current_action.percents, action_resurrect.percents)
