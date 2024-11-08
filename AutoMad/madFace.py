# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:08:59 2024

@author: dragon
"""

from flask import Flask, render_template, request, Markup
from madLibFeeder import appleSlices, noPeeling
import wordGrabber
import storySaver
import autoMad
import soupPourer


app = Flask(__name__)

@app.route("/")
def loadHome():
    return render_template("home.html",stories=wordGrabber.getStories())

@app.route("/story", methods = ['POST'])
def story():
    if request.form.get('stories') is not None:
        pickedStory = request.form.get('stories')
        rawStory = wordGrabber.getStory(wordGrabber.getStoryByName(pickedStory))
        if "|" in rawStory:
            story = noPeeling(rawStory)
        else:
            story = autoMad.autoMad(rawStory,33,wordGrabber.getDictionary())
        story = Markup(story)
        return render_template('story.html',story=story)
    if request.form.get('storyPaste') is not None:
        storyIn=request.form.get('storyPaste')
        sillyFactor = request.form.get('sillyness')
        story = autoMad.autoMad(storyIn,int(sillyFactor),wordGrabber.getDictionary())
        story = Markup(story)
        return render_template('story.html',story=story)

@app.route("/renderPage", methods = ['POST'])
def renderPage():
    soupSpoon = request.form.get('targetURL')
    sillyFactor = request.form.get('sillyness')
    pageout = Markup(soupPourer.madPage(soupSpoon,int(sillyFactor)))
    return pageout     

@app.route("/storySaver", methods = ( ['POST']))
def saveStory():
    storySaver.saveStory(request.json.get('story'))
    return '',204


app.run(host = "0.0.0.0") #, debug=True