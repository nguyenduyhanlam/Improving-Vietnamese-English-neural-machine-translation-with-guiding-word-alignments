# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:02:27 2021

@author: lam.nguyen
"""
import nltk
nltk.download('punkt')
from statistics import mean 
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu

PREDICT_FILE = 'opennmt-tf/tst2013.predict.en'
TRUE_FILE = 'opennmt-tf/tst2013.prepared.en'

predict_text = []
with open(PREDICT_FILE, encoding="utf8") as file:
    for line in file:
        predict_text.append(line)

true_text = []
with open(TRUE_FILE, encoding='utf8') as file:
    for line in file:
        true_text.append(line)

hypothesis_list = []
reference_list = []
bleus = []
for predict, true in zip(predict_text, true_text):
    hypothesis = predict.split(' ')
    reference = [true.split(' ')]
    bleu = sentence_bleu(reference, hypothesis)
    bleu = float("{:.5f}".format(bleu))
    print(bleu)
    bleus.append(bleu)

print('Mean bleu:', mean(bleus))