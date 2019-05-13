'''
Nikki Kyllonen - kyllo089
CSCI 5512 Final Project

Bags of Popcorn Movie Classifier -- binary sentiment classification
- tutorial: https://www.kaggle.com/c/word2vec-nlp-tutorial/overview/description
'''
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re, nltk
from sklearn.feature_extraction.text import CountVectorizer

# NLTK -- download stopwords data sets
nltk.download('stopwords')
from nltk.corpus import stopwords

# GLOBALS
data_dir = 'data/word2vec-nlp-tutorial/'
stopwords_eng = set(stopwords.words('english'))

'''
clean_data: remove punctuation, numbers, and stopwords
'''
def clean_data(raw_data):
  reviews = []
  total = raw_data['review'].size # get column size
  cur = 0

  for r in raw_data['review']:
    # following BeautifulSoup UserWarning -- specify parser
    cleaned = BeautifulSoup(r, features='html.parser')

    # substitute not letters with spaces
    letters_only = re.sub('[^a-zA-Z]', ' ', cleaned.get_text())
    lower_case = letters_only.lower()
    words = lower_case.split()
    
    # remove stop words
    words = [ w for w in words if w not in stopwords_eng ]
    reviews.append(' '.join(words))

    # output updates
    if (cur % 1000) == 0:
      print('Completed processing review {0} of {1}'.format(cur, total))

    cur += 1
  #print(reviews[0])
  return reviews

'''
'''
def build_bag(reviews, N):
  print('\nCreating the bag of words...')
  
  # init CountVectorizer -- can tokenize and preprocess
  vectorizer = CountVectorizer(analyzer='word', \
                                tokenizer=None, \
                                preprocessor=None, \
                                stop_words=None, \
                                max_features=N)
  
  # fit_transform() --> 1. fits the model and learns vocab
  #                 --> 2. transform data into feature vectors
  train_features = vectorizer.fit_transform(reviews)

  # convert to Numpy array
  #   --> (# reviews) rows by (N features) cols
  train_features = train_features.toarray()
  return (train_features, vectorizer)

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # 1. READ IN TRAINING DATA
  #   - header=0 : first line contains column headers
  #   - quoting=3 : ignore double quotes
  train = pd.read_csv(data_dir + 'labeledTrainData.tsv', header=0,\
                      delimiter='\t', quoting=3)

  # 2. CLEAN DATA
  print('\nCleaning and parsing the training set movie reviews...\n')
  reviews = clean_data(train)
  #print(reviews[0])

  # 3. BUILD BAG OF WORDS
  (bag, vectorizer) = build_bag(reviews, 5000)
  print('shape of generated bag of words: ', bag.shape)

  # sum up the counts of each vocab word
  dist = np.sum(bag, axis=0) # axis=0 --> x-axis --> vocab
  vocab = vectorizer.get_feature_names()

  tuple_list = [ (v, d) for v, d in zip(vocab, dist) ]
  freq_dict = dict(tuple_list)
  
  # sort summations descending
  #d = dist.tolist()
  #d.sort(reverse=True)

  # sort tuple_list (vocab : freq #)
  flipped = [ (val, word) for (word, val) in tuple_list ] 
  sort_tups = sorted(flipped, reverse=True)

  print('top 20 most frequent words across all reviews:\n')
  for i in range(0, 20):
    print('{0}\t:\t{1}'.format(sort_tups[i][1], sort_tups[i][0]))

