# coding: utf-8
from django.test import TestCase
from dext.settings import settings

from accounts.prototypes import AccountPrototype
from accounts.logic import register_user

from game.bundles import BundlePrototype

from game.logic import create_test_map
from game.workers.environment import workers_environment
from game.prototypes import TimePrototype


class LogicTest(TestCase):

    def setUp(self):
        settings.refresh()

        self.p1, self.p2, self.p3 = create_test_map()

        result, account_id, bundle_id = register_user('test_user')

        self.bundle = BundlePrototype.get_by_id(bundle_id)
        self.action_idl = self.bundle.tests_get_last_action()
        self.hero = self.bundle.tests_get_hero()

        self.account = AccountPrototype.get_by_id(self.hero.account_id)

        workers_environment.deinitialize()
        workers_environment.initialize()

        self.worker = workers_environment.logic
        self.worker.process_initialize(TimePrototype.get_current_turn_number(), 'logic')

    def tearDown(self):
        pass

    def test_process_initialize(self):
        self.assertTrue(self.worker.initialized)
        self.assertEqual(self.worker.worker_id, 'logic')
        self.assertEqual(self.worker.turn_number, 0)
        self.assertEqual(self.worker.bundles, {})
        self.assertEqual(self.worker.queue, [])
        self.assertEqual(self.worker.heroes2bundles, {})

    def test_process_mark_hero_as_not_fast(self):

        self.account.is_fast = True
        self.account.save()

        self.worker.process_register_bundle(self.bundle.id)
        self.assertTrue(self.worker.bundles[self.worker.heroes2bundles[self.hero.id]].heroes[self.hero.id].is_fast)
        self.worker.process_mark_hero_as_not_fast(self.hero.id)
        self.assertFalse(self.worker.bundles[self.worker.heroes2bundles[self.hero.id]].heroes[self.hero.id].is_fast)

    def test_process_register_bundle(self):

        self.assertTrue(self.hero.is_fast)

        self.account.is_fast = False
        self.account.save()

        self.worker.process_register_bundle(self.bundle.id)

        self.assertTrue(self.bundle.id in self.worker.bundles)
        self.assertEqual(self.worker.heroes2bundles[self.hero.id], self.bundle.id)

        self.assertFalse(self.worker.bundles[self.worker.heroes2bundles[self.hero.id]].heroes[self.hero.id].is_fast)
