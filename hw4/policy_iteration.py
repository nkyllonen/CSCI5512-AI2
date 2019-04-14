'''
CSCI 5512 - AI 2 - HW 4
Nikki Kyllonen
kyllo089

Problem 4: Policy Iteration
  (15 points)
  Assume that when moving there is a 70% chance to
  end up where you want to go and a 15% chance to
  end up 90 degrees left/right

  Given 4 rows x 3 columns Rewards & gamma = 0.8
  Start by assuming all actions are "up"
'''

import random, sys, copy, math
import Util

from Util import UCell, Coord

# for solving linear system
import numpy as np

'''
policy_iteration:
'''
def policy_iteration(rewards, utils, gamma):
  # Possible actions
  actions = {'up': Coord(-1, 0),
            'right': Coord(0, 1),
            'down': Coord(1, 0),
            'left': Coord(0, -1)}

  # Probabilities
  P_straight = 0.7
  P_right = 0.15
  P_left = 0.15

  # Coefficients -- 3D float array
  coeffs = [[None, None, None],
            [None, [], []],
            [None, [], []],
            [None, [], []]]

  # Loop until convergence
  converged = False
  count = 0
 
  while (not converged):
    # reset coefficients
    coeffs = [[None, None, None],
              [None, [], []],
              [None, [], []],
              [None, [], []]]

    for i in range(len(utils)):
      for j in range(len(utils[i])):
        '''
        1. Calculate coefficient values using guessed actions
           - Bellman Update without MAX:
             a = utils(i,j).best_act
             s' = (i',j') = (i, j) + a
             utils(i,j) = R(i,j) + gamma * SUM_s'[P(s'|s(i,j), a)*u(s')]
        '''
        if (utils[i][j].utility is not None and utils[i][j].is_end is False):
          a = utils[i][j].best_act
          
          # we go where we intend to
          s_next = Util.correct_next(utils, Coord(i,j), Coord(i,j) + actions[a])
          coeffs[s_next.x][s_next.y].append(gamma*P_straight)
          
          # we go to the right instead
          s_next = Util.correct_next(utils, Coord(i,j), Coord(i,j) + Util.turn(actions[a], -90))
          coeffs[s_next.x][s_next.y].append(gamma*P_right)

          # we go to the left instead
          s_next = Util.correct_next(utils, Coord(i,j), Coord(i,j) + Util.turn(actions[a], 90))
          coeffs[s_next.x][s_next.y].append(gamma*P_left)
      # END for j
    # END for i
    '''
    2. Solve linear system --> Calculate utilities
        a = [ C[i][j] ]
        b = [ R[i][j] ]
    '''

  # END while


'''
========= MAIN =========
'''
if __name__ == '__main__':
  rewards = [[None, 50, None],
              [None, 0, -3],
              [-50, -1, -10],
              [None, -3, -2]]
  
  utils = [[UCell(), UCell(50, True), UCell()],
            [UCell(), UCell(0, False, 'up'), UCell(0, False, 'up')],
            [UCell(-50, True), UCell(0, False, 'up'), UCell(0, False, 'up')],
            [UCell(), UCell(0, False, 'up'), UCell(0, False, 'up')]]

  print('utils: ')
  Util.print2D(utils)

  print('flat: ')
  Util.print1D(Util.flatten(utils, True))
