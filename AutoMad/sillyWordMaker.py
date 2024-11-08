# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:45:38 2024

@author: dragon
"""

import string
import random


vowels = ["a","e","i","o","u","y"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]


def sillyWord():
    sillyword = ""
    vowel = False
    wordlength = random.randint(3, 7)
    for i in range(wordlength):
        if vowel==False:
            sillyword = sillyword + random.choice(consonants)
            vowel=True
        elif vowel==True:
            sillyword= sillyword + random.choice(vowels)
            vowel=False
    return(sillyword)