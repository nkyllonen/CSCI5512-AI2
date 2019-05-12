'''
Nikki Kyllonen - kyllo089
CSCI 5512 Final Project

Bags of Popcorn Movie Classifier
'''
import pandas as pd
from bs4 import BeautifulSoup
import re

# GLOBALS
data_dir = 'data/'

# 1. READ IN TRAINING DATA
#   - header=0 : first line contains column headers
#   - quoting=3 : ignore double quotes
train = pd.read_csv(data_dir + 'labeledTrainData.tsv', header=0,\
                    delimiter='\t', quoting=3)

#print('train["review"][0]' , train["review"][0])

# 2. CLEAN DATA
# 2.1 get review text only -- without tags or markup
'''
ex1 = BeautifulSoup(train["review"][0])
print(ex1.get_text()) # cleaned up, text only
'''
# 2.2 clean out punctuation and numbers
'''
letters_only = re.sub('[^a-zA-Z]', ' ', reviews[0])
print(letters_only)
'''

reviews = []
for r in train['review']:
  # following BeautifulSoup UserWarning -- specify parser
  cleaned = BeautifulSoup(r, features='html.parser')
  # substitute not letters with spaces
  letters_only = re.sub('[^a-zA-Z]', ' ', cleaned.get_text())
  lower_case = letters_only.lower()
  words = lower_case.split()
  reviews.append(words)
print(reviews[0])

