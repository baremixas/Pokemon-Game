import random
from types_dic import All_types,Grass,Poison,Fire


class Pokemon:
    '''Parent class used to create all pokemon.

    It contains methods used to calculate user stats, update stats after each round during battle,
    determine user's type effectivity and attacks.
    '''
    def __init__(self, lvl):
        self.initialize_pokemon(lvl)

    def initialize_pokemon(self, lvl):
        self.level = lvl

        # Possible -10% / +10% dependant on nature
        self.A_Nature = 1
        self.D_Nature = 1
        self.SpA_Nature = 1
        self.SpD_Nature = 1
        self.Spd_Nature = 1

        # IV 0 - 31
        self.HP_IV = 0
        self.A_IV = 0
        self.D_IV = 0
        self.SpA_IV = 0
        self.SpD_IV = 0
        self.Spd_IV = 0

        # EV 510 total, 252 max
        self.HP_EV = 0
        self.A_EV = 0
        self.D_EV = 0
        self.SpA_EV = 0
        self.SpD_EV = 0
        self.Spd_EV = 0

        # Type and type-effectiveness
        self.type = []
        self.x1 = []
        self.x2 = []
        self.x4 = []
        self.x1_2 = []
        self.x1_4 = []
        self.immune = []
        self.effectiveness = {1: self.x1, 2: self.x2, 4: self.x4, 0.5: self.x1_2, 0.25: self.x1_4,
                              0: self.immune}

        # Statistics stages for buffs/debuffs
        self.A_stage = 0
        self.D_stage = 0
        self.SpA_stage = 0
        self.SpD_stage = 0
        self.Spd_stage = 0

        self.Accuracy_stage = 0
        self.Critical_stage = 0

        self.status_non_volatile = []
        self.status_volatile = []

    def calc_stats(self):
        '''Method used to calculate user statistics.'''
        self.HP = int((2 * self.HP_Base + self.HP_IV + int(self.HP_EV / 4)) * self.level / 100) + self.level + 10
        self.A = int((int((2 * self.A_Base + self.A_IV + int(self.A_EV / 4)) * self.level / 100) + 5) * self.A_Nature)
        self.D = int((int((2 * self.D_Base + self.D_IV + int(self.D_EV / 4)) * self.level / 100) + 5) * self.D_Nature)
        self.SpA = int((int((2 * self.SpA_Base + self.SpA_IV + int(self.SpA_EV / 4)) * self.level / 100) + 5) * self.SpA_Nature)
        self.SpD = int((int((2 * self.SpD_Base + self.SpD_IV + int(self.SpD_EV / 4)) * self.level / 100) + 5) * self.SpD_Nature)
        self.Spd = int((int((2 * self.Spd_Base + self.Spd_IV + int(self.Spd_EV / 4)) * self.level / 100) + 5) * self.Spd_Nature)

        self.stats = {'HP': self.HP, 'A': self.A, 'D': self.D, 'SpA': self.SpA, 'SpD': self.SpD, 'Spd': self.Spd}

    def calc_type_effectivity(self, types):
        '''Method used to determine user's type effectivity according to input types.'''
        for type in types:
            self.type.append(type['name'])

            for element in type[2]:
                if element in self.x4:
                    pass
                elif element in self.x2:
                    self.x2.remove(element)
                    self.x4.append(element)
                elif element in self.x1:
                    self.x1.remove(element)
                    self.x2.append(element)
                elif element in self.x1_2:
                    self.x1_2.remove(element)
                    self.x1.append(element)
                elif element in self.x1_4:
                    self.x1_4.remove(element)
                    self.x1_2.append(element)
                elif element in self.immune:
                    pass
                else:
                    self.x2.append(element)

            for element in type[4]:
                if element in self.x4:
                    pass
                elif element in self.x2:
                    self.x2.remove(element)
                    self.x4.append(element)
                elif element in self.x1:
                    self.x1.remove(element)
                    self.x4.append(element)
                elif element in self.x1_2:
                    self.x1_2.remove(element)
                    self.x2.append(element)
                elif element in self.x1_4:
                    self.x1_4.remove(element)
                    self.x1.append(element)
                elif element in self.immune:
                    pass
                else:
                    self.x4.append(element)

            for element in type[0.5]:
                if element in self.x4:
                    self.x4.remove(element)
                    self.x2.append(element)
                elif element in self.x2:
                    self.x2.remove(element)
                    self.x1.append(element)
                elif element in self.x1:
                    self.x1.remove(element)
                    self.x1_2.append(element)
                elif element in self.x1_2:
                    self.x1_2.remove(element)
                    self.x1_4.append(element)
                elif element in self.x1_4:
                    pass
                elif element in self.immune:
                    pass
                else:
                    self.x1_2.append(element)

            for element in type[0.25]:
                if element in self.x4:
                    self.x4.remove(element)
                    self.x1.append(element)
                elif element in self.x2:
                    self.x2.remove(element)
                    self.x1_2.append(element)
                elif element in self.x1:
                    self.x1.remove(element)
                    self.x1_4.append(element)
                elif element in self.x1_2:
                    self.x1_2.remove(element)
                    self.x1_4.append(element)
                elif element in self.x1_4:
                    pass
                elif element in self.immune:
                    pass
                else:
                    self.x1_4.append(element)

            for element in type[0]:
                if element in self.x4:
                    self.x4.remove(element)
                    self.immune.append(element)
                elif element in self.x2:
                    self.x2.remove(element)
                    self.immune.append(element)
                elif element in self.x1:
                    self.x1.remove(element)
                    self.immune.append(element)
                elif element in self.x1_2:
                    self.x1_2.remove(element)
                    self.immune.append(element)
                elif element in self.x1_4:
                    self.x1_4.remove(element)
                    self.immune.append(element)
                elif element in self.immune:
                    pass
                else:
                    self.immune.append(element)

            self.effectiveness[2] = self.x2
            self.effectiveness[4] = self.x4
            self.effectiveness[0.5] = self.x1_2
            self.effectiveness[0.25] = self.x1_4
            self.effectiveness[0] = self.immune

            for element in All_types:
                type_list = (list(self.effectiveness.values())[0] + list(self.effectiveness.values())[1] +
                             list(self.effectiveness.values())[2] + list(self.effectiveness.values())[3] +
                             list(self.effectiveness.values())[4] + list(self.effectiveness.values())[5])

                if element in type_list:
                    pass
                else:
                    self.x1.append(element)

            self.effectiveness[1] = self.x1

    def get_possible_attacks(self):
        '''Method used to determine which skills user is capable of having according to it's level.'''
        self.possible_attacks = []

        for lvl in range(1,self.level+1):
            if self.skills.get(lvl) != None:
                if type(self.skills.get(lvl)) == list:
                    for attack in self.skills.get(lvl):
                        if attack != None:
                            self.possible_attacks.append(attack)
                else:
                    self.possible_attacks.append(self.skills.get(lvl))

    def get_random_attacks(self):
        '''Method used to randomly select maximum of 4 attacks from user's all possible attacks according to
        it's level.
        '''
        if len(self.possible_attacks) < 4:
            self.attacks = self.possible_attacks
        else:
            self.attacks = random.sample(self.possible_attacks,k=4)

    def update_stats(self):
        '''Method used to update user's statistics after each round during battle.'''
        self.stats = {'HP': self.HP, 'A': self.A, 'D': self.D, 'SpA': self.SpA, 'SpD': self.SpD, 'Spd': self.Spd}


class Bulbasaur(Pokemon):
    def __init__(self,lvl):
        super().__init__(lvl)
        self.initialize()

    def initialize(self):
        # Base stats
        self.HP_Base = 45
        self.A_Base = 49
        self.D_Base = 49
        self.SpA_Base = 65
        self.SpD_Base = 65
        self.Spd_Base = 45

        self.calc_stats()
        self.calc_type_effectivity([Grass,Poison])

        # Skills according to level
        self.skills = {1: ['Tackle', 'Growl'], 3: 'Vine Whip', 6: 'Growth', 9: 'Leech Seed', 12: 'Razor Leaf',
                       15: ['Poison Powder', 'Sleep Powder'], 18: 'Seed Bomb', 21: 'Take Down', 24: 'Sweet Scent',
                       27: 'Synthesis', 30: 'Worry Seed', 33: 'Double-Edge', 36: 'Solar Beam'}

        self.get_possible_attacks()
        self.get_random_attacks()


class Charmander(Pokemon):
    def __init__(self,lvl):
        super().__init__(lvl)

        self.initialize()

    def initialize(self):
        # Base stats
        self.HP_Base = 39
        self.A_Base = 52
        self.D_Base = 43
        self.SpA_Base = 60
        self.SpD_Base = 50
        self.Spd_Base = 65

        self.calc_stats()
        self.calc_type_effectivity([Fire])

        # Dkills according to level
        self.skills = {1: ['Scratch', 'Growl'], 4: 'Ember', 8: 'Smokescreen', 12: 'Dragon Breath', 17: 'Fire Fang',
                       20: 'Slash', 24: 'Flamethrower', 28: 'Scary Face', 32: 'Fire Spin', 36: 'Inferno', 40: 'Flare Blitz'}

        self.get_possible_attacks()
        self.get_random_attacks()