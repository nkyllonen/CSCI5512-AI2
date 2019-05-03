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
  def __init__(self, val):
    self.value = val
    self.left = []
    self.right = []

  def __str__(self):
    return self.value
