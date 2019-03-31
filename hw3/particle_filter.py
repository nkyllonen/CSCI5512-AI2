'''
CSCI 5512 - AI 2 - HW 2
Nikki Kyllonen
kyllo089

Problem 4: Particle Weighting
    (25 points)
    Use particle filtering to estimate:
        P(x10 | e1=“not flooded”, e2=“not flooded”,
                e3=“flooded”, e4=“flooded”,
                e5=“not flooded”, e6=“not flooded”,
                e7=“not flooded”, e8=“not flooded”,
                e9=“flooded”, e10=“not flooded”)
    (i.e. the days “flooded” are 3,4 and 9. The rest are “not flooded”.)
    Give the number of particles used in your sampling, along with the
    probability for the water table values.
'''

import random

'''
state:
    contains number of particles located
    at each possible state value
    
    possible states: low, med, high
'''
class State:
    def __init__(self, n):
        self.id = n
        self.low_N = 0
        self.med_N = 0
        self.high_N = 0

'''
pt_filtering:

'''
def pt_filtering():

