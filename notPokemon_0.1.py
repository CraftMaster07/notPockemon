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
        # (category, type, power, accuracy, times)
        return (0, 0, 40, 100, 1)
    
    def move_multyHitAttack(self):
        # returns a list of attack details:
        # (category, type, power, accuracy, times)
        return (0, 0, 15, 85, 2+random.randint(0,4))
    
    def move_basicSpaIncrease(self):
        self.spa += self.baseSpa * 0.5

class ally1:
    # constractor for ally stats
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
        # (category, type, power, accuracy, times)
        return (0, 0, 40, 100, 1)
    
    def move_multyHitAttack(self):
        # returns a list of attack details:
        # (category, type, power, accuracy, times)
        return (0, 0, 15, 85, 2+random.randint(0,4))
    
    def move_basicAtkIncrease(self):
        self.Atk += self.baseAtk * 0.5


def damageCalculation(pwr, atk):
    # param pwr(int): base damage of the move
    # param atk(int): atk stat of the "fighter"
    # return: calculated damage
    # rtype: int
    
    # damage result
    damage = (pwr * atk)/50+2
    
    return damage

# basic combat test stats
playerA = ally1(50, 200, 0, 0)
playerB = ally1(50, 200, 0, 0)
turn = 0

# basic combat game loop
# untill someone dies
while playerA.hp > 0 or playerB.hp > 0:
    # move-pick phase
    playerAMove = input("Player A: enter num of move: (0-2)")
    playerBMove = input("Player B: enter num of move: (0-2)")
    
    # start attack!
    if turn%2 == 0:
        ####
        move = (playerA.move_basicAttack(), playerA.move_multyHitAttack(), 2)[playerAMove]
        if move != 2:
            for i in range(move[4]):
                if random.randint(0, 100) < move[3]:
                    playerB.hp -= damageCalculation(move[2], playerA.atk)
                    print("hit!")
        elif move == 2:
            playerA.move_basicAtkIncrease()
        ####
        move = (playerB.move_basicAttack(), playerB.move_multyHitAttack(), 2)[playerBMove]
        if move != 2:
            for i in range(move[4]):
                if random.randint(0, 100) < move[3]:
                    playerA.hp -= damageCalculation(move[2], playerB.atk)
                    print("hit!")
        elif move == 2:
            playerB.move_basicAtkIncrease()
        ####
    else:        
        move = (playerB.move_basicAttack(), playerB.move_multyHitAttack(), 2)[playerBMove]
        if move != 2:
            for i in range(move[4]):
                if random.randint(0, 100) < move[3]:
                    playerA.hp -= damageCalculation(move[2], playerB.atk)
                    print("hit!")
        elif move == 2:
            playerB.move_basicAtkIncrease()
        ####
        move = (playerA.move_basicAttack(), playerA.move_multyHitAttack(), 2)[playerAMove]
        if move != 2:
            for i in range(move[4]):
                if random.randint(0, 100) < move[3]:
                    playerB.hp -= damageCalculation(move[2], playerA.atk)
                    print("hit!")
        elif move == 2:
            playerA.move_basicAtkIncrease()
        
    ## combat end ##
    print("player a: hp = {}".format(playerA.hp))
    print("player b: hp = {}".format(playerB.hp))
