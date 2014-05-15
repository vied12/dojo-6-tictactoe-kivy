#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from core import Game

class TicTacToeGameGrid(StackLayout):

	MAPPING = ["00","01","02","10","11","12","20","21","22"]
	xo_cell_0 = ObjectProperty(None)
	xo_cell_1 = ObjectProperty(None)
	xo_cell_2 = ObjectProperty(None)
	xo_cell_3 = ObjectProperty(None)
	xo_cell_4 = ObjectProperty(None)
	xo_cell_5 = ObjectProperty(None)
	xo_cell_6 = ObjectProperty(None)
	xo_cell_7 = ObjectProperty(None)
	xo_cell_8 = ObjectProperty(None)

	grid = '---------'

	def __init__(self, **kwargs):
		super(TicTacToeGameGrid, self).__init__(**kwargs)
		self.game = Game()

		self.cells = {
			0: self.xo_cell_0,
			1: self.xo_cell_1,
			2: self.xo_cell_2,
			3: self.xo_cell_3,
			4: self.xo_cell_4,
			5: self.xo_cell_5,
			6: self.xo_cell_6,
			7: self.xo_cell_7,
			8: self.xo_cell_8
		}

		self.new_game()

	def new_game(self):
		for key, btn in self.cells.items():
			btn.background_normal = 'images/blank.png'
		self.current_player = 1

	def click(self, cell_num):
		
		if self.current_player == 1:
			response = self.game.add_cross(self.MAPPING[cell_num])
			if response != False:
				self.set_symbol(cell_num, "doge%d" % (self.current_player))
				self.game.check_win()
				# computer play
				res = self.game.computer_play()
				self.set_symbol(self.MAPPING.index(str(res)), "doge2")


	def set_symbol(self, cell, symbol):
		self.cells[cell].background_normal = 'images/%s.png' % symbol.lower()

class TicTacToeApp(App):
	def build(self):
		return TicTacToeGameGrid(cols=3)

if __name__ == '__main__':
	TicTacToeApp().run()
