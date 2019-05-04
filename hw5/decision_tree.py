'''
CSCI 5512 - AI 2 - HW 5
Nikki Kyllonen
kyllo089

Problem 1: output a decision tree using the heuristic
            based on entropy (as discussed in class)
'''
import sys, math, copy
from Nodes import BTreeNode

# GLOBAL VARIABLES
headers = dict()
examples = dict()

'''
build_ex_dict: parse input file into a dictionary
'''
def build_ex_dict(infile):
  global headers
  global examples

  # parse csv column headers
  h = infile.readline().strip('\n').split(',')

  for i in range(len(h)):
    headers[h[i]] = i
  
  # parse example rows
  for line in infile:
    vals = line.strip('\n').split(',')
    examples[int(vals[0])] = vals[1:len(vals)]
  # END for line

  infile.close()
  return examples

'''
split_on_input: split examples on an input
  - ex_indices: int[]
  - value:      str
output: new BTreeNode()
'''
def split_on_value(ex_indices, value):
  node = BTreeNode(value)  
  val_index = headers[value] - 1

  for e in ex_indices:
    if (examples[e][val_index] == '1'):
      node.left.append(e)
    else:
      node.right.append(e)

  return node

'''
calc_gain: calc gain of splitting given node
'''
def calc_gain(node):
  total_left = len(node.left)
  total_right = len(node.right)
  total = total_left + total_right

  total_true = 0
  total_false = 0
  left_true = 0
  left_false = 0
  right_true = 0
  right_false = 0

  val_index = headers[node.value]
 
  # go through left examples 
  for e in node.left:
    if (examples[e][val_index] == '1'):
      total_true += 1
      left_true += 1
    else:
      total_false += 1
      left_false += 1
  
  # go through right examples
  for e in node.right:
    if (examples[e][val_index] == '1'):
      total_true += 1
      right_true += 1
    else:
      total_false += 1
      right_false += 1

  # calculate entropies
  before = calc_entropy(total_true / total, total_false / total)
  after_t = calc_entropy(left_true / total_left, left_false / total_left)
  after_f = calc_entropy(right_true / total_right, right_false / total_right)

  return before - ((total_left / total)*after_t + (total_right / total)*after_f)

'''
calc_entropy: sum over binary probabilities to calc total entropy
'''
def calc_entropy(p_true, p_false):
  return (-1.0*p_true*math.log2(p_true)) + (-1.0*p_false*math.log2(p_false))

'''
find_max_gain: step through inputs and determine which
                maximizes gain
'''
def find_max_gain(inputs, ex_indices):
  max_gain = -1000
  max_input_node = BTreeNode(None)

  for i in inputs:
    node = split_on_value(ex_indices, i)
    gain = calc_gain(node)

    if (gain > max_gain):
      max_gain = gain
      max_input_node = node

  return max_input_node

'''
'''
def build_tree(inputs, exs):
  # base case
  if (len(exs) < 2):
    return

  # NOTE: do I need to keep track of which inputs I've already split on?
  node = find_max_gain(inputs, exs)
  
  # recursively split each side
  node.left_node = build_tree(inputs, node.left)
  node.right_node = build_tree(inputs, node.right)

  return node

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # default input file
  filename = 'inTree.csv'
  
  if (len(sys.argv) == 2):
    filename = str(sys.argv[1])

  infile = open(filename, 'r')
  build_ex_dict(infile)
  
  inputs = [ h for h in headers if len(h) == 1 ]

  tree = build_tree(inputs, copy.deepcopy(examples))
  print(tree)
