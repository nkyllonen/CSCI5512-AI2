'''
CSCI 5512 - AI 2 - HW 5
Nikki Kyllonen
kyllo089

Problem 1: output a decision tree using the heuristic
            based on entropy (as discussed in class)
'''
import sys

# GLOBAL VARIABLES
headers = dict()

'''
build_ex_dict: parse input file into a dictionary
'''
def build_ex_dict(infile):
  global headers
  examples = dict()

  # parse csv column headers
  h = infile.readline().strip('\n').split(',')

  for i in range(len(h)):
    headers[h[i]] = i

  print(headers)

  # parse example rows
  for line in infile:
    vals = line.strip('\n').split(',')
    examples[int(vals[0])] = vals[1:len(vals)]
  # END for line

  print('\n\nexamples:')
  print(examples)

  infile.close()
  return examples

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # default input file
  filename = 'inTree.csv'
  
  if (len(sys.argv) == 2):
    filename = str(sys.argv[1])

  infile = open(filename, 'r')
  examples = build_ex_dict(infile)
