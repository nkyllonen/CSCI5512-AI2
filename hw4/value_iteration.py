'''
CSCI 5512 - AI 2 - HW 4
Nikki Kyllonen
kyllo089

Problem 3: Value Iteration
  (20 points)
  Assume that when moving there is a 70% chance to
  end up where you want to go and a 15% chance to
  end up 90 degrees left/right

  Given 4 rows x 3 columns Rewards & gamma = 0.8 
'''

import random, sys, copy, math
import Util

from Util import UCell, Coord

'''
value_iteration:
'''
def value_iteration(rewards, u_start, gamma):
  # Utility tables
  u_old = u_start
  u_new = copy.deepcopy(u_old)

  # Possible actions
  actions = {'up': Coord(-1, 0),
              'right': Coord(0, 1),
              'down': Coord(1, 0),
              'left': Coord(0, -1)}
  '''
  actions = {'up': Coord(0, 1),
              'right': Coord(1, 0),
              'down': Coord(0, -1),
              'left': Coord(-1, 0)}
  '''
  # Probabilities
  P_straight = 0.7
  P_right = 0.15
  P_left = 0.15

  # Loop until convergence
  converged = False
  count = 0
  
  while (not converged):
    for i in range(len(u_old)):
      for j in range(len(u_old[i])):
        # Calculate updated values --> u_new
        # Bellman Equation:
        #   s' = (i', j') = (i, j) + action
        #   u_new(i,j) = R(i,j) + gamma * MAX_action(SUM_s'(P(s'|s(i,j), action)*u_old(s')))
        if (u_old[i][j].utility is not None and u_old[i][j].is_end is False):
          max_sum = -1000

          for a in actions:
            sum_a = 0
            # we go where we intend to
            s_next = Util.correct_next(u_old, Coord(i,j), Coord(i, j) + actions[a])
            sum_a = sum_a + (P_straight*u_old[s_next.x][s_next.y].utility)
            
            # we go to the right instead
            s_next = Util.correct_next(u_old, Coord(i,j), Coord(i, j) + Util.turn(actions[a], -90))
            sum_a = sum_a + (P_right*u_old[s_next.x][s_next.y].utility)
            
            # we go to the left instead
            s_next = Util.correct_next(u_old, Coord(i,j), Coord(i, j) + Util.turn(actions[a], 90))
            sum_a = sum_a + (P_left*u_old[s_next.x][s_next.y].utility)

            # compare to max
            if (sum_a > max_sum):
              max_sum = sum_a
              u_new[i][j].best_act = a
          # END for a
          
          u_new[i][j].utility = rewards[i][j] + gamma * max_sum
          # END if valid, non-end state
      # END for j
    # END for i
    converged = Util.has_converged(u_old, u_new)

    # Place new values into u_old
    u_old = copy.deepcopy(u_new)
    count = count + 1
  # END while
  print('-- {0} iterations --'.format(count))  

  return u_new

'''
========= MAIN =========
'''
if __name__ == '__main__':
  rewards = [[None, 50, None],
              [None, 0, -3],
              [-50, -1, -10],
              [None, -3, -2]]

  u_start = [[UCell(), UCell(50, True), UCell()],
              [UCell(), UCell(0), UCell(0)],
              [UCell(-50, True), UCell(0), UCell(0)],
              [UCell(), UCell(0), UCell(0)]]

  if (len(sys.argv) == 2 and str(sys.argv[1]) == "zeros"):
    u_start = [[UCell(), UCell(0, True), UCell()],
                [UCell(), UCell(0), UCell(0)],
                [UCell(0, True), UCell(0), UCell(0)],
                [UCell(), UCell(0), UCell(0)]]

  gamma = 0.8

  #print('rewards: ' , rewards)

  print('u_start:')
  Util.print2D(u_start)

  u_final = value_iteration(rewards, u_start, gamma)
  
  print('\nu_final:')
  Util.print2D(u_final)
