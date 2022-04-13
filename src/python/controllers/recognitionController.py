#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests
#recognition
import speech_recognition as sr
#speak
from gtts import gTTS

from cheese.ErrorCodes import Error
from cheese.resourceManager import ResMan
from cheese.modules.cheeseController import CheeseController as cc

#@controller /recognition
class RecognitionController(cc):

	#@post /fromWav
	@staticmethod
	def fromWav(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 400)
			return

		args = cc.readBytes(server)

		if (not args):
			Error.sendCustomError(server, "No bytes in request", 400)
			return

		pathToFile = RecognitionController.findRecordingName()

		with open(pathToFile, "wb") as f:
			f.write(args)

		r = sr.Recognizer()

		file = sr.AudioFile(pathToFile)
		with file as source:
			audio = r.record(source)
		try:
			text = r.recognize_google(audio).lower()
		except:
			response = cc.createResponse({'TEXT': "I did not understand"}, 204)
			cc.sendResponse(server, response)
			os.remove(pathToFile)
			return

		os.remove(pathToFile)
		response = cc.createResponse({'TEXT': text}, 200)
		cc.sendResponse(server, response)

	#@post /toMp3
	@staticmethod
	def toMp3(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 400)
			return

		args = cc.readArgs(server)

		if (not cc.validateJson(["TEXT"], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		pathToFile = RecognitionController.findRecordingName()

		tts = gTTS(args["TEXT"])
		tts.save(pathToFile)

		with open(pathToFile, "rb") as f:
			data = f.read()

		os.remove(pathToFile)
		cc.sendResponse(server, (data, 200))

	
	#METHODS

	@staticmethod
	def findRecordingName():
		recording = "recording"
		fileName = recording + ".wav"
		index = 0
		while os.path.exists(os.path.join(ResMan.web(), "recordings", fileName)):
			index += 1
			fileName = recording + str(index) + ".wav"

		return os.path.join(ResMan.web(), "recordings", fileName)

