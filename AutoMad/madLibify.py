# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:46:00 2024

@author: dragon
"""

import random

wordTypes = ["noun","verb","adjective","adverb","body","preposition"]

def madLibify(madlib):
    #print(madlib)
    madLibOut=""
    words = madlib.split(" ")
    for word in words:
        if random.random()<.1:
            word = random.choice(wordTypes)
        madLibOut = madLibOut + word + " "
    return(madLibOut)    
        