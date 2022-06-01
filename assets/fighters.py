# - this is a sub file -
#
# this file contains the "fighters", which can be both enemys and allys
import moves

# currently: ratata, pidgy, ekans, nidoran♂, nidoran♀, vulpix, oddish, paras, diglet, 
#            growlithe, poliwag, abra, tentacool, geodude, slowpoke, magnemite,
#            grimer, shellder, gastly, onix, cubone, koffing, rhyhorn
#            tangela, staryu, scyther, pinsir, magikarp, lapras, omanyte,
#            kabuto, aerodactyl, snorlax
#            mew/two

class fighterFormat():
    # constractor for fighter stats
    def __init__(self, atk, hp, spa, spe):
        self.atk = atk
        self.hp = hp
        self.spe = spe
        self.spa = spa

        self.baseAtk = atk
        self.baseHp = hp
        self.baseSpe = spe
        self.baseSpa = spa
        
        # moves are not included

class pidgy(fighterFormat):
    # this fighter is based on pidgy
    def __init__(self):
        super().__init__(40, 45, 35, 56)
        self.move1 = moves.basicAttack()
        self.move2 = moves.agility()
        self.move3 = moves.wingAttack()


class ratata(fighterFormat):
    # this fighter is based on ratata
    def __init__(self):
        super().__init__(56, 30, 25, 72)
        self.move1 = moves.basicAttack()
        self.move2 = moves.quickAttack()
