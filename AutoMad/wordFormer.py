# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:47:53 2024

@author: dragon
"""
import pyinflect


"""def inflectCorrect(word, possum):
    e = inflect.engine()
    if possum in ['NNS','NNPS']:
        return e.plural(word)
    if possum == 'VBG':
        return e.present_participle(word)
    if possum == 'VBD':
        return e."""
    
def inflectCorrect(word, possum):
    formed = pyinflect.getInflection(word,possum)
    if formed is not None:
        return formed [0]
    else:
        return word
    
print(inflectCorrect('boringly','RBR'))