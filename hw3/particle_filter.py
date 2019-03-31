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
    def __init__(self, n, total):
        self.id = n
        self.low = 0
        self.med = 0
        self.high = 0
        self.total = total

    def __str__(self):
        return 'State {0}:\nlow = {1}, P(low) = {4}\nmed = {2}, P(med) = {5}\nhigh = {3}, P(high) = {6}'.format(
                self.id, self.low, self.med, self.high,
                self.low/self.total, self.med/self.total, self.high/self.total)

'''
pt_filtering:

'''
def pt_filtering(evidence, final_t, num_particles):
    # initialize probabilities in adj lists
    x0_probs = {'low' : 0.33333, 'med' : 0.33333, 'high' : 0.33333}
    trans_probs = {'low' : {'low' : 0.6, 'med' : 0.35, 'high' : 0.05},
        'med' : {'low' : 0.2, 'med' : 0.6, 'high' : 0.2},
        'high' : {'low' : 0.0, 'med' : 0.5, 'high' : 0.5}}
    obs_probs = {True : {'low' : 0, 'med' : 0.05, 'high' : 0.4},
        False : {'low' :  1.0, 'med' : 0.95, 'high' : 0.6}}

    # gather list of States
    states = []
    for i in range(final_t+1):
        states.append(State(i, num_particles))

    # 1. sample to initialize State 0
    sample(num_particles, states[0], x0_probs)
    
    #print(states[0])

    # 2. loop through states until we reach the final state
    for t in range(1,final_t+1):
        # 2.1 sample to populate: state[t-1] --> state[t]
        low_old = states[t-1].low
        med_old = states[t-1].med
        high_old = states[t-1].high
        
        sample(low_old, states[t], trans_probs['low'])
        sample(med_old, states[t], trans_probs['med'])
        sample(high_old, states[t], trans_probs['high'])

        # 2.2 weight samples using observed evidence
        low_w = states[t].low * obs_probs[evidence[t]]['low']
        med_w = states[t].med * obs_probs[evidence[t]]['med']
        high_w = states[t].high * obs_probs[evidence[t]]['high']

        # 2.3 resample using total weight
        total_w = low_w + med_w + high_w
        resample_probs = {'low' : low_w / total_w,
            'med' : med_w / total_w,
            'high' : high_w / total_w}
   
        # zero out current values
        states[t] = State(t, num_particles)
        sample(num_particles, states[t], resample_probs)
    
    #print (resample_probs)    

    # 3. output final state + probabilities
    print(states[final_t])

'''
sample:
    updates current state values
    using given transiion probabiliies
'''
def sample(old_val, cur_state, probs):
    for i in range(old_val):
        r = random.random()
        if (r < probs['low']):
            cur_state.low = cur_state.low + 1
        elif (r < probs['low'] + probs['med']):
            cur_state.med = cur_state.med + 1
        else:
            cur_state.high = cur_state.high + 1

'''
========= MAIN =========
'''
if __name__ == '__main__':
    # default
    N = 100

    # get command line input
    if (len(sys.argv) == 2):
        N = int(sys.argv[1])

    # given observed evidence values -- e0 doesn't exist
    evidence = [None, False, False, True, True, False, False, False, False, True, False]

    pt_filtering(evidence, 10, N)
