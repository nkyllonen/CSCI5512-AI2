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
    self.left_value = None
    self.right_value = None

  def __str__(self):
    return '''\nvalue: {0}
              {0}.left: {1}
              {0}.right: {2}'''.format(
              self.value, self.left, self.right)

  '''
  set_leaf_values: determine T/F value for left and right
  '''
  def set_leaf_values(self, examples, headers):
    out = headers['output'] - 1

    if (self.left == []):
      self.left_value = None
      return
    if (self.right == []):
      self.right_value = None
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
    if (left_true/len(self.left) > 0.5):
      self.left_value = '1'
    else:
      self.left_value = '0'
    
    if (right_true/len(self.right) > 0.5):
      self.right_value = '1'
    else:
      self.right_value = '0'
