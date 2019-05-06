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
def output_depth_one(inputs):
  exs = list(examples.keys())

  for i in inputs:
    node = split_on_value(exs, i)
    gain = calc_gain(node)
    node.set_leaf_values(examples, headers, True)

    print(node)
    print('--->gain: {0}'.format(gain))
  # END for i

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # default input file
  filename = 'inTree.csv'
  
  if (len(sys.argv) > 1):
    filename = str(sys.argv[1])

  infile = open(filename, 'r')
  (examples, headers, num_inputs) = build_ex_dict(infile)
  
  inputs = [ h for h in headers if len(h) == 1 ]
  output_depth_one(inputs)
