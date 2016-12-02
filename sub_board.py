"""
Author: Halil Utku Unlu & Stefan Niehaus
"""

import pygame

screen = pygame.display.set_mode((56*10, 31*10 + 20)) 
fp = open('board.csv')
		
		
class Board:

	def __init__(self):
	
		self.screen = screen
		self.color = (0, 0, 255)
		
		#Making the board
		board = []
		for line in fp:
			row = line.strip().split(',')
			board.append(row)
		self.board = board
		
		
		#Making the walls from the board
		self.wall_lst = []
		self.interior_lst = []
		for i_row in range(len(self.board)):
			for i_col in range(len(self.board[i_row])):
				if self.board[i_row][i_col] == '#':
					wall = pygame.Rect(10*(i_col), 10*(i_row), 10, 10)
					inside = pygame.Rect(10*(i_col) +1 , 10*(i_row) + 1, 8, 8)
					
					#wall_lst will be used to identify collisions
					self.wall_lst.append(wall)
					self.interior_lst.append(inside)	
	
	def display(self):
		for wall in self.wall_lst:
			pygame.draw.rect(self.screen, self.color, wall)
		for inside in self.interior_lst:
			pygame.draw.rect(self.screen, (0,0,0), inside)
			

class Dots:
	
	def __init__(self, Board):
	
		self.color = (255, 255, 0)
		self.screen = screen
		self.dots_lst = []
		self.board = Board.board
		for i_row in range(len(self.board)):
				for i_col in range(len(self.board[i_row])):
					if self.board[i_row][i_col] == '':
						dots = pygame.Rect(10*(i_col) + 4, 10*(i_row) + 4 , 2, 2)
					
						#List of all the centers of the dots
						self.dots_lst.append(dots)
	
	def display(self):
		for dots in self.dots_lst:
			pygame.draw.rect(self.screen, self.color, dots)
		
		
		
maze = Board()
dots = Dots(maze)

while True:
	maze.display()
	dots.display()
	pygame.display.update()


