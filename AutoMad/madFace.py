# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:08:59 2024

@author: dragon
"""

from flask import Flask, Markup, render_template, request

from madLibFeeder import noPeeling
import autoMad
import soupPourer
import storySaver
import wordGrabber

app = Flask(__name__)

@app.route("/")
def loadHome():
    return render_template("home.html",stories=wordGrabber.getStories())

@app.route("/story", methods = ['POST'])
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
    return render_template('story.html',story='no story foun')

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