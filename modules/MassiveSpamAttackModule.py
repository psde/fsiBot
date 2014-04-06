#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule

import os, sys, random

class MassiveSpamAttackModule(BotModule):
	def _init_(self):
		return

	def command(self, command):

		if command.command == "!msa":
			msg = ""
			
			if len(command.args) != 0:
				mode = command.args[0]
				users = self.getAllUsers(command.origin, mode)

				if len(users) != 0:
					for user in users:
						if len(msg) != 0:
							msg += ", "
						msg += user

					msg += ": "
					self.sendPublicMessage("Von " + command.origin + " an " + msg)
					msg = ""
					for chunk in command.args[1::1]:
						msg += chunk + " "

					self.sendPublicMessage(msg)

	def help(self, nick):
		self.sendPrivateMessage(nick, "!msa arg message - arg: all, fs. MassiveSpamAttak nur für Ops. ")
		return
