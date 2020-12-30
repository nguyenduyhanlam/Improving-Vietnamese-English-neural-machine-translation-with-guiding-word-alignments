# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:12:54 2020

@author: lam.nguyen
"""
import nltk
from nltk.tokenize import word_tokenize
import html
import re

SOURCE_FILE = 'data/train.clean.vi'
TARGET_FILE = 'data/train.clean.en'
COMBINE_FILE = 'data/train.clean.vi-en'

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