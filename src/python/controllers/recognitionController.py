#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.ErrorCodes import Error
from cheese.modules.cheeseController import CheeseController as cc

from python.repositories.recognitionRepository import RecognitionRepository

from python.models.recognition import Recognition

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

