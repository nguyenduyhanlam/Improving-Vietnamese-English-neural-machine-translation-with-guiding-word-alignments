# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:12:54 2020

@author: lam.nguyen
"""
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import html
import re

SOURCE_FILE = 'data/train.clean.vi'
TARGET_FILE = 'data/train.clean.en'
COMBINE_FILE = 'opennmt-tf/train.clean.vi-en'
SOURCE_PREPARED_FILE = 'opennmt-tf/train.prepared.vi'
TARGET_PREPARED_FILE = 'opennmt-tf/train.prepared.en'

VALID_SOURCE = 'data/tst2012.true.vi'
VALID_TARGET = 'data/tst2012.true.en'
COMBINE_VALID_FILE = 'opennmt-tf/valid.clean.vi-en'
VALID_SOURCE_PREPARED_FILE = 'opennmt-tf/tst2012.prepared.vi'
VALID_TARGET_PREPARED_FILE = 'opennmt-tf/tst2012.prepared.en'

TEST_SOURCE = 'data/tst2013.true.vi'
TEST_TARGET = 'data/tst2013.true.en'
TEST_SOURCE_PREPARED_FILE = 'opennmt-tf/tst2013.prepared.vi'
TEST_TARGET_PREPARED_FILE = 'opennmt-tf/tst2013.prepared.en'
        
# Normalize the string (marks and words are seperated, words don't contain accents,...)
def normalizeString(s):
    s = html.unescape(s)
    # Seperate words and marks by adding spaces between them
    marks = '[.!?,-${}()]'
    r = "(["+"\\".join(marks)+"])"
    s = re.sub(r, r" \1 ", s)
    # replace continuous spaces with a single space
    s = re.sub(r"\s+", r" ", s).strip()
    return s

source_text = []
with open(SOURCE_FILE, encoding="utf8") as file:
    for line in file:
        source_text.append(normalizeString(line))

target_text = []
with open(TARGET_FILE, encoding='utf8') as file:
    for line in file:
        target_text.append(normalizeString(line))
        
valid_source_text = []
with open(VALID_SOURCE, encoding="utf8") as file:
    for line in file:
        valid_source_text.append(normalizeString(line))

valid_target_text = []
with open(VALID_TARGET, encoding='utf8') as file:
    for line in file:
        valid_target_text.append(normalizeString(line))

test_source_text = []
with open(TEST_SOURCE, encoding="utf8") as file:
    for line in file:
        test_source_text.append(normalizeString(line))

test_target_text = []
with open(TEST_TARGET, encoding='utf8') as file:
    for line in file:
        test_target_text.append(normalizeString(line))
        
def InsertSpace(token):
    result = ''
    
    for text in token:
        result += text + ' '
    
    return result.rstrip()

def GenerateCombineText(source, target):
    combine = []
    for source, target in zip(source, target):
        source_tokenize = word_tokenize(source)
        target_tokenize = word_tokenize(target)
        source_raw = InsertSpace(source_tokenize)
        target_raw = InsertSpace(target_tokenize)
        combine_raw = source_raw + ' ||| ' + target_raw
        combine.append(combine_raw)
    return combine
    
combine_text = GenerateCombineText(source_text, target_text)
combine_valid_text = GenerateCombineText(valid_source_text, valid_target_text)

print(combine_text[0])

# Print to file
with open(COMBINE_FILE, 'w', encoding='utf8') as file:
    for item in combine_text:
        file.write("%s\n" % item)
 
# Print to file
with open(COMBINE_VALID_FILE, 'w', encoding='utf8') as file:
    for item in combine_valid_text:
        file.write("%s\n" % item)
        
# Print to file
with open(SOURCE_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in source_text:
        file.write("%s\n" % item)

with open(TARGET_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in target_text:
        file.write("%s\n" % item)

with open(VALID_SOURCE_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in valid_source_text:
        file.write("%s\n" % item)

with open(VALID_TARGET_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in valid_target_text:
        file.write("%s\n" % item)

with open(TEST_SOURCE_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in test_source_text:
        file.write("%s\n" % item)

with open(TEST_TARGET_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in test_target_text:
        file.write("%s\n" % item)