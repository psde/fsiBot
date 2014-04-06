#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule

import os, sys, random

# To find a needle in a haystack
def isOccuring(needle, haystack, caseInsensitive = False):
	for hay in haystack:
		if caseInsensitive:
			if needle.lower().find(hay.lower()) > -1:
				return True
		else:
			if needle.find(hay) > -1:
				return True
	return False

class DeiMuddaModule(BotModule):
	def __init__(self):
		return

	def command(self, command):
		if command.command == "!dm" or command.command == "!deimudda":
			bofile = open(os.path.abspath(os.path.dirname(sys.argv[0])) + "/deimudda", "r")

			# Fetch best of dei mudda.
			bo = []
			for line in bofile:
				if line.startswith("  *"):
					if len(args) == 0 or isOccuring(line, command.args, True):
						bo.append('"' + line[4:].replace("\n", "") + '" via http://hska.info/deimudda')
			line = ""	
			if len(bo) == 0:
				line = "Dei Mudda nicht gefunden."
			else:
				line = bo[random.randint(0, len(bo)-1)]

			command.answer(line)

	def help(self, nick):
		self.sendPrivateMessage(nick, "!deimudda/!dm [stichwort] - Dei Mudda, Junge. (http://hska.info/deimudda).")
		return
