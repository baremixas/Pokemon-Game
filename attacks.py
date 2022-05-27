import random

from functions import *
from status import *


class Tackle:
    def __init__(self):
        self.type = 'Normal'
        self.category = 'Physical'
        self.power = 40
        self.accuracy = 100
        self.PP = 35

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self, user, target):
        self.damage = physical_damage(user, target, self)
        return self.damage


class Growl:
    def __init__(self):
        self.type = 'Normal'
        self.category = 'Status'
        self.power = 0
        self.accuracy = 100
        self.PP = 40
        self.priority = 0

    def effect_status(self, target):
        target.A_stage -= 1


class Scratch:
    def __init__(self):
        self.type = 'Normal'
        self.category = 'Physical'
        self.power = 40
        self.accuracy = 100
        self.PP = 35

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self, user, target):
        self.damage = physical_damage(user, target, self)
        return self.damage


class Ember:
    def __init__(self):
        self.type = 'Fire'
        self.category = 'Special'
        self.power = 40
        self.accuracy = 100
        self.PP = 25

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self, user, target):
        self.damage = special_damage(user, target, self)
        return self.damage


class Smokescreen:
    def __init__(self):
        self.type = 'Normal'
        self.category = 'Status'
        self.power = 0
        self.accuracy = 100
        self.PP = 20
        self.priority = 0
    def effect_status(self, target):
        target.Accuracy_stage -= 1


class Dragon_Breath:
    def __init__(self):
        self.type = 'Dragon'
        self.category = 'Special'
        self.power = 60
        self.accuracy = 100
        self.PP = 20

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self,user,target):
        self.damage = special_damage(user,target,self)
        return self.damage

    def effect_status(self, user, target):
        if random.choice([False, False, False, False, False, False, False, True, True, True]):
            target.status.append(Paralysis)


class Fire_Fang:
    def __init__(self):
        self.type = 'Fire'
        self.category = 'Physical'
        self.power = 65
        self.accuracy = 95
        self.PP = 15

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self, user, target):
        self.damage = physical_damage(user, target, self)
        return self.damage

    def effect_status(self):
        # If move before other move, it has 10% to flinch opponent
        self.flinch = random.choice([False,False,False,False,False,False,False,False,False,True])
        self.burn = random.choice([False,False,False,False,False,False,False,False,False,True])
        return self.flinch, self.burn


class Slash:
    def __init__(self):
        self.type = 'Normal'
        self.category = 'Physical'
        self.power = 70
        self.accuracy = 100
        self.PP = 20

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect(self, user, target):
        self.damage = physical_damage(user, target, self)
        return self.damage


class Flamethrower:
    def __init__(self):
        self.type = 'Fire'
        self.category = 'Special'
        self.power = 90
        self.accuracy = 100
        self.PP = 15

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect(self, user, target):
        self.damage = special_damage(user, target, self)
        return self.damage


class Scary_Face:
    def __init__(self):
        self.type = 'Normal'
        self.category = 'Status'
        self.power = 0
        self.accuracy = 100
        self.PP = 10
        self.priority = 0

    def effect(self, target):
        target.Speed_stage -= 2


class Fire_Spin:
    def __init__(self):
        self.type = 'Fire'
        self.category = 'Special'
        self.power = 35
        self.accuracy = 85
        self.PP = 15

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect(self, user, target):
        self.damage = special_damage(user, target, self)
        return self.damage


class Inferno:
    def __init__(self):
        self.type = 'Fire'
        self.category = 'Special'
        self.power = 100
        self.accuracy = 50
        self.PP = 5

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect(self,user,target):
        self.damage = special_damage(user, target, self)
        return self.damage


class Flare_Blitz:
    def __init__(self):
        self.type = 'Fire'
        self.category = 'Physical'
        self.power = 120
        self.accuracy = 100
        self.PP = 15

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect(self, user, target):
        self.damage = physical_damage(user, target, self)
        return self.damage
