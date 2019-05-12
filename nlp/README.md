# Notes
### pipenv problems
- `pip 18.1 causes 'TypeError: 'module' object is not callable'`
    - https://github.com/pypa/pipenv/issues/2924#issuecomment-427773529
    - one solution: lock pip version to 18.0
    ```
    $ pip install pipenv
    $ pipenv run pip install pip==18.0
    $ pipenv install
    ```
    - another solution: actually use 18.1
    ```
    $ pip install --user --upgrade pip # to install latest 18.1
    $ pip install --user git+https://github.com/pypa/pipenv.git
    ```
- 

### Tutorial I am following: `Bag of Words Meets Bags of Popcorn` (Kaggle)
- https://www.kaggle.com/c/word2vec-nlp-tutorial/overview/setting-up-your-system
- installed kaggle as part of pipenv dependencies in order to get tutorial data
- Data: (from: https://www.kaggle.com/c/word2vec-nlp-tutorial/data)
    - Data Set:
      - The labeled data set consists of 50,000 IMDB movie reviews, specially selected for sentiment analysis. The sentiment of reviews is binary, meaning the IMDB rating < 5 results in a sentiment score of 0, and rating >=7 have a sentiment score of 1. No individual movie has more than 30 reviews. The 25,000 review labeled training set does not include any of the same movies as the 25,000 review test set. In addition, there are another 50,000 IMDB reviews provided without any rating labels.
    - File descriptions:
      - labeledTrainData: The labeled training set. The file is tab-delimited and has a header row followed by 25,000 rows containing an id, sentiment, and text for each review.
      - testData: The test set. The tab-delimited file has a header row followed by 25,000 rows containing an id and text for each review. Your task is to predict the sentiment for each one.
      - unlabeledTrainData: An extra training set with no labels. The tab-delimited file has a header row followed by 50,000 rows containing an id and text for each review.
      - sampleSubmission: A comma-delimited sample submission file in the correct format.
