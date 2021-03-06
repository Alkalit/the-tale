# coding: utf-8

from django.db import IntegrityError, transaction

from the_tale.common.utils.prototypes import BasePrototype

from the_tale.game.pvp.models import Battle1x1, Battle1x1Result
from the_tale.game.pvp.relations import BATTLE_1X1_STATE


class Battle1x1Prototype(BasePrototype):
    _model_class = Battle1x1
    _readonly = ('id', 'account_id', 'enemy_id', 'created_at')
    _bidirectional = ('calculate_rating', 'state')
    _get_by = ('id', 'enemy_id', 'account_id')

    @classmethod
    def reset_waiting_battles(cls):
        Battle1x1.objects.filter(state=BATTLE_1X1_STATE.WAITING).delete()

    def set_enemy(self, enemy):
        self._model.enemy = enemy._model
        self.state = BATTLE_1X1_STATE.PREPAIRING

    def save(self):
        self._model.save()

    def remove(self):
        self._model.delete()

    @classmethod
    def create(cls, account):
        try:
            with transaction.atomic():
                model = cls._model_class.objects.create(account=account._model,
                                                        state=BATTLE_1X1_STATE.WAITING)
        except IntegrityError:
            return cls.get_by_account_id(account.id)

        return cls(model=model)


class Battle1x1ResultPrototype(BasePrototype):
    _model_class = Battle1x1Result
    _readonly = ('id', 'created_at', 'participant_1_id', 'participant_2_id', 'result')
    _bidirectional = ()
    _get_by = ()

    @classmethod
    def create(cls, participant_1, participant_2, result):
        return cls(model=cls._model_class.objects.create(participant_1=participant_1._model,
                                                         participant_2=participant_2._model,
                                                         result=result))
