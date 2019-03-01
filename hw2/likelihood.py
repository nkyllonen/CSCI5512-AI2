'''
CSCI 5512 - AI 2 - HW 2
Nikki Kyllonen
kyllo089

Problem 3: Likelihood Weighting
    (25 points)
    Use likelihood weighting to estimate P(g|k,¬b,c). Use an
    appropriate amount of samples, which will require you to
    write code. Submit your your code as a supplement. You
    have the options of Python (preferred), Matlab or Java.
'''

import copy, random
from Network import Node, Network

'''
LH_weighting:
    bnet:       Bayes Net without values
    query:      query variables
    evidence:   evidence variables and values {name: value...}
'''
def LH_weighting(bnet, query, evidence, N):
    # set evidence values
    for e, val in evidence.items():
        bnet.setNodeVal(e, val)

    # keep copy of original state now that evidence values have been set
    bnet_copy = copy.deepcopy(bnet)

    total = 0.0
    y_sum = 0.0
    num_nodes = len(bnet.node_list)

    for i in range(N+1):
        # keep track of which nodes we've visited
        visited = set()
        # keep track of which node values we know
        known = set(evidence.keys())
        weight = 1.0
        matches_query = False
        # make sure we're using the original net to start
        bnet = copy.deepcopy(bnet_copy)
        
        while (len(visited) < num_nodes):
            # find node whose parents are known
            i = random.randint(0, num_nodes-1)
            
            # while node_i's parents are NOT a subset of known
            while (not set(bnet.node_list[i].parents).issubset(known)):
                i = random.randint(0, num_nodes-1)

#            print("Known: " + str(known) + ' -- ', end='')
#            print(str(bnet) + " -- weight = " + str(weight))
            temp = bnet.node_list[i]
#            print("Picked node " + str(i) + " name: " + temp.name)
            
            # check to see if we've visited this node yet
            if (temp.name in visited):
#                print("ALREADY VISITED " + temp.name)
                continue

            prob = bnet.calcProb(temp.name)
#            print("-->calcProb = " + str(prob))

            # if node is an evidence node -> update weight
            if (temp.name in evidence.keys()):
                weight *= prob
            # else set value using random value
            else:
                v = random.random()
                if (v < prob):
                    temp.value = True
                else:
                    temp.value = False

            # add to known and visited values
            known.add(temp.name)
            visited.add(temp.name)

            # check if this node was our query node
            temp_str = '+' + temp.name.lower()
            if (temp.value == False):
                temp_str = temp_str.replace('+','-')
            
            if (temp_str == query):
                matches_query = True

#        print("------- END WHILE -------")
        # --- END WHILE --- #
        total += weight

        if (matches_query):
            y_sum += weight
        
        print(str(bnet) + " -- weight = " + str(weight))

    # --- END FOR ---#
    # final value once finished looping
    return y_sum / total

'''
========= MAIN =========
'''
if __name__ == '__main__':
    # array of Nodes for the Network
    '''nodes = [Node('A', None, [], {'+a':0.3}),
                Node('B', None, [], {'+b':0.6}),
                Node('C', None, ['A'], {'+a': 0.2, '-a': 0.5}),
                Node('D', None, ['A'], {'+a': 0.8, '-a': 0.4}),
                Node('E', None, ['B'], {'+b': 0.8, '-b': 0.1}),
                Node('F', None, [], {'+f': 0.5}),
                Node('G', None, ['C', 'D', 'E'], {'+c': {'+d': {'+e': 0.1, '-e': 0.2},
                        '-d': {'+e': 0.3, '-e': 0.4}, '-c': {'+d': {'+e': 0.5, '-e': 0.6},
                        '-d': {'+e': 0.7, '-e': 0.8}}}}),
                Node('H', None, ['E'], {'+e': 0.4, '-e': 0.7}),
                Node('I', None, ['F', 'G'], {'+f': {'+g': 0.8, '-g': 0.6}, 
                        '-f': {'+g': 0.4, '-g': 0.2}}),
                Node('J', None, ['G', 'H'], {'+g': {'+h': 0.2, '-h': 0.7},
                        '-g': {'+h': 0.9, '-h': 0.1}}),
                Node('K', None, ['I'], {'+i': 0.3, '-i': 0.7})]
    '''
    nodes = [Node('A', None, [], {'+a': 0.2}),
            Node('B', None, ['A'], {'+a': 0.4, '-a': 0.01}),
            Node('C', None, ['A', 'B'], {'+a': {'+b': 1.0, '-b': 0.7},
                    '-a': {'+b': 0.3, '-b': 0.0}})]

    net = Network(nodes)
    net2 = copy.deepcopy(net)

    # sets for P(g | k, -b, c)
    '''query = 'G'
    evidence = {'K': True, 'B': False, 'C': True}
    N = 10'''
    query = 'A'
    evidence = {'B': True}
    N = 10

    P_pos = LH_weighting(net, '+' + query.lower(), evidence, N)
    P_neg = LH_weighting(net2, '-' + query.lower(), evidence, N)

    # normalize results
    P = (1.0/(P_pos + P_neg)) * P_pos

    print("P_pos = " + str(P_pos))
    print("P_neg = " + str(P_neg))
    print("P = " + str(P))
