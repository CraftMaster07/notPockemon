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
        print("\n**player 1's turn**\n")
        pickedMove1 = pickMove(fighter1)
        pickedMove2 = pickMove(fighter2)

def pickMove(fighter):
    # gets number as input and returns move
    printMoveChoices(fighter)
    pickedMove = moveByNum(int(input("pick a move (1-4): ")))
    return pickedMove


def printMoveChoices(fighter):
    print("1 - {}, 2 - {}\n3 - {}, 4 - {}".format(*fighter.getMoves()))

def moveByNum(fighter):
    if pickedMoveNum == 1:
        pickedMove = fighter.move1
    if pickedMoveNum == 2:
        pickedMove = fighter.move2
    if pickedMoveNum == 3:
        pickedMove = fighter.move3
    if pickedMoveNum == 4:
        pickedMove = fighter.move4
    return pickedMove
