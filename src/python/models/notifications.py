#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseModel import CheeseModel

#@model
class Notifications(CheeseModel):
	def __init__(self, id=None, end_time=None, repeat=None, description=None):
		self.id=id
		self.end_time=end_time
		self.repeat=repeat
		self.description=description

	def toJson(self):
		return {
			"ID": self.id,
			"END_TIME": self.end_time,
			"REPEAT": self.repeat,
			"DESCRIPTION": self.description
		}

	def toModel(self, json):
		self.id = json["ID"]
		self.end_time = json["END_TIME"]
		self.repeat = json["REPEAT"]
		self.description = json["DESCRIPTION"]
