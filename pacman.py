from random import choice
import pygame

class PacMan:
	def __init__(self, screen, side, board):
		self.screen = screen
		self.board = board
		self.side = side
				
		skin_main1 = pygame.image.load("skins/main1_s.png")
		skin_main2 = pygame.image.load("skins/main2_s.png")
		skin_main3 = pygame.image.load("skins/main3_s.png")
		
		self.skin_main = [skin_main1, skin_main2, skin_main3, skin_main2]
		self.skin_select = 0
		
		self.skin_over1 = pygame.image.load("skins/over1_s.png")
		self.skin_over2 = pygame.image.load("skins/over2_s.png")
		self.skin_over3 = pygame.image.load("skins/over3_s.png")
		
		
		self.direction = None
		
		self.speed = 1
		
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
		
		self.rect = pygame.Rect(self.pos[0], self.pos[1], 10, 10)
		
	def show(self):
		
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		
		if self.direction == 8:
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], 90)
			
		elif self.direction == 2:	
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], -90)
		
		elif self.direction == 4:
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], 180)
		
		elif self.direction == 6 or self.direction == None:
			skin = self.skin_main[self.skin_select // 8]	
		
		self.screen.blit(skin, (self.rect.topleft[0] - 5, self.rect.topleft[1] - 5))
				
	def move(self, direction): 
		
		#print(self.skin_select)
		
		old_pos = self.rect.topleft
		
		if direction == 4: # 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
			self.rect.topleft = (self.rect.topleft[0] - self.speed, self.rect.topleft[1])
			
		elif direction == 6:
			self.rect.topleft = (self.rect.topleft[0] + self.speed, self.rect.topleft[1])
			
		elif direction == 8:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]  - self.speed)
					
		elif direction == 2:
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1]  + self.speed)
		else:
			pass
		#print(self.pos)
		
		if self.rect.collidelist(self.board.wall_lst) != -1: #wall symbol or indicator
			self.rect.topleft = old_pos
		
		if old_pos != self.rect.topleft: #Only switch skins when not colliding against a wall
			
			self.skin_select += 1
		
			if self.skin_select == 32:
				self.skin_select = 0
	
		self.show()
			
		
	def change_dir(self, direction): # 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
		self.direction = direction
