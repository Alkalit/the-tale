# coding: utf-8
import random

from ..quest_line import Quest, Line, ACTOR_TYPE
from .. import commands as cmd

class EVENTS:
    QUEST_DESCRIPTION = 'quest_description'
    MOVE_TO_QUEST = 'move_to_quest'
    MOVE_TO_CUSTOMER = 'move_to_customer'
    START_QUEST = 'start_quest'
    GIVE_POWER_TO_CUSTOMER = 'give_power_to_customer'
    GET_POWER_FROM_PERFORMER = 'get_power_from_performer'
    ATTACK_PERFORMER = 'brutforce_performer'
    WORK_CHOICE = 'diplomacy_choice'
    GET_REWARD = 'get_reward'


class NotMyWork(Quest):

    ACTORS = [(u'попросил', 'person_start', ACTOR_TYPE.PERSON),
              (u'должник', 'person_end', ACTOR_TYPE.PERSON)]

    def initialize(self, identifier, env, **kwargs):
        super(NotMyWork, self).initialize(identifier, env, **kwargs)

        self.env_local.register('choose_point_1', env.new_choice_point())

        self.env_local.register('others_work_quest', env.new_quest(place_start=self.env_local.place_end,
                                                                   person_start=self.env_local.person_end) )

    def create_line(self, env):
        env.quests[self.env_local.others_work_quest].create_line(env)

        work_line = Line(sequence=[ cmd.Quest(quest=self.env_local.others_work_quest, event=EVENTS.START_QUEST),
                                    cmd.Move(place=self.env_local.place_start, event=EVENTS.MOVE_TO_CUSTOMER),
                                    cmd.GivePower(person=self.env_local.person_start, power=1, event=EVENTS.GIVE_POWER_TO_CUSTOMER),
                                    cmd.GetReward(person=self.env_local.person_start, event=EVENTS.GET_REWARD),
                                    ] )

        attack_line =  Line(sequence=[ cmd.Battle(number=random.randint(1, 5), event=EVENTS.ATTACK_PERFORMER),
                                       cmd.GivePower(person=self.env_local.person_end, power=-1, event=EVENTS.GET_POWER_FROM_PERFORMER),
                                       cmd.Move(place=self.env_local.place_start, event=EVENTS.MOVE_TO_CUSTOMER),
                                       cmd.GivePower(person=self.env_local.person_start, power=1, event=EVENTS.GIVE_POWER_TO_CUSTOMER),
                                       cmd.GetReward(person=self.env_local.person_start, event=EVENTS.GET_REWARD),
                                       ] )

        main_line = Line(sequence=[cmd.Move(place=self.env_local.place_end, event=EVENTS.MOVE_TO_QUEST),
                                   cmd.Choose(id=self.env_local.choose_point_1,
                                              default='work',
                                              choices={'diplomacy': env.new_line(work_line),
                                                       'bruteforce': env.new_line(attack_line)},
                                              event=EVENTS.WORK_CHOICE,
                                              choice='work') ])

        self.line = env.new_line(main_line)
