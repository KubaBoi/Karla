#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cheese.ErrorCodes import Error
from Cheese.cheeseController import CheeseController as cc

from src.repositories.notificationsRepository import NotificationsRepository

#@controller /notifications;
class NotificationsController(cc):

	#@post /create;
	@staticmethod
	def create(server, path, auth):
		args = cc.readArgs(server)
		cc.checkJson(['END_TIME', 'REPEAT', 'DESCRIPTION'], args)

		endTime = args["END_TIME"]
		repeat = args["REPEAT"]
		description = args["DESCRIPTION"]

		notificationsModel = NotificationsRepository.model()
		notificationsModel.setAttrs(end_time=endTime, repeat=repeat, description=description)
		NotificationsRepository.save(notificationsModel)

		return cc.createResponse({"ID": notificationsModel.id})

	#@get /get;
	@staticmethod
	def get(server, path, auth):
		args = cc.getArgs(path)
		cc.checkJson(["ID"], args)

		id = args["ID"]

		notificationsModel = NotificationsRepository.find(id)
		jsonResponse = {}
		jsonResponse["NOTIFICATION"] = notificationsModel.toJson()

		return cc.createResponse(jsonResponse)

	#@get /getAll;
	@staticmethod
	def getAll(server, path, auth):
		notificationsArray = NotificationsRepository.findAll()
		jsonResponse = {}
		jsonResponse["NOTIFICATIONS"] = cc.modulesToJsonArray(notificationsArray)

		return cc.createResponse(jsonResponse)

	#@post /update;
	@staticmethod
	def update(server, path, auth):
		args = cc.readArgs(server)
		cc.checkJson(['ID', 'END_TIME', 'REPEAT', 'DESCRIPTION'], args)

		id = args["ID"]
		endTime = args["END_TIME"]
		repeat = args["REPEAT"]
		description = args["DESCRIPTION"]

		notificationsModel = NotificationsRepository.find(id)
		notificationsModel.end_time = endTime
		notificationsModel.repeat = repeat
		notificationsModel.description = description
		NotificationsRepository.update(notificationsModel)

		return cc.createResponse({'STATUS': 'notification has been updated'})

	#@post /delete;
	@staticmethod
	def delete(server, path, auth):
		args = cc.readArgs(server)
		cc.checkJson(["ID"], args)

		id = args["ID"]

		notificationsModel = NotificationsRepository.find(id)
		NotificationsRepository.delete(notificationsModel)

		return cc.createResponse({'STATUS': 'notification has been deleted'})

	#@get /getByRepeat;
	@staticmethod
	def getByRepeat(server, path, auth):
		args = cc.getArgs(path)
		cc.checkJson(["REPEAT"], args)

		repeat = args["REPEAT"]

		notificationsArray = NotificationsRepository.findBy("repeat", repeat)
		jsonResponse = {}
		jsonResponse["NOTIFICATIONS"] = cc.modulesToJsonArray(notificationsArray)

		return cc.createResponse(jsonResponse)

	#@get /getByDescription;
	@staticmethod
	def getByDescription(server, path, auth):
		args = cc.getArgs(path)
		cc.checkJson(["DESCRIPTION"], args)

		description = args["DESCRIPTION"]

		notificationsArray = NotificationsRepository.findBy("description", description)
		jsonResponse = {}
		jsonResponse["NOTIFICATIONS"] = cc.modulesToJsonArray(notificationsArray)

		return cc.createResponse(jsonResponse)

	#@get /check;
	@staticmethod
	def check(server, path, auth):
		notifications = NotificationsRepository.findPassedNotifications()

		jsonArray = []
		for notif in notifications:
			jsonArray.append(notif.toJson())
			NotificationsRepository.delete(notif)

		return cc.createResponse({"NOTIFICATIONS": jsonArray})
		

