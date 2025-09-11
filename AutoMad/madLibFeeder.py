# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:23:26 2024

@author: dragon
"""

import re

import sillyWordMaker
import wordGrabber

#import nltk

def getName(character, name):
    if character[0] == name:
        return character[1]
    return ""

def appleSlices(story):
    madlib = wordGrabber.getStory(wordGrabber.getStoryByName(story))
    return noPeeling(madlib)

def noPeeling(madlib):
    #print(madlib)
    madwords = madlib.split("|")
    libout = "" 
    characters = []
    
    madDictionary = wordGrabber.getDictionary()
    
    for word in madwords:
        if bool(re.search('&',word)):
            character = word.split(",")
            chickenNugget = ""
            for person in characters:
                gotName=getName(person,character[0])
                if len(gotName)>0:
                    chickenNugget=gotName
            if len(chickenNugget)>0:
                libout+=chickenNugget
            elif len(character)>1:
                chickenNugget = madDictionary.getWord(character[1])
                characters.append([character[0],chickenNugget])
                libout+=chickenNugget
        elif word == 'sillyword':
            libout += sillyWordMaker.sillyWord()
        elif (not bool(re.search(' ',word))):
            libout+=madDictionary.getWord(word)
        else:
            libout += word   
    libout=libout.replace("\n","<br>")
    return(libout)

def wholeApple(madlib, result):
    madwords = madlib.split("|")
    libout="" 
    characters = []
    
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
    #libout=libout.replace("\n","<br>")
    return(libout)