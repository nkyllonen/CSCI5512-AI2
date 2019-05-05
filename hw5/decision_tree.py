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
num_inputs = 0
print_nodes = False

'''
build_ex_dict: parse input file into a dictionary
'''
def build_ex_dict(infile):
  global headers
  global examples
  global num_inputs

  # parse csv column headers
  h = infile.readline().strip('\n').split(',')

  for i in range(len(h)):
    headers[h[i]] = i
    if (len(h[i])==1):
      num_inputs += 1
  # END for i
  
  # parse example rows
  for line in infile:
    vals = line.strip('\n').split(',')
    examples[int(vals[0])] = vals[1:len(vals)]
  # END for line

  infile.close()
  return (examples, headers, num_inputs)

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

  val_index = headers['output'] - 1
 
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
  after_t = 0.0
  after_f = 0.0

  if (total_left > 0):
    after_t = calc_entropy(left_true / total_left, left_false / total_left)
  if (total_right > 0):
    after_f = calc_entropy(right_true / total_right, right_false / total_right)

  return before - ((total_left / total)*after_t + (total_right / total)*after_f)

'''
calc_entropy: sum over binary probabilities to calc total entropy
'''
def calc_entropy(p_true, p_false):
  #print('p_true: {0}\tp_false:{1}'.format(p_true, p_false))

  sum_true = 0.0
  sum_false = 0.0

  if (p_true != 0):
    sum_true = -1.0*p_true*math.log2(p_true)
  if (p_false != 0):
    sum_false = -1.0*p_false*math.log2(p_false)

  return sum_true + sum_false

'''
find_max_gain: step through inputs and determine which
                maximizes gain
'''
def find_max_gain(inputs, ex_indices, visited):
  max_gain = -1000
  max_input_node = BTreeNode(None)

  possible = [ i for i in inputs if i not in visited ]

  for i in possible:
    node = split_on_value(ex_indices, i)
    
    #print(node)

    gain = calc_gain(node)

    #print('--->{0} -- gain: {1}\n'.format(node.value, gain))

    if (gain > max_gain):
      max_gain = gain
      max_input_node = node
  # END for i
  
  if (print_nodes):
    print('\n****CHOSE: {0} -- gain: {1}****'.format(max_input_node.value, max_gain))
    print(max_input_node)

  return max_input_node

'''
build_tree: build tree by recursively building first the left
            child branch, then the right child branch
'''
def build_tree(inputs, exs, visited):
  # base cases
  if (len(exs) < 2):
    return
  elif (len(visited) >= num_inputs):
    return

  node = find_max_gain(inputs, exs, visited)
  visited.append(node.value)

  node.set_leaf_values(examples, headers, False)
  
  # recursively split each side if we need to
  if (node.left != [] and node.right != []):
    node.left_node = build_tree(inputs, node.left, copy.deepcopy(visited))
    node.right_node = build_tree(inputs, node.right, copy.deepcopy(visited))
  return node

'''
'''
def display_tree(root):
  arr = [None] * 10
  arr = node_to_array(root, arr, 1)
  #print(arr)
  
  output = ''

  for val in arr:
    if (val != None):
      output += val + '_'

  # ignore last _ 
  output = output[0:len(output)-1]
  print('\n' + output)
  
'''
'''
def node_to_array(node, arr, index):
  # base cases
  if (node == None or node.value == None):
    return arr

  # double length to make room
  if (2*index + 1 > len(arr)):
    arr = arr + len(arr)*[None]
 
  arr[index] = node.value

  if (arr[index] == None):
    arr[index] = ' '
 
  # check if children are leaves 
  if (node.left_node == None):
    arr[2*index] = node.left_value
  else:
    arr = node_to_array(node.left_node, arr, 2*index)

  if (node.right_node == None):
    arr[2*index + 1] = node.right_value
  else:
    arr = node_to_array(node.right_node, arr, 2*index + 1)

  return arr

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # default input file
  filename = 'inTree.csv'
  
  if (len(sys.argv) > 1):
    filename = str(sys.argv[1])
    if (len(sys.argv) == 3 and sys.argv[2] == 'display'):
      print_nodes = True

  infile = open(filename, 'r')
  build_ex_dict(infile)
  
  inputs = [ h for h in headers if len(h) == 1 ]
  tree = build_tree(inputs, copy.deepcopy(examples), [])
  display_tree(tree)
