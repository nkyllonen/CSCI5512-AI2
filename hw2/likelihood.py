```
CSCI 5512 - AI 2 - HW 2
Nikki Kyllonen
kyllo089

Problem 3: Likelihood Weighting
```

class Node:
    ```
    name: string
    value: boolean or None
    parents: [string...]
    cond_prob: {string: {string : float}...}
    ```
    def __init__(self, n, val, rents, probs):
        self.name = n
        self.value = val
        self.parents = rents
        self.cond_prob = probs

    def __repr__(self):
        if (self.value == True):
            print(' +' , self.name , end='')
        elif (self.value == False):
            print(' -' , self.name , end='')
        else:
            print(self.name, end-'')

class Network:
    ```
    node_list: [Node]
    ```
    def __init__(self, nodes):
        self.node_list = nodes

    def __repr__(self):
        print('[', end='') #print without endline

        for n in node_list:
            print(n)

        print(']', end='')

### MAIN ###
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

