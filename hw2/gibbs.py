'''
CSCI 5512 - AI 2 - HW 2
Nikki Kyllonen
kyllo089

Problem 4: Gibbs Sampling
    (25 points)
    Use Gibbs sampling to re-estimate P(g|k,¬b,c). Again you
    have to use sufficient samples to be close enough to the
    correct answer (you will lose points if you are too far
    away). Submit your code as a supplement. You have the
    options of Python (preferred), Matlab or Java.
'''

import copy, random, sys
from Network import Node, Network

'''
Gibbs_sampling:
    bnet:       Bayes Net without values
    query:      query variables
    evidence:   evidence variables and values {name: value...}
    N:          # iterations
    f:          file pointer
    do_write:   bool indicating y/n file writing
'''
def Gibbs_sampling(bnet, query, evidence, N, f, do_write):
    # set evidence values
    for e, val in evidence.items():
        bnet.setNodeVal(e, val)
    
    # keep copy of original state now that evidence
    # values have been set
    bnet_copy = copy.deepcopy(bnet)

    total = 0.0
    y_sum_query = 0.0
    y_sum_other = 0.0
    num_nodes = len(bnet.node_list)

    # randomly initialize entire network
    known = set(evidence.keys())
    for node in bnet.node_list:
        if (node.name not in known):
            i = random.randint(0,1)
            if (i == 0):
                node.value = True
            else:
                node.value = False

    print(bnet)

#    for i in range(N+1):

'''
========= MAIN =========
'''
if __name__ == '__main__':
    # default values
    filename = "output.txt"
    N = 10
    do_write = True

    # array of Nodes for the Network
    nodes = [Node('A', None, [], {'C', 'D'}, {'+a':0.3}),
                Node('B', None, [], {'E'}, {'+b':0.6}),
                Node('C', None, ['A'], {'G'}, {'+a': 0.2, '-a': 0.5}),
                Node('D', None, ['A'], {'G'}, {'+a': 0.8, '-a': 0.4}),
                Node('E', None, ['B'], {'G', 'H'}, {'+b': 0.8, '-b': 0.1}),
                Node('F', None, [], {'I'}, {'+f': 0.5}),
                Node('G', None, ['C', 'D', 'E'], {'I', 'J'}, {'+c': {'+d': {'+e': 0.1, '-e': 0.2},
                        '-d': {'+e': 0.3, '-e': 0.4}, '-c': {'+d': {'+e': 0.5, '-e': 0.6},
                        '-d': {'+e': 0.7, '-e': 0.8}}}}),
                Node('H', None, ['E'], {'J'}, {'+e': 0.4, '-e': 0.7}),
                Node('I', None, ['F', 'G'], {'K'}, {'+f': {'+g': 0.8, '-g': 0.6}, 
                        '-f': {'+g': 0.4, '-g': 0.2}}),
                Node('J', None, ['G', 'H'], set(), {'+g': {'+h': 0.2, '-h': 0.7},
                        '-g': {'+h': 0.9, '-h': 0.1}}),
                Node('K', None, ['I'], set(), {'+i': 0.3, '-i': 0.7})]
    
    '''nodes = [Node('A', None, [], {'+a': 0.2}),
            Node('B', None, ['A'], {'+a': 0.4, '-a': 0.01}),
            Node('C', None, ['A', 'B'], {'+a': {'+b': 1.0, '-b': 0.7},
                    '-a': {'+b': 0.3, '-b': 0.0}})]
    '''
    net = Network(nodes)
    net2 = copy.deepcopy(net)

    # sets for P(g | k, -b, c)
    query = 'G'
    evidence = {'K': True, 'B': False, 'C': True}
    
    # test network
    '''query = 'A'
    evidence = {'B': True}'''

    f = None

    Gibbs_sampling(net, '+' + query.lower(), evidence, N, f, do_write)
