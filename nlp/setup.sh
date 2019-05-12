#!/bin/sh
echo ---------------------------------------------------
echo extracting data...
lrzip -d data/word2vec-nlp-tutorial.tar.lrz
tar -C data/ -xvf data/word2vec-nlp-tutorial.tar
echo data successfully extracted
echo ---------------------------------------------------

echo using pipenv to set up environment...
pipenv install
echo environment successfully set up
echo ---------------------------------------------------


