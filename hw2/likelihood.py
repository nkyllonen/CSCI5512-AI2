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

import copy, random, sys
from Network import Node, Network

'''
LH_weighting:
    bnet:       Bayes Net without values
    query:      query variables
    evidence:   evidence variables and values {name: value...}
    N:          # iterations
    f:          file pointer
    do_write:   bool indicating y/n file writing
'''
def LH_weighting(bnet, query, evidence, N, f, do_write):
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

    for i in range(N):
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
            y_sum_query += weight
        else:
            y_sum_other += weight
        
#        print(str(bnet) + " -- weight = " + str(weight))
        if (do_write):
            f.write(str(bnet) + " -- weight = " + str(weight) + '\n')

    # --- END FOR ---#
    # final value once finished looping
    return {'match': y_sum_query / total, 'other': y_sum_other / total}

'''
========= MAIN =========
'''
if __name__ == '__main__':
    # default values
    filename = "output.txt"
    N = 10
    do_write = True

    # get command line input
    if (len(sys.argv) > 1):
        filename = str(sys.argv[1])

        # check if we want to output to file or not
        if (filename == "no-output"):
            do_write = False

        if (len(sys.argv) == 3):
            N = int(sys.argv[2])
        elif (len(sys.argv) > 3):
            print('''ERROR: Invalid number of arguments.\\
                    Expected pattern: python3 <pyfile> <filename> <OPT: N value>\\
                    Expected pattern: python3 <pyfile> <OPT: 'no-output'> <OPT: N value>''')
            exit()
    
    # array of Nodes for the Network
    nodes = [Node('A', None, [], {'C', 'D'}, {'+a':0.3}),
                Node('B', None, [], {'E'}, {'+b':0.6}),
                Node('C', None, ['A'], {'G'}, {'+a': 0.2, '-a': 0.5}),
                Node('D', None, ['A'], {'G'}, {'+a': 0.8, '-a': 0.4}),
                Node('E', None, ['B'], {'G', 'H'}, {'+b': 0.8, '-b': 0.1}),
                Node('F', None, [], {'I'}, {'+f': 0.5}),
                Node('G', None, ['C', 'D', 'E'], {'I', 'J'}, {'+c': {'+d': {'+e': 0.1, '-e': 0.2},
                        '-d': {'+e': 0.3, '-e': 0.4}}, '-c': {'+d': {'+e': 0.5, '-e': 0.6},
                        '-d': {'+e': 0.7, '-e': 0.8}}}),
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

    if (do_write):
        f = open(filename, "w")
    result_dict= LH_weighting(net, '+' + query.lower(), evidence, N, f, do_write)

    P_pos = result_dict['match']
    P_neg = result_dict['other']

    # normalize results
    P = (1.0/(P_pos + P_neg)) * P_pos

    print("P_pos = " + str(P_pos))
    print("P_neg = " + str(P_neg))
    print("P = " + str(P))
