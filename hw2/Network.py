'''
CSCI 5512 - AI 2 - HW 2
Nikki Kyllonen
kyllo089

Node and Network classes
'''
import copy, random

class Node:
    '''
    name:       string
    value:      boolean or None
    parents:    [string...]     # must be an array for cond_prob ordering
    children:   [string...]
    cond_prob:  {string: {string : float}...}
    '''
    def __init__(self, n, val, rents, kids, probs):
        self.name = n
        self.value = val
        self.parents = rents
        self.children = kids
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

    def getNode(self, name):
        for n in self.node_list:
            if (n.name == name):
                return n

    def setNodeVal(self, name, val):
        n = self.getNode(name)
        n.value = val

    # calculate conditional probability : P(X | Parents(X))
    #   name:   name of node X
    def calcProb(self, name):
        n = self.getNode(name)

        # if this node has no parents
        if (n.parents == []):
            val = n.cond_prob['+' + name.lower()]
            
            if (n.value == False):
                val = 1.0 - val    
            return val

        dict_val = n.cond_prob
        
        # loop through the parents, checking their values
        for p in n.parents:
            p_node = self.getNode(p)
            p_val = p_node.value
            p_key = '+' + p_node.name.lower()

            if (p_val == False):
                p_key = p_key.replace('+', '-')
            
            dict_val = dict_val[p_key]

        # negate if current node's value is negative
        if (n.value == False):
            dict_val = 1.0 - dict_val
        return dict_val
    
    # calculate unnormalized Markov Blanket probability
    #   name:   name of node X
    def calcUnnormalizedBlanket(self, name):
        n = self.getNode(name)
        prob = self.calcProb(name)

        # loop through children
        for c in n.children:
            prob *= self.calcProb(c)

        return prob

    # calculate Markov Blanket probability :
    # P(X | MarkovBlanket(X))
    #   name:   name of node X
    def calcBlanketProb(self, name):
        n = self.getNode(name)

        # calculate with positive X
        n.value = True
        p_pos = self.calcUnnormalizedBlanket(name)

        n.value = False
        p_neg = self.calcUnnormalizedBlanket(name)

        # normalize --> return positive result
        return (1.0 / (p_pos + p_neg)) * p_pos
