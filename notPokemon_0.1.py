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

class enemy1:
    # constractor for enemy stats
    def __init__(self, atk, hp, spa, spe):
        self.atk = atk
        self.hp = hp
        self.spe = spe
        self.spa = spa
        
        self.baseAtk = atk
        self.baseHp = hp
        self.baseSpe = spe
        self.baseSpa = spa
    
    def move_basicAttack(self):
        # returns a list of attack details:
        # (category, type, power, accuracy)
        return (0, 0, 50, 100)
    
    def move_basicSpaIncrease(self):
        self.spa += self.baseSpa * 0.5

class allay1:
    # constractor for allay stats
    def __init__(self, atk, hp, spe):
        self.atk = atk
        self.hp = hp
        self.spe = spe


def damageCalculation(pwr, atk):
    # param pwr(int): base damage of the move
    # param atk(int): atk stat of the "fighter"
    # return: calculated damage
    # rtype: int
    
    # damage result
    damage = (pwr * atk)/50+2
    
    return damage
