'''
CSCI 5512 - AI 2 - HW 5
Nikki Kyllonen
kyllo089

Node Classes
'''

class BTreeNode:
  '''
  value:  str
  left:   int[] -- when True
  right:  int[] -- when False
  '''
  def __init__(self, val, left = None, right = None):
    self.value = val
    self.left = left or []
    self.right = right or []
    self.left_node = None
    self.right_node = None
    self.left_value = ' '
    self.right_value = ' '
    self.accuracy = 0.0

  def __str__(self):
    return '''\nvalue: {0}
              {0}.left = {1} : \t{3}
              {0}.right = {2} : \t{4}'''.format(
              self.value, self.left_value, self.right_value, self.left, self.right)

  '''
  set_leaf_values: determine T/F value for left and right
  '''
  def set_leaf_values(self, examples, headers, display):
    out = headers['output'] - 1

    if (self.left == []):
      self.left_value = ' '
      return
    if (self.right == []):
      self.right_value = ' '
      return

    left_true = 0
    for e in self.left:
      if (examples[e][out] == '1'):
        left_true += 1

    right_true = 0
    for e in self.right:
      if (examples[e][out] == '1'):
        right_true += 1
   
    # assign according to majority
    self.accuracy = 0.0
    if (left_true/len(self.left) > 0.5):
      self.left_value = '1'
      self.accuracy += left_true
    else:
      self.left_value = '0'
      self.accuracy += (len(self.left) - left_true)
    
    if (right_true/len(self.right) > 0.5):
      self.right_value = '1'
      self.accuracy += right_true
    else:
      self.right_value = '0'
      self.accuracy += (len(self.right) - right_true)

    self.accuracy /= len(examples)
    # display how many of each
    if (display):
      print('\n{0}.left:  {1}T, {2}F'.format(
            self.value, left_true, len(self.left)-left_true))
      print('{0}.right: {1}T, {2}F'.format(
            self.value, right_true, len(self.right)-right_true))
      print('--->{0} splits with {1}% accuracy'.format(self.value, 100.0*self.accuracy))

  '''
  accuracy_of: return accuracy of given evidence
  '''
  def accuracy_of(self, eid, examples, headers):
    output = examples[eid][headers['output']-1]

    # if our left branch classification matches
    if (output == self.left_value):
      if (eid in self.left):
        return self.accuracy
      else:
        return 1-self.accuracy
    # if our right branch classification matches
    else:
      if (eid in self.right):
        return self.accuracy
      else:
        return 1-self.accuracy
