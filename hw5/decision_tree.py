'''
CSCI 5512 - AI 2 - HW 5
Nikki Kyllonen
kyllo089

Problem 1: output a decision tree using the heuristic
            based on entropy (as discussed in class)
'''
import sys
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

  #print(headers)

  # parse example rows
  for line in infile:
    vals = line.strip('\n').split(',')
    examples[int(vals[0])] = vals[1:len(vals)]
  # END for line

  #print('\n\nexamples:')
  #print(examples)

  infile.close()

'''
split_on_input: split examples on an input
  - ex_indices: int[]
  - value:      str
output: new BTreeNode()
'''
def split_on_value(ex_indices, value):
  global headers
  global examples

  node = BTreeNode(value)  

  for e in ex_indices:
    if (examples[e][headers[value] == 1):
      node.left.append(e)
    else:
      node.right.append(e)

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
