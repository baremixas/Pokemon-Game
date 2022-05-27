import random

from functions import *
from status import *


class PhysicalAttack:
    def __init__(self, type, power, accuracy, pp, priority, category='Physical'):
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self, user, target):
        self.damage = physical_damage(user, target, self)
        return self.damage


class SpecialAttack:
    def __init__(self, type, power, accuracy, pp, priority, category='Special'):
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority

        self.critical = 1
        self.random = 1
        self.weather = 1

    def effect_damage(self, user, target):
        self.damage = special_damage(user, target, self)
        return self.damage


class StatusAttack:
    def __init__(self, accuracy, pp, priority, type, category='Status'):
        self.type = type
        self.category = category
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority


class Tackle(PhysicalAttack):
    def __init__(self):
        super().__init__('Normal', 40, 100, 35, 0)


class Growl(StatusAttack):
    def __init__(self):
        super().__init__('Normal', 100, 40, 0)

    def effect_status(self, target):
        target.A_stage -= 1


class Scratch(PhysicalAttack):
    def __init__(self):
        super().__init__('Normal', 40, 100, 35, 0)


class Ember(SpecialAttack):
    def __init__(self):
        super().__init__('Fire', 40, 100, 25, 0)


class Smokescreen(StatusAttack):
    def __init__(self):
        super().__init__('Normal', 100, 20, 0)

    def effect_status(self, target):
        target.Accuracy_stage -= 1


class Dragon_Breath(SpecialAttack):
    def __init__(self):
        super().__init__('Dragon', 60, 100, 20, 0)

    def effect_status(self, user, target):
        if random.choice([False, False, False, False, False, False, False, True, True, True]):
            target.status.append(Paralysis)


class Fire_Fang(PhysicalAttack):
    def __init__(self):
        super().__init__('Fire', 65, 95, 15, 0)

    def effect_status(self):
        # If move before other move, it has 10% to flinch opponent
        self.flinch = random.choice([False,False,False,False,False,False,False,False,False,True])
        self.burn = random.choice([False,False,False,False,False,False,False,False,False,True])
        return self.flinch, self.burn


class Slash(PhysicalAttack):
    def __init__(self):
        super().__init__('Normal', 70, 100, 20, 0)


class Flamethrower(SpecialAttack):
    def __init__(self):
        super().__init__('Fire', 90, 100, 15, 0)


class Scary_Face(StatusAttack):
    def __init__(self):
        super().__init__('Normal', 100, 10, 0)

    def effect(self, target):
        target.Speed_stage -= 2


class Fire_Spin(SpecialAttack):
    def __init__(self):
        super().__init__('Fire', 35, 85, 15, 0)


class Inferno(SpecialAttack):
    def __init__(self):
        super().__init__('Fire', 100, 50, 5, 0)


class Flare_Blitz(PhysicalAttack):
    def __init__(self):
        super().__init__('Fire', 120, 100, 15, 0)
