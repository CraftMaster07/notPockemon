import random
# welcome madafaqas to my game!
#
# this game is TOTALLY NOT based on the popular 
# game AMON- I mean Pokemon 1997
#
# in this game each "fighter" has 3 basic stats:
# atk: stands for Attack
# hp: stands for Health Points
# spa: stands for Special attack
# spe: stands for Speed

def damageCalculation(pwr, atk):
    # param pwr(int): base damage of the move
    # param atk(int): atk stat of the "fighter"
    # return: calculated damage
    # rtype: int
    
    # damage result
    damage = (pwr * atk)/50+2
    
    return damage


def combat(fighter1, fighter2):
    while fighter1.hp > 0 && fighter2.hp > 0:
        pass
