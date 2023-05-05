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
    damage = ((pwr * atk)/50+2)*float(f'{random.randint(85,100)/100:.2f}')

    return damage


def combat(fighter1, fighter2):
    while fighter1.hp > 0 && fighter2.hp > 0:
        # move choosing
        print("\n**player 1's turn**\n")
        pickedMove1 = pickMove(fighter1)
        pickedMove2 = pickMove(fighter2)
        
        # its morbing time!
        if whoAttacksFirst(fighter1, fighter2) == fighter1:
            # continue here
        print("{} used {}!".format())

def pickMove(fighter):
    # gets number as input and returns move
    printMoveChoices(fighter)
    pickedMove = moveByNum(fighter, int(input("pick a move (1-4): ")))
    return pickedMove


def printMoveChoices(fighter):
    # prints the available moves
    print("1 - {}, 2 - {}\n3 - {}, 4 - {}".format(*fighter.getMoves()))

def moveByNum(fighter, num):
    # turns number into corresponding move
    if pickedMoveNum == 1:
        pickedMove = fighter.move1
    elif pickedMoveNum == 2:
        pickedMove = fighter.move2
    elif pickedMoveNum == 3:
        pickedMove = fighter.move3
    elif pickedMoveNum == 4:
        pickedMove = fighter.move4
    else:
        pickedMove = "error"
    return pickedMove


def whoAttacksFirst(fighter1, fighter2):
    # should add priority check
    if fighter1.spe > fighter2.spe:
        return fighter1
    else:
        return fighter2
    
