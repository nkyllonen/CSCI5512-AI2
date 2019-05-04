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

  def __str__(self):
    return '''\nvalue: {0}
              {0}.left: {1}
              {0}.right: {2}'''.format(
              self.value, self.left, self.right)
