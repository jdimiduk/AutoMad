# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:23:26 2024

@author: dragon
"""

import re

import madLibify
import sillyWordMaker
import wordGrabber
import wordPicker

#import nltk

def getName(character, name):
    if character[0] == name:
        return character[1]
    return ""

def appleSlices():
    return None

#request = input("type a file name: ")
#madlib = open(request, "r").read()
madlib = wordGrabber.getStory('10jrRkAKDfXZBkRdI0v5g-A2sFm5Wf4ar-mLsC6K7Qew')

#print(nltk.pos_tag(madlib))
#print(madlib)

#madwords = madlib.split("|")
#madlib = madLibify.madLibify(madlib)


madwords = madlib.split("|")

libout="" 
characters = []
sillyword = 'sillyword'

result=wordGrabber.getGoogleSheet()

for word in madwords:
    if bool(re.search('&',word)):
        character = word.split(",")
        chickenNugget=""
        for person in characters:
            gotName=getName(person,character[0])
            if len(gotName)>0:
                chickenNugget=gotName
        if len(chickenNugget)>0:
            libout+=chickenNugget
        elif len(character)>1:
            chickenNugget = wordGrabber.getWordFromResult(result,character[1])
            characters.append([character[0],chickenNugget])
            libout+=chickenNugget
    elif word == 'sillyword':
        libout += sillyWordMaker.sillyWord()
    elif (not bool(re.search(' ',word))):
        libout+=wordGrabber.getWordFromResult(result,word)
    else:
        libout += word

# for word in madwords:
#     match word:
#         case "nouns":
#             libout+=wordPicker.pluralNoun().strip()
#         case "noun":
#             libout+=wordPicker.noun().strip()
#         case "verb":
#             libout+=wordPicker.verb().strip()
#         case "verbing":
#             libout+=wordPicker.verbing().strip()
#         case "body":
#             libout+=wordPicker.body().strip()
#         case "adverb":
#             libout+=wordPicker.adverb().strip()
#         case "adjective":
#             libout+=wordPicker.adjective().strip()
#         case "preposition":
#             libout+=wordPicker.preposition().strip()
#         case "pokemon":
#             libout+=wordPicker.word('pokemon').strip()
#         case "pokemonMove":
#             libout+=wordPicker.word('pokemonMove').strip()
#         case "hero":
#             libout+=wordPicker.word('hero').strip()
#         case "dwelling":
#             libout+=wordPicker.word('dwelling').strip()
#         case "team":
#             libout+=wordPicker.word('team').strip()
#         case "sillyword":
#             libout+=sillyWordMaker.sillyWord()
#         case _ :
#             if bool(re.search('&',word)):
#                 character = word.split(",")
#                 chickenNugget=""
#                 for person in characters:
#                     gotName=getName(person,character[0])
#                     if len(gotName)>0:
#                         chickenNugget=gotName
#                 if len(chickenNugget)>0:
#                     libout+=chickenNugget.strip()
#                 else:
#                     chickenNugget = wordPicker.word(character[1])
#                     characters.append([character[0],chickenNugget])
#                     libout+=chickenNugget.strip()
#             else: 
#                 libout=libout + word # + " "
            
print(libout)