# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:12:54 2020

@author: lam.nguyen
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.align import AlignedSent
from nltk.align import IBMModel1

SOURCE_FILE = 'data/train.clean.vi'
TARGET_FILE = 'data/train.clean.en'

TEST_SOURCE = 'data/tst2013.true.vi'
TEST_TARGET = 'data/tst2013.true.en'

source_text = []
with open(SOURCE_FILE, encoding="utf8") as file:
    for line in file:
        source_text.append(line)

target_text = []
with open(TARGET_FILE, encoding='utf8') as file:
    for line in file:
        target_text.append(line)

combine_text = []
for source, target in zip(source_text, target_text):
    source_tokenize = word_tokenize(source)
    target_tokenize = word_tokenize(target)
    combine_text.append(AlignedSent(source_tokenize, target_text))

ibm1 = IBMModel1(combine_text, 5)

test_sentence = combine_text[2]
test_sentence.words
test_sentence.mots
test_sentence.alignment

test_source_text = []
with open(TEST_SOURCE, encoding="utf8") as file:
    for line in file:
        test_source_text.append(line)

test_target_text = []
with open(TEST_TARGET, encoding='utf8') as file:
    for line in file:
        test_target_text.append(line)
        
