# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:14:59 2024

@author: dragon
"""

import random
import re
import wordGrabber
import madLibFeeder
import madDictionary
import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

NOUNS = ["NN","NNS"]
VERBS = ["EX","MD","VB","VBD","VBG","VBN","VBP","VBZ"]
CONJUNCTIONS =["CC"]
NUMBER = ["CD","LS"]
ADJECTIVES = ["JJ","JJR","JJS","WDT"]
ADVERBS = ["RB","RBR","RBS","RP","WRB"]
SILLIES = ["UH"]
UNKNOWN = ["FW","PDT","POS"]
PREPOSITIONS = ["IN","TO","WP","WP$"]
PRONOUNS = ["PRP","PRP$"]
ARTICLES = ["DT"]
NAMES = ["NNP","NNPS"]

def posToCategory(pos):
    if pos in NOUNS:
        return 'noun'
    if pos in VERBS:
        return 'verb'
    if pos in CONJUNCTIONS:
        return 'conjunction'
    if pos in NUMBER:
        return 'number'
    if pos in ADJECTIVES:
        return 'adjective'
    if pos in ADVERBS:
        return 'adverb'
    if pos in SILLIES:
        return 'sillyword'
    if pos in UNKNOWN:
        return 'sillyword'
    if pos in PREPOSITIONS:
        return 'preposition'
    if pos in PRONOUNS:
        return 'pronoun'
    if pos in ARTICLES:
        return 'article'
    if pos in NAMES:
        return 'name'
    return pos + "word Not Found"
        
def autoMad(story, percent, dictionary):
    story.replace("'","'")
    words = re.split(r"(?<!')\b(?!')",story)
    libout = ""
    for word in words:
        if re.fullmatch("[A-Za-z'0-9]+", word) is not None and random.random()<.01*percent:            
            if dictionary.inCategory(word, 'pokemon'):
                libout += dictionary.getWord('pokemon')
            else:
                wordTypes=nltk.pos_tag(nltk.word_tokenize(word))
                wordpart = wordTypes[0]    
                pos = wordpart[1]
                wordType = posToCategory(pos)
                newWord = dictionary.getWordInflect(wordType,pos)
                libout += newWord
                print(wordpart[0] + ' ' + pos + ' ' + newWord)
                if len(wordTypes)>1:
                    wordpart = wordTypes[1]    
                    pos = wordpart[1]
                    wordType = posToCategory(pos)
                    newWord = dictionary.getWordInflect(wordType,pos)
                    libout += ' ' + newWord
                    print(wordpart[0] + ' ' + pos + ' ' + newWord)
                    
        else:
            libout += word 
    #madStory = madLibFeeder.wholeApple(libout, result)
    libout=libout.replace("\n","<br>")
    return libout
    
    

