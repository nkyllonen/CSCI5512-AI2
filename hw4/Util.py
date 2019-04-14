'''
CSCI 5512 - AI 2 - HW 4
Nikki Kyllonen
kyllo089

Util file with helper classes and functions
'''
import math

class Coord:
  def __init__(self, i, j):
    self.x = int(i)
    self.y = int(j)

  def __add__(self, other):
    return Coord(self.x + other.x, self.y + other.y)

  def __str__(self):
    return '({0} , {1})'.format(self.x, self.y)

class UCell:
  '''
  UCell: Utility object
    self.utility  (float) : utility value of this cell
    self.best_act (str)   : direction of best action to take
    self.is_end   (bool)  : T/F is this an end state cell
  '''
  def __init__(self, u = None, end = None):
    self.utility = None
    if u is not None:
      self.utility = u
    self.is_end = end or False
    self.best_act = "none"

  def __str__(self):
    if (self.utility != None and self.is_end == False):
      return ' {0:03.5f} - {1} '.format(self.utility, self.best_act)
    elif (self.utility == None):
      return ' XXXXXXXXX '
    else:
      return ' {0:03.5f} '.format(self.utility)

'''
has_converged: determine if there is a difference in the 
                chosen / determined best action to take
'''
def has_converged(u0, u1):
  for i in range(len(u0)):
    for j in range(len(u0[i])):
      if (u0[i][j].utility is not None):
        # check to see if the action has changed
        if u0[i][j].best_act != u1[i][j].best_act:
          return False
  return True

'''
turn: return Coord representing Coord c rotated deg degrees
'''
def turn(c, deg):
  rad = math.radians(deg)
  return Coord(c.x*math.cos(rad) - c.y*math.sin(rad), c.x*math.sin(rad) + c.y*math.cos(rad))

'''
correct_next: determine if next state is a valid state
'''
def correct_next(u, s, s_next):
  row = len(u)
  col = len(u[0])

  if (s_next.x < row and s_next.y < col and s_next.x >= 0 and s_next.y >= 0):
    if (u[s_next.x][s_next.y].utility != None):
      return s_next
    else:
      return s
  else:
    return s

def print2D(arr):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      print(arr[i][j], end='')
    print('\n')
