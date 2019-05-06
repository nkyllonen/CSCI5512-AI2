'''
CSCI 5512 - AI 2 - HW 5
Nikki Kyllonen
kyllo089

Problem 2: Build depth-one trees
'''
import sys, math, copy
from decision_tree import build_ex_dict, split_on_value, calc_gain, calc_entropy
from Nodes import BTreeNode

# GLOBAL VARIABLES
headers = dict()
examples = dict()
num_inputs = 0

'''
output_depth_one: output possible splits using given inputs
'''
def output_depth_one(inputs, depth):
  exs = list(examples.keys())
  node_dict = {}

  for i in inputs:
    node = split_on_value(exs, i)
    node_dict[node.value] = node
    gain = calc_gain(node)

    if (depth == 1):
      node.set_leaf_values(examples, headers, True)
      print(node)
      print('--->gain: {0}'.format(gain))
    else:
      node.set_leaf_values(examples, headers, False)
  # END for i
  return node_dict

'''
'''
def three_trees(inputs, nodes):
  exs = list(examples.keys())
  
  # 1. all possible combinations
  triples = []
  for i in range(len(inputs)):
    for j in range(i+1, len(inputs)):
      s = inputs[i] + inputs[j]
      for k in range(j+1, len(inputs)):
        triples.append(s + inputs[k])
    # END for j
  # END for i
  print(triples)

  # 2. calculate combined accuracies
  max_acc = -100
  max_trip = ''
  #triples = ['ABC']
  for t in triples:
    # gather corresponding nodes
    triplet = []
    for ch in t:
      triplet.append(nodes[ch])
    # step through all examples
    acc = 0.0
    for e in exs:
      a = 1.0
      a *= triplet[0].accuracy_of(e, examples, headers)
      a *= triplet[1].accuracy_of(e, examples, headers)
      a *= triplet[2].accuracy_of(e, examples, headers)
      acc += a
      #print('ex {0} : a = {1}'.format(e, a))
    print('{0} splits with {1:0.2f}% accuracy'.format(t, acc*100.0))
    if (acc > max_acc):
      max_acc = acc
      max_trip = t
  print('\nMAX ACCURACY: {0} at {1:0.2f}%'.format(max_trip, max_acc*100.0))

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # default input file
  filename = 'inTree.csv'
  depth = 1

  if (len(sys.argv) > 1):
    filename = str(sys.argv[1])
    if (len(sys.argv) == 3):
      depth = int(sys.argv[2])

  infile = open(filename, 'r')
  (examples, headers, num_inputs) = build_ex_dict(infile)
  
  inputs = [ h for h in headers if len(h) == 1 ]
  node_dict = output_depth_one(inputs, depth)

  if (depth == 3):
    three_trees(inputs, node_dict)
