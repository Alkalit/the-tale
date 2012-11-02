# coding: utf-8

from django.db import models

from dext.utils import s11n

from game.game_info import RACE_CHOICES

from game.persons.models import Person, PERSON_STATE

from game.map.models import MapInfo

class MapInfoPrototype(object):

    def __init__(self, model):
        self.model = model

    @property
    def turn_number(self): return self.model.turn_number

    @property
    def terrain(self):
        if not hasattr(self, '_terrain'):
            self._terrain = s11n.from_json(self.model.terrain)
        return self._terrain

    @property
    def terrain_percents(self):
        if not hasattr(self, '_terrain_percents'):
            self._terrain_percents = s11n.from_json(self.model.terrain_percents)
        return self._terrain_percents

    @property
    def race_percents(self):
        if not hasattr(self, '_race_percents'):
            self._race_percents = dict( (int(k), v) for k, v in s11n.from_json(self.model.race_percents).items())
        return self._race_percents


    ######################
    # object operations
    ######################

    @classmethod
    def create(cls, turn_number, width, height, terrain):

        terrain_squares = {}

        for row in terrain:
            for cell in row:
                terrain_squares[cell] = terrain_squares.get(cell, 0) + 1

        total_cells = sum(terrain_squares.values())

        terrain_percents = dict( (cell, float(square) / total_cells) for cell, square in terrain_squares.items())

        race_powers = {}
        for race_id, race_name in RACE_CHOICES:
            power = Person.objects.filter(race=race_id, state=PERSON_STATE.IN_GAME).aggregate(models.Sum('power'))['power__sum']
            race_powers[race_id] = power if power is not None else 0

        total_power = sum(race_powers.values()) + 1 # +1 - to prevent division by 0

        race_percents = dict( (race_id, float(power) / total_power) for race_id, power in race_powers.items())

        model = MapInfo.objects.create(turn_number=turn_number,
                                       width=width,
                                       height=height,
                                       terrain=s11n.to_json(terrain),
                                       terrain_percents=s11n.to_json(terrain_percents),
                                       race_percents=s11n.to_json(race_percents))
        return cls(model)
