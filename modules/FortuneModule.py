#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule

import os, sys, random, commands

class FortuneModule(BotModule):
	def __init__(self):
		return

	def command(self, command):
		if command.command == "!fortune":
			fargs = "-s"
			if len(command.args) >= 1:
				if command.args[0] == "bofh":
					fargs = "bofh-excuses"
				if command.args[0] == "offensive":
					fargs = "-s -o"

			output = commands.getoutput("fortune " + fargs).replace("\n", " ").replace("\t", " ")

			command.answer(output)

	def help(self, nick):
		self.sendPrivateMessage(nick, "!fortune - Glückskeks und so.")
		return
