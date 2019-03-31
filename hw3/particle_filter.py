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

import random, sys

'''
state:
    contains number of particles located
    at each possible state value
    
    possible states: low, med, high
'''
class State:
    def __init__(self, n):
        self.id = n
        self.low = 0
        self.med = 0
        self.high = 0

    def __str__(self):
        return 'State {0}:\nlow = {1}\nmed = {2}\nhigh = {3}'.format(
                self.id, self.low, self.med, self.high)

'''
pt_filtering:

'''
def pt_filtering(evidence, final_t, num_particles):
    # initialize probabilities in adj lists
    x0_probs = {'low' : 0.333, 'med' : 0.333, 'high' : 0.333}
    trans_probs = {'low' : {'low' : 0.6, 'med' : 0.2, 'high' : 0},
        'med' : {'low' : 0.35, 'med' : 0.6, 'high' : 0.5},
        'high' : {'low' : 0.05, 'med' : 0.2, 'high' : 0.5}}
    obs_probs = {True : {'low' : 0, 'med' : 0.05, 'high' : 0.4},
        False : {'low' :  1.0, 'med' : 0.95, 'high' : 0.6}}

    # gather list of States
    states = []
    for i in range(final_t):
        states.append(State(i))

    # 1. sample to initialize State 0
    for i in range(num_particles):
        r = random.random()
        if (r < x0_probs['low']):
            states[0].low = states[0].low + 1
        elif (r < x0_probs['low'] + x0_probs['med']):
            states[0].med = states[0].med + 1
        else:
            states[0].high = states[0].high + 1
    
    print(states[0])

    # 2. loop through states until we reach the final state

'''
========= MAIN =========
'''
if __name__ == '__main__':
    # default
    N = 100

    # get command line input
    if (len(sys.argv) == 2):
        N = int(sys.argv[1])

    # given observed evidence values
    evidence = [False, False, True, True, False, False, False, False, True, False]

    pt_filtering(evidence, 10, N)
