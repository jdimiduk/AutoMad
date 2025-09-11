# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:08:59 2024

@author: dragon
"""

from flask import Flask, Markup, render_template, request
from pathlib import Path
import pandas as pd
import json
from flask_cors import CORS, cross_origin

from madLibFeeder import noPeeling
import autoMad
import soupPourer
import storySaver
import wordGrabber

frontend  = Path(__file__).parent /"mad-front"/"dist"
app = Flask(__name__,  template_folder = frontend, static_folder = frontend, static_url_path = "")

#CORS(app)

@app.route("/storyz", methods = ['POST'])
def story():
    pickedStory = request.form.get('stories')
    if pickedStory is not None:
        rawStory = wordGrabber.getStory(wordGrabber.getStoryByName(pickedStory))
        if "|" in rawStory: #is used in prepared stories with manual word choice, they should not go through the automatic process
            story = noPeeling(rawStory)
        else:
            story = autoMad.autoMad(rawStory,33,wordGrabber.getDictionary()).replace("\n","<br>")
        story = Markup(story)
        return render_template('story.html',story=story)
    autoStory = request.form.get('storyPaste')
    if autoStory is not None:
        sillyFactor = request.form.get('sillyness')
        story = autoMad.autoMad(autoStory,int(sillyFactor),wordGrabber.getDictionary(), ['pokemon'])
        story = Markup(story)
        return render_template('story.html',story=story)
    return render_template('story.html',story='no story found')

@app.route("/renderPage", methods = ['POST'])
def renderPage():
    soupSpoon = request.form.get('targetURL')
    sillyFactor = request.form.get('sillyness')
    pageout = soupPourer.madPage(soupSpoon,int(sillyFactor))
    pageoutJson = json.dumps(pageout)
    pageJson= '{"html": ' + pageoutJson + '}'
    return pageJson

@app.route("/storySaver", methods = ( ['POST']))
def saveStory():
    storySaver.saveStory(request.json.get('story'))
    return '',204

@app.route("/", methods = (['GET']))
def serveReact():
    return render_template("index.html")

@app.route("/stories", methods = (["GET", "OPTIONS"]))
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
    storyDump = json.dumps(story)
    storyJson = '{"story": ' + storyDump + '}'
    return storyJson
    
@app.route("/text", methods = (["POST"]))
def madText():
    text = request.form.get('text')
    sillyFactor = request.form.get('sillyness')
    story = autoMad.autoMad(text,int(sillyFactor),wordGrabber.getDictionary(), ['pokemon'])
    storyDump = json.dumps(story)
    storyJson = '{"story": ' + storyDump + '}'
    return storyJson



app.run(host = "0.0.0.0") #, debug=True