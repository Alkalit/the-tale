# coding: utf-8

from textgen.words import Fake

from game.game_info import GENDER_ID_2_STR
from game.map.places.storage import places_storage
from game.heroes.models import Hero

from game.persons.models import Person, PERSON_STATE



class PersonPrototype(object):

    def __init__(self, model):
        self.model = model

    @classmethod
    def get_by_id(cls, id_):
        return cls(Person.objects.get(id=id_))

    @property
    def id(self): return self.model.id

    @property
    def place_id(self): return self.model.place_id

    @property
    def place(self): return places_storage[self.model.place_id]

    @property
    def name(self): return self.model.name

    @property
    def normalized_name(self): return (Fake(self.model.name), (GENDER_ID_2_STR[self.gender], u'загл'))

    @property
    def gender(self): return self.model.gender

    @property
    def race(self): return self.model.race

    @property
    def race_verbose(self):
        from ..game_info import RACE_DICT
        return RACE_DICT[self.race]

    @property
    def type(self): return self.model.type

    @property
    def state(self): return self.model.state

    def move_out_game(self): self.model.state = PERSON_STATE.OUT_GAME
    def move_in_game(self):  self.model.state = PERSON_STATE.IN_GAME

    @property
    def out_game(self): return self.model.state == PERSON_STATE.OUT_GAME

    @property
    def in_game(self):  return self.model.state == PERSON_STATE.IN_GAME

    @property
    def type_verbose(self):
        from .models import PERSON_TYPE_DICT
        return PERSON_TYPE_DICT[self.type]

    def get_power(self): return self.model.power
    def set_power(self, value): self.model.power = value
    power = property(get_power, set_power)

    @property
    def friends_number(self): return self.model.friends_number
    def update_friends_number(self): self.model.friends_number = Hero.objects.filter(pref_friend_id=self.id).count()

    @property
    def enemies_number(self): return self.model.enemies_number
    def update_enemies_number(self): self.model.enemies_number = Hero.objects.filter(pref_enemy_id=self.id).count()

    def save(self):
        self.model.save()

    def remove(self):
        self.model.remove()

    @classmethod
    def create(cls, place, race, tp, name, gender, power=0, state=None):

        instance = Person.objects.create(place=place.model,
                                         state=state if state is not None else PERSON_STATE.IN_GAME,
                                         race=race,
                                         type=tp,
                                         gender=gender,
                                         name=name,
                                         power=power)

        return cls(model=instance)
