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

		if (not cc.validateJson(['TEXT', 'PINDEX'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		text = args["TEXT"]
		pindex = args["PINDEX"]

		answer, done = SessionManager.doSession(text, pindex)

		response = cc.createResponse({'TEXT': answer, 'DONE': done, 'PINDEX': pindex}, 200)
		cc.sendResponse(server, response)

