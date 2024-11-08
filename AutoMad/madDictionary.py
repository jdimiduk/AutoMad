# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 02:36:40 2024

@author: dragon
"""

from dataclasses import dataclass
import numpy as np
import pandas as pd
import random
import wordFormer

@dataclass
class madDictionary:
    dictionary : pd.DataFrame
    
    def getWord(self, wordType):
        for category in self.dictionary.columns:
            if wordType == category:
            #print(random.choice(df[category].dropna()))
                return random.choice(list(self.dictionary[category].dropna()))
        return wordType
        
    def inCategory(self, word, category):
        if self.dictionary[category].str.fullmatch(word.title()).any():
            return True
        return False
    
    def getWordInflect(self, wordType, possum):
        for category in self.dictionary.columns:
            if wordType == category:
            #print(random.choice(df[category].dropna()))
                newWord = random.choice(list(self.dictionary[category].dropna()))
                newWord = wordFormer.inflectCorrect(newWord, possum)
                return newWord
        return wordType