# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:36:29 2024

@author: dragon
"""

import random
import sillyWordMaker

def verb():
    return(random.choice(verbs)+" ")

def noun():
    return(random.choice(nouns)+" ")

def adjective():
    return(random.choice(adjectives)+" ")

def adverb():
    return(random.choice(adverbs)+" ")

def preposition():
    return(random.choice(prepositions)+" ")

def pokemons():
    return(random.choice(pokemon)+" ")

def pokemonMoves():
    return(random.choice(pokemonMove)+" ")

def hero():
    return(random.choice(heroes)+" ")

def pluralNoun():
    return(noun().strip()+"s ")

def verbing():
    return(verb().strip()+"ing ")

def body():
    return(random.choice(bodyParts)+" ")

def dwelling():
    return(random.choice(dwellings)+" ")

def team():
    return(random.choice(teams)+" ")

def sillyWord():
    return(sillyWordMaker.sillyWord()+" ")

def word(word):
    match word:
        case "pokemon":
            return pokemons()
        case "pokemonMove":
            return pokemonMoves()
        case "hero":
            return hero()
        case "dwelling":
            return dwelling()
        case "team":
            return team()
        case "noun":
            return noun()
        case _:
            return word
        

verbs = ["eat","sneeze","read","jump","jog", "destroy", "poop", "smack", "fart", "play","fly","run","walk","burp","talk"]
nouns = ["Jabba the Hutt", "slice of pizza", "piece of cheese","cow", "poopy the poop", 
         "monster", "lava", "poop", "computer", "face", "fire","gem","moth","math problem","rocket"]
adjectives = ["annoying", "loud","poopy","wet", "dry", "boring", "hard", "five-headed"]
adverbs = ["crazily", "slowly", "poopily", "quickly", "very", "powerfully", "noisily"]
prepositions = ["over", "under", "around", "above", "behind", "in", "in front of", "on", "below", "up"]
bodyParts = ["head","eye","leg","foot","nose","ear","kidney","belly button","hand","arm","forehead","mouth","nostril","butt","tongue","tooth"]
heroes = ["Kyrre","Pyre","Lord Haart","Sandro","Nimbus","Styg","Gunnar","Dessa","Clavius","Gelu","Cathrine","Adrienne",
          "Caitlin","Valeska","Nagash"]
troops = ["wood elves","grand elves","centuars","centuar captains","dwarves","battle dwarves",
          "angels","archangels","devils","genies","azure dragons","wyvern monarchs","titans","giants","chaos hydras",
          "gremlins","phoenixes", "fairy dragons","cyclopses","cyclops kings"]
dwellings = ["pyre","homestead","portal of glory","estate","cliff nest", "golden pavillion", "serpent fly hive"]
teams = ["castle","tower","rampart","dungeon","fortress","inferno","conflux","stronghold","necropolis"]
spells = ["magic arrow","meteor shower","slow", "bless","ice bolt","frost ring","chain lightning","resurrection","haste"
          ,"prayer", "town portal","dimension door"]
resources = ["gold","wood","ore","gems","mercury","crystals","sulfur"]
pokemon = ["mewtwo", "pikachu","raichu","gyarados","charmeleon","blastoise","wartortle","tentacruel","kabuto","pichu",
           "aerodactyl","voltorb","electrode","diglett","ivysaur","charizard","muk","togepi","mew","vaporeon","grimer","ponyta","poliwrath"
           ,"butterfree","slowpoke","victreebel"]
pokemonMove = ["earthquake","flamethrower","fire spin", "liquidation","hydro pump","shadow ball","dazzling gleam","razor leaf","moonblast",
                "energy ball","megahorn","stone edge","dragon claw","thunderbolt","air cutter","magnet bomb","sludge bomb", "psybeam"
                ,"dynamic punch","surf","confusion"]

