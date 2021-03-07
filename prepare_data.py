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

LIMIT_LENGTH = 100
LIMIT_RATIO = 1.5

SOURCE_FILE = 'data/train.clean.vi'
TARGET_FILE = 'data/train.clean.en'
COMBINE_FILE = 'opennmt-tf/train.clean.vi-en'
SOURCE_PREPARED_FILE = 'opennmt-tf/train.prepared.vi'
TARGET_PREPARED_FILE = 'opennmt-tf/train.prepared.en'

VALID_SOURCE = 'data/tst2012.true.vi'
VALID_TARGET = 'data/tst2012.true.en'
VALID_SOURCE_PREPARED_FILE = 'opennmt-tf/tst2012.prepared.vi'
VALID_TARGET_PREPARED_FILE = 'opennmt-tf/tst2012.prepared.en'

TEST_SOURCE = 'data/tst2013.true.vi'
TEST_TARGET = 'data/tst2013.true.en'
TEST_SOURCE_PREPARED_FILE = 'opennmt-tf/tst2013.prepared.vi'
TEST_TARGET_PREPARED_FILE = 'opennmt-tf/tst2013.prepared.en'

def filterPair(s):
    return len(s.split(' ')) <= LIMIT_LENGTH
        
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
        if(not filterPair(line)):
            continue
        source_text.append(line)

target_text = []
with open(TARGET_FILE, encoding='utf8') as file:
    for line in file:
        if(not filterPair(line)):
            continue
        target_text.append(line)

for source, target in zip(source_text, target_text):
    source_length = len(source.split(' '))
    target_length = len(target.split(' '))
    if((source_length / target_length > LIMIT_RATIO) or
       (target_length / source_length > LIMIT_RATIO)):
        source_text.remove(source)
        target_text.remove(target)
    else:
        source = normalizeString(source).rstrip()
        target = normalizeString(target).rstrip()
        
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

combine_text = []
for source, target in zip(source_text, target_text):
    source_tokenize = word_tokenize(source)
    target_tokenize = word_tokenize(target)
    source_raw = InsertSpace(source_tokenize)
    target_raw = InsertSpace(target_tokenize)
    combine_raw = source_raw + ' ||| ' + target_raw
    combine_text.append(combine_raw)

print(combine_text[0])

# Print to file
with open(COMBINE_FILE, 'w', encoding='utf8') as file:
    for item in combine_text:
        file.write("%s\n" % item)
        
# Print to file
with open(SOURCE_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in source_text:
        file.write("%s" % item)

with open(TARGET_PREPARED_FILE, 'w', encoding='utf8') as file:
    for item in target_text:
        file.write("%s" % item)

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