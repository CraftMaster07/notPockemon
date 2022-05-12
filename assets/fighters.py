# - this is a sub file -
#
# this file contains the "fighters", which can be both enemys and allys
import moves


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


class fighter1(fighterFormat):
    # this fighter is based on piggy
    def __init__(self):
        super().__init__(40, 45, 35, 56)
        self.move1 = moves.basicAttack()


class fighter2(fighterFormat):
    # this fighter is based on ratata
    def __init__(self):
        super().__init__(56, 30, 25, 72)
        self.move1 = moves.basicAttack()
        self.move2 = moves.quickAttack()
