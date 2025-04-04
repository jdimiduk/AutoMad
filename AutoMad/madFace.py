# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:08:59 2024

@author: dragon
"""

from flask import Flask, Markup, render_template, request
from pathlib import Path
import pandas as pd
import json

from madLibFeeder import noPeeling
import autoMad
import soupPourer
import storySaver
import wordGrabber

frontend  = Path(__file__).parent /"mad-front"/"dist"
app = Flask(__name__,  template_folder = frontend, static_folder = frontend, static_url_path = "")
#app = Flask(__name__)


@app.route("/", methods = (['GET']))
def serveReact():
    return render_template("index.html")

@app.route("/stories", methods = (["GET"]))
def getStories():
    return wordGrabber.getStories().to_json()
    
@app.route("/story", methods = (["POST"]))
def getStory():
    pickedStory = request.form.get('stories')
    rawStory = wordGrabber.getStory(wordGrabber.getStoryByName(pickedStory))
    if "|" in rawStory: #is used in prepared stories with manual word choice, they should not go through the automatic process
        story = noPeeling(rawStory)
    else:
        story = autoMad.autoMad(rawStory,33,wordGrabber.getDictionary()).replace("\n","<br>")
    storyJson = '{"story": "' + story + '"}'
    return storyJson
    
@app.route("/text", methods = (["POST"]))
def madText():
    text = request.form.get('text')
    sillyFactor = request.form.get('sillyness')
    story = autoMad.autoMad(text,int(sillyFactor),wordGrabber.getDictionary(), ['pokemon'])
    storyJson = '{"story": "' + story + '"}'
    return storyJson

@app.route("/storySaver", methods = ( ['POST']))
def saveStory():
    storySaver.saveStory(request.json.get('story'))
    return '',204


app.run(host = "0.0.0.0") #, debug=True