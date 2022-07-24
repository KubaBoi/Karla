#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Cheese.cheeseRepository import CheeseRepository

#@repository notifications;
#@dbscheme (id, end_time, repeat, description);
#@dbmodel Notifications;
class NotificationsRepository(CheeseRepository):

	#@query "select * from notifications where end_time <= now();";
	#@return array;
	@staticmethod
	def findPassedNotifications():
		return CheeseRepository.findPassedNotifications()


