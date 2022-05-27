import random

# non-volatile
class Paralysis():
    def __init__(self):
        self.kind = 'non-volatile'
        # 50% slow
        self.slow = 0.5

    def hit_yourself(self):
        # 25% of hitting yourself
        return random.choice([False,False,False,True])


# non-volatile
class Burn():
    def __init__(self):
        self.kind = 'non-volatile'
        self.damage_per_turn = 0.125


# # non-volatile
# class Poison():
#     def __init__(self):
#
#
# # non-volatile
# class Sleep():
#     def __init__(self):
