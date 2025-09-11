# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:14:59 2024

@author: dragon
"""

import random
import re
from typing import Optional

import nltk

import madDictionary

NOUN = 'noun'
VERB = 'verb'
CONJUNCTION = 'conjunction'
NUMBER = 'number'
ADJECTIVE = 'adjective'
ADVERB = 'adverb'
SILLYWORD = 'sillyword'
PREPOSITION = 'preposition'
PRONOUN = 'pronoun'
ARTICLE = 'article'
NAME = 'name'

POS_MAPPING = {
    'NN': NOUN, 'NNS': NOUN,
    'EX': VERB, 'MD': VERB, 'VB': VERB, 'VBD': VERB, 'VBG': VERB, 'VBN': VERB, 'VBP': VERB, 'VBZ': VERB,
    'CC': CONJUNCTION,
    'CD': NUMBER, 'LS': NUMBER,
    'JJ': ADJECTIVE, 'JJR': ADJECTIVE, 'JJS': ADJECTIVE, 'WDT': ADJECTIVE,
    'RB': ADVERB, 'RBR': ADVERB, 'RBS': ADVERB, 'RP': ADVERB, 'WRB': ADVERB,
    'UH': SILLYWORD, 
    'FW': SILLYWORD, 'PDT': SILLYWORD, 'POS': SILLYWORD, # these are not handled yet so we just make them silly for now
    'IN': PREPOSITION, 'TO': PREPOSITION, 'WP': PREPOSITION, 'WP$': PREPOSITION,
    'PRP': PRONOUN, 'PRP$': PRONOUN,
    'DT': ARTICLE,
    'NNP': NAME, 'NNPS': NAME
    }

def posToCategory(pos):
    return POS_MAPPING[pos]
    
        
def autoMad(story, percent, madDictionary, replaceCategories = None):
    if replaceCategories == None:
        replaceCategories = []
    words = re.split(r"(?<!')\b(?!')",story) #split the story on word boundries
    newStory = [maybeReplace(word, percent, madDictionary, replaceCategories) for word in words]
    return ''.join(newStory)
  
def maybeReplace(word: str, percent: int, madDictionary: madDictionary.MadDictionary, replaceCategories: Optional[list[str]]) -> str: 
    if re.fullmatch("[A-Za-z'0-9]+", word) is not None and random.random()<.01*percent:
        return processWord(word, madDictionary, replaceCategories)
    return word
                           
  
def processWord(word, madDictionary, replaceCategories):
    for category in replaceCategories:
        if madDictionary.inCategory(word, category):
            return madDictionary.getWord(category)
    wordTypes=nltk.pos_tag(nltk.word_tokenize(word))
    wordpart = wordTypes[0]    
    pos = wordpart[1]
    wordType = posToCategory(pos)
    newWord = madDictionary.getWordInflect(wordType,pos)
    wordOut = ''
    wordOut += newWord
    if len(wordTypes)>1: #just to handle contractions
        wordpart = wordTypes[1]    
        pos = wordpart[1]
        wordType = posToCategory(pos)
        newWord = madDictionary.getWordInflect(wordType,pos)
        wordOut += ' ' + newWord
    return wordOut
    
    

