#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule

import os, sys, re

class LinkModule(BotModule):
	def __init__(self):
		return

	def command(self, command):
		if command.command == "!l" or command.command == "!link":

			# Open wikipage containing links
			links = open(os.path.abspath(os.path.dirname(sys.argv[0])) + "/links", "r")

			if len(command.args) == 0:
				reg = re.compile('\^\W*([^\|]*)\W*\|\W*([^\|]*?)\|', re.IGNORECASE)
				self.sendPrivateMessage(command.origin, 'Folgende URLs sind bekannt und können per !link <name> gepostet werden:')
				# Just output all known links
				for line in links:
					link = reg.match(line)
					if link:
						self.sendPrivateMessage(command.origin, link.group(1) + ': ' + link.group(2))

			else:
				reg = re.compile('\^\W*(.*' + re.escape(command.args[0]) + '.*)\W*\|\W*([^\|]*?)\|', re.IGNORECASE)
				# Fetch entry in table
				matches = []
				for line in links:
					match = reg.match(line)
					if match:
						matches.append(match)
				if len(matches) > 1:
					res = "Folgende Links gefunden:"
					for i in matches:
						res += " " + i.group(1)
					command.answer(res)
				elif len(matches) == 1:
					command.answer(matches[0].group(2))
				else:
					command.answer("Kein Ergebnis für " + command.args[0])

	def help(self, nick):
		self.sendPrivateMessage(nick, "!link/!l [link label/Suchbegriff] - Gibt eine bestimmte URL aus. (http://hska.info/links).")
		return
