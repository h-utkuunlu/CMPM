from random import choice
import pygame

class PacMan:
	def __init__(self, screen, side, board):
		self.screen = screen
		self.board = board
		self.side = side
				
		self.skin_main1 = pygame.image.load("skins/main1_s.png")
		self.skin_main2 = pygame.image.load("skins/main2_s.png")
		self.skin_main3 = pygame.image.load("skins/main3_s.png")
		self.skin_over1 = pygame.image.load("skins/over1_s.png")
		self.skin_over2 = pygame.image.load("skins/over2_s.png")
		self.skin_over3 = pygame.image.load("skins/over3_s.png")
		
		self.direction = None
		
		self.speed = 2
		
		if self.side:
			found = False
			for i_row in range(len(self.board.board)):
				for i_col in range(len(self.board.board[i_row])):
					if self.board.board[i_row][i_col] == 'p':
						start_pos = (i_col * 20, i_row * 20)
						found = True
					
					if found:
						break
				if found:
					break
			self.pos = start_pos # depends on the board
			
		else:
			found = False
			for i_row in range(len(self.board.board)):
				for i_col in range(len(self.board.board[i_row])):
					if self.board.board[i_row][i_col] == 'q':
						start_pos = (i_col * 20, i_row * 20)
						found = True
					
					if found:
						break
				if found:
					break
			self.pos = start_pos # depends on the board
		
		self.rect = pygame.Rect(self.pos[0], self.pos[1], 20, 20)
		
	def show(self):
		
		pygame.draw.rect(self.screen, (50, 50, 50), self.rect)
		self.screen.blit(self.skin_main1, self.rect.topleft)
		pygame.display.update()
		
	def move(self, direction): 
		
		#print(self.rect.topleft)
		
		if direction == 4:
			opposite = 6
			self.rect.topleft = (self.rect.topleft[0] - self.speed, self.rect.topleft[1])
		elif direction == 6:
			opposite = 4
			self.rect.topleft = (self.rect.topleft[0] + self.speed, self.rect.topleft[1])
		elif direction == 8:
			opposite = 2
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]  - self.speed)		
		elif direction == 2:
			opposite = 8
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]  + self.speed)
		else:
			pass
		#print(self.pos)
		
		if self.rect.collidelist(self.board.wall_lst) != -1: #wall symbol or indicator
			self.move(opposite) # Not sure if this will work 
		
		self.show()
			
		
	def change_dir(self, direction): # 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
		self.direction = direction
