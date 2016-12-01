from random import choice
import pygame

class PacMan:
	def __init__(self, screen, side, board = 0):
		self.screen = screen
		self.board = board
		self.side = side
		
		self.skin_main1 = pygame.image.load("skins/main1_s.png")
		self.skin_main2 = pygame.image.load("skins/main2_s.png")
		self.skin_main3 = pygame.image.load("skins/main3_s.png")
		self.skin_over1 = pygame.image.load("skins/over1_s.png")
		self.skin_over2 = pygame.image.load("skins/over2_s.png")
		self.skin_over3 = pygame.image.load("skins/over3_s.png")
		
		if self.side:
			self.direction = 6
		else:
			self.direction = 4
		self.speed = 2
		
		if self.side:
			self.pos = (screen.get_width()//4, screen.get_height()//2) # depends on the board
		else:
			self.pos = ((screen.get_width()//4)*3, screen.get_height()//2) # depends on the board
		
		self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 10)
		
	def show(self):
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		self.screen.blit(self.skin_main1, self.rect.topleft)
	
	def move(self, direction): 
		
		if direction == 4:
			opposite = 6
			self.pos = (self.pos[0] - self.speed, self.pos[1])
		elif direction == 6:
			opposite = 4
			self.pos = (self.pos[0] + self.speed, self.pos[1])
		elif direction == 8:
			opposite = 2
			self.pos = (self.pos[0], self.pos[1]  - self.speed)		
		elif direction == 2:
			opposite = 8
			self.pos = (self.pos[0], self.pos[1]  + self.speed)
		
		if self.board[self.pos[0]][self.pos[1]] == "#": #wall symbol or indicator
			self.move(opposite) # Not sure if this will work 
			
		self.show()
			
		
	def change_dir(self, direction): # 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
		self.direction = direction
