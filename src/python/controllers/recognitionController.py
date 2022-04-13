#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.ErrorCodes import Error
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


		response = cc.createResponse({'TEXT': 'str'}, 200)
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


		response = cc.createResponse({'TEXT': 'str'}, 200)
		cc.sendResponse(server, response)

