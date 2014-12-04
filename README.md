CL1-Project
===========

Verb Frames extraction from Hindi Language Corpus


Requirements
------------
* [shallow_parser_hin](http://ltrc.iiit.ac.in/showfile.php?filename=downloads/shallow_parser.php)
* [full_parser](http://ltrc.iiit.ac.in/showfile.php?filename=downloads/full_parser.php)
* [scipy](http://www.scipy.org/)>=0.12.0
* [gensim](https://pypi.python.org/pypi/gensim)


Usage
-----

Basic usage:
Step 1: Generation of Word2vec model of corpus
In the output directory given, the word2vec model should be generated in binary form.

./word2vec -train [input corpus] -output [output file as in output directory] -cbow 0 -size 2 -window 5 -binary 1 -min-count 0

Step 2: Execution of scripts


./script.py -i [input file] -o [output directory]




