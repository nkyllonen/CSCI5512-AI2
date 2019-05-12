#!/bin/sh
echo ---------------------------------------------------
echo unzipping data...
unzip data/word2vec-nlp-tutorial.zip -d data
echo data successfully unzipped into data/
echo ---------------------------------------------------

echo using pipenv to set up environment...
pipenv install
echo environment successfully set up
echo ---------------------------------------------------


