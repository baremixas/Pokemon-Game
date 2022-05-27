import random

def effects(user, target, move):
    '''Function used to calculate all the additional bonuses for attack, such as:
    Critical strike bonus, Random bonus, Same-type attack bonus, Type effectiveness.

    The function is called during calculating damage output of a move.
    '''
    # Critical bonus
    if user.Critical_stage == 0:
        crit_value = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
    elif user.Critical_stage == 1:
        crit_value = random.choice([1,1,1,1,1,1,1,2])
    elif user.Critical_stage == 2:
        crit_value = random.choice([1,1,1,2])
    elif user.Critical_stage == 3:
        crit_value = random.choice([1,1,2])
    elif user.Critical_stage >= 4:
        crit_value = random.choice([1,2])

    crit_value = float(crit_value)

    # Random bonus
    rand_value = random.randint(85, 100) / 100

    # Same-type attack bonus
    stab_value = 1.0
    if move.type in user.type:
        stab_value = 1.5

    # Type effectiveness
    key_list = list(target.effectiveness.keys())
    val_list = list(target.effectiveness.values())
    for i in range(0, len(val_list)):
        if move.type in val_list[i]:
            position = i
    effect_value = float(key_list[position])

    # All bonuses
    all = crit_value * rand_value * stab_value * effect_value
    return all

def physical_damage(user, target, move):
    '''Function to calculate damage from physical type attacks.'''
    damage = ((((2 * user.level / 5 + 2) * move.power * user.A / target.D) / 50) + 2)\
             * move.weather * effects(user, target, move)
    return damage

def special_damage(user, target, move):
    '''Function to calculate damage from special type attacks.'''
    damage = ((((2 * user.level / 5 + 2) * move.power * user.SpA / target.SpD) / 50) + 2) \
             * move.weather * effects(user, target, move)
    return damage
