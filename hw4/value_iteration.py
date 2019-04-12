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

import random, sys

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
    self.index    (Coord) : (i, j) indices of this cell
    self.best_act (str)   : direction of best action to take
    self.is_end   (bool)  : T/F is this an end state cell
  '''
  def __init__(self, u, pos, end):
    self.utility = u
    self.index = pos
    self.best_act = ""
    self.is_end = end

  def __str__(self):
    if (self.is_end == False):
      return str(self.index) , ' : {0} - {1}'.format(self.utility, self.best_act)
    else:
      return str(self.index) , ' : {0}'.format(self.utility)

