#!/usr/bin/env python
# Encoding: utf-8

from random import randrange
import sys

class Game(object):

	def __init__(self):
		self.rows = [
				["_","_","_"],
				["_","_","_"],
				["_","_","_"]
			]

	def add_cross(self, coord):

		row_num = int(coord[0])
		col_num = int(coord[1])

		self.display_board()

		if (self.rows[row_num][col_num] == "_"):
			self.rows[row_num][col_num] = "X"
		else:
			print "T TRO BET TU PEU PA JOUE LA"
			return False

		#COMPUTER PLAYS


	def computer_play(self):
		comp_played = 0
		while (comp_played == 0):
			comp_col = randrange(3)
			comp_row = randrange(3)

			print "COMP THINKS HARD"

			if (self.rows[comp_row][comp_col] == "_"):
				self.rows[comp_row][comp_col] = "O"
				comp_played = 1
		return "%s%s" % (comp_row, comp_col)

	def display_board(self):
		for row in self.rows:
			print row[0] + row[1] + row[2]

# 	check_win()
# 	ask_coord()

	def check_win(self):
		if (self.rows[0][0] == self.rows[0][1] and self.rows[0][1] == self.rows[0][2] and self.rows[0][2] != "_"):
			self.win(self.rows[0][0])

		elif (self.rows[1][0] == self.rows[1][1] and self.rows[1][1] == self.rows[1][2] and self.rows[1][2] != "_"):
			self.win(self.rows[1][0])

		elif (self.rows[2][0] == self.rows[2][1] and self.rows[2][1] == self.rows[2][2] and self.rows[2][2] != "_"):
			self.win(self.rows[2][0])

		elif (self.rows[0][0] == self.rows[1][0] and self.rows[1][0] == self.rows[2][0] and self.rows[2][0] != "_"):
			self.win(self.rows[0][0])

		elif (self.rows[0][1] == self.rows[1][1] and self.rows[1][1] == self.rows[2][1] and self.rows[2][1] != "_"):
			self.win(self.rows[0][1])

		elif (self.rows[0][2] == self.rows[1][2] and self.rows[1][2] == self.rows[2][2] and self.rows[2][2] != "_"):
			self.win(self.rows[0][2])

		elif (self.rows[0][0] == self.rows[1][1] and self.rows[1][1] == self.rows[2][2] and self.rows[2][2] != "_"):
			self.win(self.rows[0][0])

		elif (self.rows[0][2] == self.rows[1][1] and self.rows[1][1] == self.rows[2][0] and self.rows[2][0] != "_"):
			self.win(self.rows[0][2])

	def win(self, cell):
		if (cell == "X"):
			print "YOU WIN"
		elif (cell == "O"):
			print "YOU LOSE"
		else:
			print "BUGGER"
		sys.exit()
