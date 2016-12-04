"""
Author: Halil Utku Unlu & Stefan Niehaus
"""

import pygame
		
class Board:

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
	
	def display(self):
	
		for wall in self.wall_lst:
			pygame.draw.rect(self.screen, self.color, wall)
			
		for inside in self.interior_lst:
			pygame.draw.rect(self.screen, (0,0,0), inside)
			

class Dots:
	
	def __init__(self, Board, screen):
	
		self.color = (255, 255, 0)
		self.screen = screen
		self.dots_lst1 = []
		self.dots_lst2 = []
		self.board = Board.board
		
		for i_row in range(len(self.board)):
				for i_col in range(len(self.board[i_row])//2):
					if self.board[i_row][i_col] == '':
						dots = pygame.Rect(20*(i_col) + 9, 20*(i_row) + 9 , 2, 2)
					
						#List of all the squares (dots) for the 1st screen
						self.dots_lst1.append(dots)
						
		for i_row in range(len(self.board)):
				for i_col in range(len(self.board[i_row])//2):
					if self.board[i_row][i_col + len(self.board[i_row])//2] == '':
						dots = pygame.Rect(20*(i_col + (len(self.board[i_row])//2)) + 9, 20*(i_row) + 9 , 2, 2)
					
						#List of all the squares (dots) for the 2nd screen
						self.dots_lst2.append(dots)
	
	def display(self):
	
		for dots in self.dots_lst1:
			pygame.draw.rect(self.screen, self.color, dots)
			
		for dots in self.dots_lst2:
			pygame.draw.rect(self.screen, self.color, dots)
		
"""			
maze = Board()
dots = Dots(maze)

while True:
	
	maze.display()
	dots.display()
	pygame.display.update()
"""

