# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 02:36:40 2024

@author: dragon
"""

import random
from dataclasses import dataclass

import numpy as np
import pandas as pd

import wordFormer


@dataclass
class MadDictionary:
    dictionary : pd.DataFrame
    
    def getWord(self, wordType):
        for category in self.dictionary.columns:
            if wordType == category:
            #print(random.choice(df[category].dropna()))
                return random.choice(list(self.dictionary[category].dropna()))
        return wordType
        
    def inCategory(self, word, category):
        print('the category is ' + category)
        return self.dictionary[category].str.fullmatch(word.title()).any()
       
    def getWordInflect(self, wordType, possum):
        for category in self.dictionary.columns:
            if wordType == category:
                newWord = random.choice(list(self.dictionary[category].dropna()))
                newWord = wordFormer.inflectCorrect(newWord, possum)
                return newWord
        return wordType 