#! /usr/bin/env python
# coding=utf8

import abc

# Baseclass of all modules, handles important stuff
class BotModule(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self):
		self.bot = None
		return

	def tick(self):
		return

	def onMessage(self, type, msg):
		return

	def setup(self, bot):
		self.bot = bot
		self.nick = bot.nick
		self.sendPrivateMessage = bot.sendPrivateMessage
		self.sendPublicMessage = bot.sendPublicMessage
		self.sendPrivateAction = bot.sendPrivateAction
		self.sendPublicAction = bot.sendPublicAction
		self.isOper = bot.isOper
		self.kick = bot.kick
		self.DEBUG = bot.DEBUG
		self.getAllUsers = bot.getAllUsers

# An example on howto write modules
class HelloWorldExample(BotModule):
	def __init__(self):
		return

	def command(self, nick, cmd, args, type):
		if cmd == "!hello":
			if type == "private":
				self.sendPrivateMessage(nick, "world!")
			else:
				self.sendPublicMessage("world!")

	def help(self, nick):
		self.sendPrivateMessage(nick, "!hello - Antwortet 'world!'")
		return
