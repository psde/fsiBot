#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule
from PastebinModuleConfig import PastebinModuleConfig

import os, sys, random, commands, MySQLdb

class PastebinModule(BotModule):
	def __init__(self):
		self.password = PastebinModuleConfig().getPassword()
		return

	def command(self, command):
		if command.command == "!paste" or command.command == "!p" :
			if len(command.args) == 0:
				output = "https://strg-c-v.hska.info"
			else:
				#output = commands.getoutput("fortune -s").replace("\n", " ").replace("\t", " ")
				conn = MySQLdb.connect(	host = "localhost",
										user = "pastebin",
										passwd = self.password,
										db = "pastebin")
				cursor = conn.cursor()
				foo = ' '.join(command.args)
				cursor.execute('SELECT pid FROM pastes WHERE name = %s ORDER BY created DESC LIMIT 1', (foo))
				row = cursor.fetchone()
				if row is not None:
					output = "https://strg-c-v.hska.info/view/" + row[0]
				else:
					output = "Kein Paste von " + foo + " gefunden."
				cursor.close()
				conn.close()
			command.answer(output)

	def help(self, nick):
		self.sendPrivateMessage(nick, "!paste [name] - Link zum letzten Post des angegeben Users oder zum Pastebin.")
		return
