#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule
from BotCommand import BotCommand

from time import *

import os, sys, random

class BeerModule(BotModule):
	def __init__(self):
		return

	def command(self, command):
		lt = localtime()	
		if command.command == "!beer" or command.command == "!bier":
			if 6 < lt[3] < 16:
				line = "Kein Bier vor 4!"
				command.answer(line)
			else:
				schmack = random.choice(["leckeres", "wohltuendes", "wohlschmeckendes", "eisgekühltes", "lauwarmes", "abgestandenes", "schales"])
				beer = random.choice(["Tannenzäpfle", "Höpfner", "Leikeim", "Becks", "Jever", "Öttinger", "Palmbräu", "Andechser Doppelbock", "Kölsch", "Veltins"])
				
				compliment = ""
				reciever = nick
				if len(args) > 0:
					reciever = args[0]
					compliment = " Mit freundlichen Grüßen von " + nick
				line = "gibt " + reciever + " ein " + schmack + " " + beer + "." + compliment

				command.answer(line)

	def help(self, nick):
		self.sendPrivateMessage(nick, "!bier/!beer - Verteilt Bier.")
		return
