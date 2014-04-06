#! /usr/bin/env python
# coding=utf8

from BotModule import BotModule
from BotCommand import BotCommand

import os, sys, random, time

class RRouletteModule(BotModule):
	def __init__(self):
		self.size = 6
		self.lastShot = 0
		self.revolver = self.reload()
		return

	def reload(self):
		rev = []
		for n in range(0, self.size):
			rev.append('empty')

		rev[random.randint(0,self.size-1)] = 'bullet'
		
		return rev

	def command(self, command):
		# let em shoot
		if command.command == '!roulette' and command.type == BotCommand.PUBLIC:
			# Reload revolver if ppl havent played in a while
			if len(self.revolver) != self.size and time.time() > self.lastShot + 60*60*2:
				self.revolver = self.reload()
				self.sendPublicMessage('Neues Glück: Trommel aus ' + str(self.size) + ' Männer-Bonbon-Fächern... Ein Bonbon ist drin und tödlich.')

			if self.revolver.pop() == 'bullet':
				line = 'Bang!! ' + command.origin + ' geht von uns wie ein echter Mann...'
				self.sendPublicMessage(line)
				self.kick(command.origin, line)
				self.revolver = self.reload()
				self.sendPublicMessage('Neues Glück: Trommel aus ' + str(self.size) + ' Männer-Bonbon-Fächern... Ein Bonbon ist drin und tödlich.')

			else:
				self.sendPublicMessage('*click* - ' + command.origin + ' ist ein Glückspilz. Nächster?')
			self.lastShot = time.time()

		return

	def help(self, nick):
		self.sendPrivateMessage(nick, '!roulette - Russisch Roulette - zeig was in dir steckt!')
		return
