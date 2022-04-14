#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.ErrorCodes import Error
from cheese.modules.cheeseController import CheeseController as cc

from python.repositories.notificationsRepository import NotificationsRepository

from python.models.notifications import Notifications

#@controller /notifications
class NotificationsController(cc):

	#@post /create
	@staticmethod
	def create(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		args = cc.readArgs(server)

		if (not cc.validateJson(['END_TIME', 'REPEAT', 'DESCRIPTION'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		endTime = args["END_TIME"]
		repeat = args["REPEAT"]
		description = args["DESCRIPTION"]

		newId = NotificationsRepository.findNewId()
		notificationsModel = Notifications()
		notificationsModel.id = newId
		notificationsModel.end_time = endTime
		notificationsModel.repeat = repeat
		notificationsModel.description = description
		NotificationsRepository.save(notificationsModel)

		response = cc.createResponse({"ID": newId}, 200)
		cc.sendResponse(server, response)

	#@get /get
	@staticmethod
	def get(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		args = cc.getArgs(path)

		if (not cc.validateJson(['ID'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		id = args["ID"]

		notificationsModel = NotificationsRepository.find(id)
		jsonResponse = {}
		jsonResponse["NOTIFICATION"] = notificationsModel.toJson()

		response = cc.createResponse(jsonResponse, 200)
		cc.sendResponse(server, response)

	#@get /getAll
	@staticmethod
	def getAll(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		notificationsArray = NotificationsRepository.findAll()
		jsonResponse = {}
		jsonResponse["NOTIFICATIONS"] = []
		for notification in notificationsArray:
			jsonResponse["NOTIFICATIONS"].append(notification.toJson())

		response = cc.createResponse(jsonResponse, 200)
		cc.sendResponse(server, response)

	#@post /update
	@staticmethod
	def update(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		args = cc.readArgs(server)

		if (not cc.validateJson(['ID', 'END_TIME', 'REPEAT', 'DESCRIPTION'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		id = args["ID"]
		endTime = args["END_TIME"]
		repeat = args["REPEAT"]
		description = args["DESCRIPTION"]

		notificationsModel = NotificationsRepository.findById(id)
		notificationsModel.id = id
		notificationsModel.end_time = endTime
		notificationsModel.repeat = repeat
		notificationsModel.description = description
		NotificationsRepository.update(notificationsModel)

		response = cc.createResponse({'STATUS': 'notification has been updated'}, 200)
		cc.sendResponse(server, response)

	#@post /delete
	@staticmethod
	def delete(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		args = cc.readArgs(server)

		if (not cc.validateJson(['ID'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		id = args["ID"]

		notificationsModel = NotificationsRepository.findById(id)
		NotificationsRepository.delete(notificationsModel)

		response = cc.createResponse({'STATUS': 'notification has been deleted'}, 200)
		cc.sendResponse(server, response)

	#@get /getByRepeat
	@staticmethod
	def getByRepeat(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		args = cc.getArgs(path)

		if (not cc.validateJson(['REPEAT'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		repeat = args["REPEAT"]

		notificationsArray = NotificationsRepository.findBy("columnName-repeat", repeat)
		jsonResponse = {}
		jsonResponse["NOTIFICATIONS"] = []
		for notification in notificationsArray:
			jsonResponse["NOTIFICATIONS"].append(notification.toJson())

		response = cc.createResponse(jsonResponse, 200)
		cc.sendResponse(server, response)

	#@get /getByDescription
	@staticmethod
	def getByDescription(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		args = cc.getArgs(path)

		if (not cc.validateJson(['DESCRIPTION'], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		description = args["DESCRIPTION"]

		notificationsArray = NotificationsRepository.findBy("columnName-description", description)
		jsonResponse = {}
		jsonResponse["NOTIFICATIONS"] = []
		for notification in notificationsArray:
			jsonResponse["NOTIFICATIONS"].append(notification.toJson())

		response = cc.createResponse(jsonResponse, 200)
		cc.sendResponse(server, response)

	#@get /check
	@staticmethod
	def check(server, path, auth):
		if (auth["role"] > 1):
			Error.sendCustomError(server, "Unauthorized access", 401)
			return

		notifications = NotificationsRepository.findPassedNotifications()

		jsonArray = []
		for notif in notifications:
			jsonArray.append(notif.toJson())
			#NotificationsRepository.delete(notif)

		response = cc.createResponse({"NOTIFICATIONS": jsonArray}, 200)
		cc.sendResponse(server, response)

