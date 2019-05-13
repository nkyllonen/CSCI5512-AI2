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
from sklearn.ensemble import RandomForestClassifier

# NLTK -- download stopwords data sets
nltk.download('stopwords')
from nltk.corpus import stopwords

# GLOBALS
data_dir = 'data/word2vec-nlp-tutorial/'
train_file = data_dir + 'labeledTrainData.tsv'
test_file = data_dir + 'testData.tsv'
output_file = 'model_output.csv'
stopwords_eng = set(stopwords.words('english'))

'''
clean_data: remove punctuation, numbers, and stopwords
'''
def clean_data(raw_data):
  train_set = []
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
    train_set.append(' '.join(words))

    # output updates
    if (cur % 1000) == 0:
      print('Completed processing review {0} of {1}'.format(cur, total))

    cur += 1
  return train_set

'''
build_bag: build bag of words using cleaned data
            and N max features
'''
def build_bag(data, N):
  print('\nCreating the bag of words...')
  
  # init CountVectorizer -- can tokenize and preprocess
  vectorizer = CountVectorizer(analyzer='word', \
                                tokenizer=None, \
                                preprocessor=None, \
                                stop_words=None, \
                                max_features=N)
  
  # fit_transform() --> 1. fits the model and learns vocab
  #                 --> 2. transform data into feature vectors
  features = vectorizer.fit_transform(data)

  # convert to Numpy array
  #   --> (# reviews) rows by (N features) cols
  features = features.toarray()
  return (features, vectorizer)

'''
'''
def print_top20(features, vectorizer):
  # sum up the counts of each vocab word
  dist = np.sum(features, axis=0) # axis=0 --> x-axis --> vocab
  vocab = vectorizer.get_feature_names()

  tuple_list = [ (v, d) for v, d in zip(vocab, dist) ]
  freq_dict = dict(tuple_list)
  
  # sort flipped tuple_list (vocab : freq #) --> (freq # : vocab) 
  flipped = [ (val, word) for (word, val) in tuple_list ] 
  sort_tups = sorted(flipped, reverse=True)

  print('\n-->top 20 most frequent words:')
  for i in range(0, 20):
    print('{0}\t:\t{1}'.format(sort_tups[i][1], sort_tups[i][0]))

'''
train_forest: use built features and raw data to train
              a random forest with T tree-based classifiers
'''
def train_forest(features, train_data, T):
  # init random forest with T trees
  forest = RandomForestClassifier(n_estimators = T)

  # fit the forest to the traing set
  # - features : bag of words
  # - response variable : sentiment labels
  forest = forest.fit(features, train_data['sentiment'])
  return forest

'''
========= MAIN =========
'''
if __name__ == '__main__':
  # DEFAULTS
  n_features = 5000
  n_trees = 100
  
  # 1. READ IN TRAINING DATA
  #   - header=0 : first line contains column headers
  #   - quoting=3 : ignore double quotes
  train_data = pd.read_csv(train_file, header=0, \
                      delimiter='\t', quoting=3)
  print('\nShape of training data: ', train_data.shape)

  # 2. CLEAN DATA
  print('\nCleaning and parsing the training set...\n')
  train_set = clean_data(train_data)

  # 3. BUILD BAG OF WORDS
  (features_bag, vectorizer) = build_bag(train_set, n_features)
  print('-->shape of generated bag of words: ', features_bag.shape)
  print_top20(features_bag, vectorizer)

  # 4. TRAINING CLASSIFIER
  print('\nTraining the random forest with {0} trees...'.format(n_trees))
  trained_forest = train_forest(features_bag, train_data, n_trees)

  # 5. RUN TRAINED FOREST -- do not need to fit model anymore
  print('*'*20 + '\nUSING TRAINED FOREST\n' + '*'*20)
  test_data = pd.read_csv(test_file, header=0, \
                          delimiter='\t', quoting=3)
  print('\nShape of test data: ', test_data.shape)

  print('\nCleaning and parsing the test set...\n')
  test_set = clean_data(test_data)
  
  # use previously built and populated CountVectorizer
  test_features = vectorizer.transform(test_set)

  print('\nProcessing test set with trained forest...')
  result = trained_forest.predict(test_features)

  print('\nGenerating output...')
  output = pd.DataFrame(data={'id' : test_data['id'], 'sentiment' : result})
  output.to_csv(output_file, index=False, quoting=3)
