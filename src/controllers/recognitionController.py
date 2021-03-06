#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import cgi
import subprocess
import platform
# recognition
import speech_recognition as sr
# speak
from gtts import gTTS

from pydub import AudioSegment

from Cheese.ErrorCodes import Error
from Cheese.Logger import Logger
from Cheese.resourceManager import ResMan
from Cheese.cheeseController import CheeseController as cc
from Cheese.httpClientErrors import *
from Cheese.httpServerError import *

from src.sessions.sessionManager import SessionManager

#@controller /recognition;
class RecognitionController(cc):

	#@post /fromWavFrontEnd;
	@staticmethod
	def fromWav(server, path, auth):
		#args = cc.readBytes(server)
		#if (not args):
		#	raise BadRequest("No bytes in request")

		ip = cc.getClientAddress(server)

		bytes = RecognitionController.deal_post_data(server)

		pathToFile = RecognitionController.saveMp3(bytes)

		text = RecognitionController.recognize(pathToFile)
		Logger.info(f"I have heard: {text}")

		answer = SessionManager.doSession(text, ip)
		Logger.info(f"I am saying: {answer}")

		if (answer == ""):
			return cc.createResponse({"ANSWER": "NO"})

		pathToFile = RecognitionController.createMp3(answer)

		return cc.createResponse({"ANSWER": pathToFile})

	#@post /fromWav;
	@staticmethod
	def fromWav(server, path, auth):
		args = cc.readBytes(server)
		if (not args):
			raise BadRequest("No bytes in request")

		ip = cc.getClientAddress(server)
		pathToFile = RecognitionController.saveMp3(args)

		text = RecognitionController.recognize(pathToFile)
		Logger.info(f"I have heard: {text}")

		answer = SessionManager.doSession(text, ip)
		Logger.info(f"I am saying: {answer}")

		if (answer == ""):
			raise InternalServerError("Karla did not hear anything")

		data = RecognitionController.createMp3(answer)

		return (data, 200, {"Content-type": "text/html"})

	#@post /toMp3;
	@staticmethod
	def toMp3(server, path, auth):
		args = cc.readArgs(server)
		cc.checkJson(["TEXT"], args)

		pathToFile = RecognitionController.findRecordingName()

		tts = gTTS(args["TEXT"])
		tts.save(pathToFile)

		with open(pathToFile, "rb") as f:
			data = f.read()

		os.remove(pathToFile)
		return (data, 200, {"Content-type": "text/html"})

	# METHODS

	@staticmethod
	def findRecordingName(reg=".wav"):
		recording = "recording"
		fileName = recording + reg
		index = 0
		while os.path.exists(ResMan.web("recordings", fileName)):
			index += 1
			fileName = recording + str(index) + reg

		return ResMan.web("recordings", fileName)

	@staticmethod
	def saveMp3(bytes):
		pathToFile = RecognitionController.findRecordingName()
		pathToFileMp3 = pathToFile.replace(".wav", ".mp3").replace("\\", "/")

		with open(pathToFileMp3, "wb") as f:
			f.write(bytes)

		if (platform.system() == "Windows"):
			command = (ResMan.resources("ffmpeg", "bin", "ffmpeg") +
						f' -i "{pathToFileMp3}" "{pathToFile}"')
			print(command)
			subprocess.call(command, shell=False)
		else:
			command = ["ffmpeg", "-i", pathToFileMp3, pathToFile]
			print(command)
			subprocess.Popen(command)
		time.sleep(0.1)
		return pathToFile

	@staticmethod
	def recognize(fileName):
		r = sr.Recognizer()

		file = sr.AudioFile(fileName)
		with file as source:
			audio = r.record(source)

		os.remove(fileName)
		os.remove(fileName.replace(".wav", ".mp3"))
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

	@staticmethod
	def deal_post_data(server):
		ctype, pdict = cgi.parse_header(server.headers['Content-Type'])
		pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
		pdict['CONTENT-LENGTH'] = int(server.headers['Content-Length'])
		if ctype == 'multipart/form-data':
			form = cgi.FieldStorage( fp=server.rfile, headers=server.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':server.headers['Content-Type'], })
			if isinstance(form["file"], list):
				for record in form["file"]:
					return record.file.read()
			else:
				return form["file"].file.read()



