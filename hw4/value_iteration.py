'''
CSCI 5512 - AI 2 - HW 4
Nikki Kyllonen
kyllo089

Problem 3: Value Iteration
  (20 points)
  Assume that when moving there is a 70% chance to
  end up where you want to go and a 15% chance to
  end up 90 degrees left/right

  Given 4 rows x 3 columns Rewards + gamma = 0.8 
'''

import random, sys, copy

class Coord:
  def __init__(self, i, j):
    self.x = i
    self.y = j

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
    self.utility = u or None
    self.is_end = end or False
    self.best_act = ""

  def __str__(self):
    if (self.is_end == False):
      return ' {0} - {1} '.format(self.utility, self.best_act)
    else:
      return ' {0} '.format(self.utility)

'''
has_converged: determine if difference in given utility
                tables is within epsilon error
'''
def has_converged(u0, u1):
  epsilon = 0.0001

  for i in range(len(u0)):
    for j in range(len(u0[i])):
      if abs(u0[i][j].utility - u1[i][j].utility) > epsilon:
        return False
  return True

'''
value_iteration:
'''
def value_iteration(results, u_start):
  # Utility tables
  u_old = u_start
  u_new = copy.deepcopy(u_old)

  # Possible actions
  actions = {'up': Coord(0, -1),
              'right': Coord(1, 0),
              'down': Coord(0, 1),
              'left': Coord(-1, 0)}

  


'''
========= MAIN =========
'''
if __name__ == '__main__':
  results = [[None, 50, None],
              [None, 0, -3],
              [-50, -1, -10],
              [None, -3, -2]]

  u_start = [[UCell(), UCell(50, True), UCell()],
              [UCell(), UCell(0), UCell(0)],
              [UCell(-50, True), UCell(0), UCell(0)],
              [UCell(), UCell(0), UCell(0)]]

  u_final = value_iteration(results, u_start)
