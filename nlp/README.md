# Notes
## pipenv problems
- `pip 18.1 causes 'TypeError: 'module' object is not callable'`
    - https://github.com/pypa/pipenv/issues/2924#issuecomment-427773529
    - one solution: lock pip version to 18.0
    ```
    $ pip install pipenv
    $ pipenv run pip install pip==18.0
    $ pipenv install
    ```
    - another solution: actually ust 18.1
    ```
    $ pip install --user --upgrade pip # to install latest 18.1
    $ pip install --user git+https://github.com/pypa/pipenv.git
    ```
- 

## Tutorial I am following: `Bag of Words Meets Bags of Popcorn` (Kaggle)
https://www.kaggle.com/c/word2vec-nlp-tutorial/overview/setting-up-your-system
