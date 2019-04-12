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

import random, sys, copy, math

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
turn: return Coord representing Coord c rotated deg degrees
'''
def turn(c, deg):
  rad = math.radians(deg)
  return Coord(c.x*math.cos(rad) - c.y*math.sin(rad), c.x*math.sin(rad) + c.y*math.cos(rad))

'''
value_iteration:
'''
def value_iteration(rewards, u_start, gamma):
  # Utility tables
  u_old = u_start
  u_new = copy.deepcopy(u_old)

  # Possible actions
  actions = {'up': Coord(0, 1),
              'right': Coord(1, 0),
              'down': Coord(0, -1),
              'left': Coord(-1, 0)}

  # Probabilities
  P_straight = 0.7
  P_right = 0.15
  P_left = 0.15

  # Loop until convergence
  converged = False
  while (!converged):
    for i in range(len(u_old)):
      for j in range(len(u_old[i])):
        # Calculate updated values --> u_new
        # Bellman Equation:
        #   s' = (i', j') = (i, j) + action
        #   u_new(i,j) = R(i,j) + gamma * MAX_action(SUM_s'(P(s'|s(i,j), action)*u_old(s')))
        if (u_old[i][j].value != None and u_old[i][j].is_end == False_:
          max_sum = -1000

          for a in actions:
            sum_a = 0
            # we go where we intend to
            s_next = Coord(i, j) + actions[a]
            sum_a = sum_a + (P_straight*u_old[s_next.x][s_next.y])
            
            # we go to the right instead
            s_next = Coord(i,j) + turn(actions[a], 90)
            sum_a = sum_a + (P_right*u_old[s_next.x][s_next.y])
            
            # we go to the left instead
            s_next = Coord(i,j) + turn(actions[a], -90)
            sum_a = sum_a + (P_left*u_old[s_next.x][s_next.y])

            # compare to max
            if (sum_a > max_sum):
              max_sum = sum_a
          # END for a
          
          u_new[i][j].value = rewards[i][j] + gamma * max_sum
          # END if valid, non-end state
      # END for j
    # END for i
    converged = has_converged(u_old, u_new)

    # Place new values into u_old
    u_old = copy.deepcopy(u_new)
  # END while

  return u_new

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

  gamma = 0.8

  u_final = value_iteration(results, u_start, gamma)
