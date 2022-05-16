# **this is a sub file**
# 
# this file contains the classes of
# the moves for the main game

class moveAttackFormat():
        # returns a list of attack details:
        # (category, type, power, accuracy, times)
        def __init__(self, category, tipe, power, accuracy, times):
          self.category = category
          self.tipe = tipe
          self.power = power
          self.accuracy = accuracy
          self.times = times


class tackle(moveAttackFormat):
  def __init__(self):
    super().__init__("normal", 0, 40, 100, 1)


class quickAttack(moveAttackFormat):
  def __init__(self):
    super().__init__("normal", 0, 40, 100, 1)
    self.priority = 1


class doubleSlap(moveAttackFormat):
  def __init__(self):
    super().__init__("normal", 0, 15, 85, 5)


class strength(moveAttackFormat):
    def __init__(self):
        super().__init__("normal", 0, 80, 100, 1)


class xScissor(moveAttackFormat):
    def __init__(self):
        super().__init__("bug", 0, 80, 100, 1)


class airSlash(moveAttackFormat): # not gen1
  def __init__(self):
    super().__init__("flying", 0, 75, 95, 1)


class wingAttack(moveAttackFormat):
  def __init__(self):
    super().__init__("flying", 0, 35, 100, 1)


# stat moves should have type somehow 
class basicAtkIncrease():
  def __init__(self, fighter):
    fighter.atk += fighter.baseAtk * 0.5


class tailWind(): # should last 3 turns
    def __init__(self, fighter):
        fighter.spd += fighter.baseSpd

class tailWhip():
   def __init__(self, enemy):
        enemy.def -= enemy.baseDef * 0.5

