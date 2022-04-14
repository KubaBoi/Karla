#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.ErrorCodes import Error
from cheese.modules.cheeseController import CheeseController as cc

from python.sessions.sessionManager import SessionManager

#@controller /understand
class UnderstandController(cc):

	#@post /text
	@staticmethod
	def text(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 400)
			return

		args = cc.readArgs(server)

		if (not cc.validateJson(['TEXT'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		text = args["TEXT"]
		clientIp = cc.getClientAddress(server)

		answer = SessionManager.doSession(text, clientIp)

		response = cc.createResponse({'TEXT': answer}, 200)
		cc.sendResponse(server, response)

