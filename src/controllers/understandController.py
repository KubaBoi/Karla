
from Cheese.cheeseController import CheeseController as cc

from src.sessions.sessionManager import SessionManager

#@controller /understand;
class UnderstandController(cc):

	#@post /text;
	@staticmethod
	def text(server, path, auth):
		args = cc.readArgs(server)
		cc.checkJson(["TEXT"], args)

		text = args["TEXT"]
		clientIp = cc.getClientAddress(server)

		answer = SessionManager.doSession(text, clientIp)

		return cc.createResponse({'TEXT': answer})

