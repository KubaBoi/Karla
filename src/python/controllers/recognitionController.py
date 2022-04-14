#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import platform
#recognition
import speech_recognition as sr
#speak
from gtts import gTTS

from pydub import AudioSegment

from cheese.ErrorCodes import Error
from cheese.Logger import Logger
from cheese.resourceManager import ResMan
from cheese.modules.cheeseController import CheeseController as cc

from python.sessions.sessionManager import SessionManager

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

		ip = cc.getClientAddress(server)
		pathToFile = RecognitionController.saveMp3(args)

		text = RecognitionController.recognize(pathToFile)
		Logger.info(f"I have heard: {text}")

		answer = SessionManager.doSession(text, ip)
		Logger.info(f"I am saying: {answer}")

		if (answer == ""):
			Error.sendCustomError(server, "Karla did not hear anything", 500)
			return

		data = RecognitionController.createMp3(answer)

		cc.sendResponse(server, (data, 200))

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

	@staticmethod
	def saveMp3(bytes):
		pathToFile = RecognitionController.findRecordingName()
		pathToFileMp3 = pathToFile.replace(".wav", ".mp3").replace("\\", "/")

		with open(pathToFileMp3, "wb") as f:
			f.write(bytes)

		if (platform.system() == "Windows"):
			command = (os.path.join(ResMan.resources(), "ffmpeg", "bin", "ffmpeg") +
						f' -i "{pathToFileMp3}" "{pathToFile}"')
			print(command)
			subprocess.call(command, shell=False)
		else:
			sound = AudioSegment.from_mp3(pathToFileMp3)
			sound.export(pathToFile, format="wav")

		os.remove(pathToFileMp3)
		return pathToFile

	@staticmethod
	def recognize(fileName):
		r = sr.Recognizer()

		file = sr.AudioFile(fileName)
		with file as source:
			audio = r.record(source)

		os.remove(fileName)
		try:
			return r.recognize_google(audio).lower()
		except:
			return ""

	@staticmethod
	def createMp3(text):
		pathToFile = RecognitionController.findRecordingName().replace(".wav", ".mp3")

		
		tts = gTTS(text)
		tts.save(pathToFile)

		with open(pathToFile, "rb") as f:
			data = f.read()

		os.remove(pathToFile)
		return data

