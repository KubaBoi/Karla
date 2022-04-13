#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.ErrorCodes import Error
from cheese.modules.cheeseController import CheeseController as cc

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

		response = cc.createResponse({'TEXT': 'str', 'DONE': True, 'PINDEX': 0}, 200)
		cc.sendResponse(server, response)

