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
          
class basicAttack(moveAttackFormat):
  def __init__(self):
    super().__init__(0, 0, 40, 100, 1)

class quickAttack(moveAttackFormat):
  def __init__(self):
    super().__init__(0, 0, 40, 100, 1)
    self.priority = 1


class multyHitAttack(moveAttackFormat):
  def __init__(self):
    super().__init__(0, 0, 15, 85, 5)
    
class basicAtkIncrease():
  def __init__(self, fighter):
    fighter.Atk += fighter.baseAtk * 0.5
