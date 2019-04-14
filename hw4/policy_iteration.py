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

