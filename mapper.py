#!/usr/bin/env python
import os
import sys
def split_into_words(text):
    word_list = []
    word_list_spl = []
    current_word = []
    # splitting text into words. each character is checked and eliminated if it is a special character or a number. Once a whitespace is encountered it appends all the characters verified till that space into a word
    for each_char in text:
        if each_char.isalpha():
            current_word.append(each_char)
            #print("alpha:", current_word)
        elif current_word:
            word = u''.join(current_word)
            #print("elif:",word, "len of word", len(word))
            word_list_spl.append(word)
            #print("wlist:",word_list_spl)
            current_word = []
    # Moving all the words to a list post removal of numbers, special characters
    if current_word:
        word = u''.join(current_word)
        word_list_spl.append(word)

    word_list_pos = []
    noStop_lowerCase_words = []

    #Next looping through word_list_pos list and converting words to lowercase and Check if there is word which is a Stop_word and exclude them from being appended to another list
    for word in word_list_spl:
        if word.lower() in ('and', 'but', 'is', 'the', 'to'):
            continue
        noStop_lowerCase_words.append(word.lower())
    return noStop_lowerCase_words

for line in sys.stdin:
    words = split_into_words(line)
    for word in words:
        print ('%s\t%s' % (word, os.environ["map_input_file"]))