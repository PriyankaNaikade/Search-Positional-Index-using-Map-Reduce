#!/usr/bin/env python
from operator import itemgetter
import sys
import re

current_word = None
doclist = ""
word = None
docID = None

for line in sys.stdin:
    line = line.strip()
    word, docID = line.split('\t',1)
    docID = re.sub('hdfs://(.*)/', '', docID)

    if(current_word == word):
        doclist +=  "," + docID
    else:
        if(current_word):
            print('%s\t%s' % (current_word, doclist))
        doclist = docID
        current_word = word

if(current_word == word):
    print('%s\t%s' % (current_word, doclist))