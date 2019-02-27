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

class Node:
    '''
    name:       string
    value:      boolean or None
    parents:    [string...]
    cond_prob:  {string: {string : float}...}
    '''
    def __init__(self, n, val, rents, probs):
        self.name = n
        self.value = val
        self.parents = rents
        self.cond_prob = probs

    # return string representation --> for print()
    def __str__(self):
        if (self.value == True):
            return ' +' + self.name
        elif (self.value == False):
            return ' -' + self.name
        else:
            return self.name

class Network:
    '''
    node_list:  [Node...]
    '''
    def __init__(self, nodes):
        self.node_list = nodes

    # return string representation --> for print()
    def __str__(self):
        out = '['

        for n in self.node_list:
            out = out + str(n) + ' '

        out = out + ']'
        return out

    def setNodeVal(self, name, val):
        for n in self.node_list:
            if (n.name == name):
                n.value = val
                return

    # calculate conditional probability : P(X | Parents(X))
    def calcProb(self, name):
        
        return 0.0


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
    bnet_orig = copy.deepcopy(bnet)

    # keep track of which nodes we've visited
    visited = {}
    # keep track of which node values we know
    known = set(evidence.keys())
    total = 0.0
    y_sum = 0.0
    num_nodes = len(bnet)

    for i in range(N):
        # random ordering
        #random.shuffle(bnet.node_list)
        
        weight = 1.0
        
        while (len(visited) < num_nodes):
            # find node whose parents are known
            i = random.randint(0, num_nodes-1)
            
            # while node_i's parents are NOT a subset of known
            while (not set(bnet.node_list[i].parents).issubset(known)):
                i = random.randint(0, num_nodes-1)

            temp = bnet.node_list[i]
            prob = bnet.calcProb(temp.name)

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

        # reset values
        visited = {}


'''
========= MAIN =========
'''
if __name__ == '__main__':
    # array of Nodes for the Network
    nodes = [Node('A', None, [], {'+a':0.3}),
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

    net = Network(nodes)

    # sets for P(g | k, -b, c)
    query = 'G'
    evidence = {'K': True, 'B': False, 'C': True}
    N = 10

    P = LH_weighting(net, query, evidence, N)
