"""
Author: Halil Utku Unlu & Stefan Niehaus
"""

import pygame
from random import choice
		
class Board:
	"""
	The function converts an existing csv file into a board that is useful in the game
	"""
	def __init__(self, screen):
	
		self.screen = screen
		self.color = (0, 0, 255)
		
		#Making the board
		fp = open('board.csv')
		board = []
		for line in fp:
			row = line.strip().split(',')
			board.append(row)
		self.board = board
		fp.close()
		
		#Making the walls from the board
		self.wall_lst = []
		self.interior_lst = []
		
		for i_row in range(len(self.board)):
			for i_col in range(len(self.board[i_row])):
				if self.board[i_row][i_col] == '#':
					wall = pygame.Rect(20*(i_col), 20*(i_row), 20, 20)
					inside = pygame.Rect(20*(i_col) + 1 , 20*(i_row) + 1, 18, 18)
					
					#wall_lst will be used to identify collisions
					self.wall_lst.append(wall)
					self.interior_lst.append(inside)	
	
		self.left_power = False
		self.right_power = False
	
	def display(self):
		"""
		Function to display the board
		"""
		for wall in self.wall_lst:
			pygame.draw.rect(self.screen, self.color, wall)
			
		for inside in self.interior_lst:
			pygame.draw.rect(self.screen, (0,0,0), inside)
		
class Dots:
	"""
	Class that manages the collectible dots for each pacman
	"""
	def __init__(self, Board, screen, side):
		
		self.side = side
		self.color = (255, 255, 0)
		self.screen = screen
#		self.dots_lst_right = []
#		self.dots_lst_left = []
		self.board = Board.board
		self.dots_lst = []
		
		if self.side:
			for j_row in range(len(self.board)):
				for j_col in range(28, 28+len(self.board[j_row][28:])):
					if self.board[j_row][j_col] == '':
						dot = pygame.Rect(20*(j_col) + 9, 20*(j_row) + 9 , 2, 2)
				
						#List of all the centers of the dots
						self.dots_lst.append(dot)
		else:
		
			for i_row in range(len(self.board)):
				for i_col in range(len(self.board[i_row][:28])):
					if self.board[i_row][i_col] == '':
						dot = pygame.Rect(20*(i_col) + 9, 20*(i_row) + 9 , 2, 2)
	
						self.dots_lst.append(dot)
		
		#print("Left:", self.dots_lst_left)
		#print("Right:", self.dots_lst_right)
	
	def display(self):
		"""
		Function to display the collectible dots
		"""
		for dot in self.dots_lst:
			pygame.draw.rect(self.screen, self.color, dot)

		
class Power:
	"""
	Class that controls the power ups
	"""
	def __init__(self, board, screen):
		
		self.board = board
		self.screen = screen
		self.color = (255, 0, 0)
		
		self.right_pos_list = []
		self.left_pos_list = []
		
		for i_row in range(len(self.board)):
			for i_col in range(len(self.board[i_row][:28])):
				if self.board[i_row][i_col] == "":
					self.left_pos_list.append((i_col, i_row))
		
		for j_row in range(len(self.board)):
			for j_col in range(28, 28+len(self.board[j_row][28:])):
				if self.board[j_row][j_col] == "":  
					self.right_pos_list.append((j_col, j_row))
		
		self.length = 10 # time the effect will last
		
		#print(self.right_pos_list)
		#print(self.left_pos_list)
		
	def spawn(self, side):
		"""
		Given a side to spawn, the function determines the position of spawning
		"""
		#self.side = side
		
		if side:
			spawn_point = choice(self.right_pos_list)
		else:
			spawn_point = choice(self.left_pos_list)
		
		self.rect = pygame.Rect(spawn_point[0] * 20 + 7, spawn_point[1] * 20 + 7, 6, 6)
		
	def display(self):
		"""
		Function to display the power-up
		"""
		pygame.draw.rect(self.screen, self.color, self.rect)

