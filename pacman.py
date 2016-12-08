from random import choice
import pygame
import sub_board as board
from time import sleep

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
		self.prev_direction = None
		
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
		
		self.rect = pygame.Rect(self.pos[0], self.pos[1], 20, 20)
		
	def show(self):
		
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		
		if self.direction == "up":
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], 90)
			
		elif self.direction == "down":	
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], -90)
		
		elif self.direction == "left":
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], 180)
		
		elif self.direction == "right" or self.direction == None:
			skin = self.skin_main[self.skin_select // 8]	
		
		self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				
	def move(self, direction): 
		
		pos = (self.rect.center[0] // 20, self.rect.center[1] // 20)
		old_pos = self.rect.topleft
		
		# 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
		if self.prev_direction == "up":
			go = (0, -1)
		elif self.prev_direction == "down":
			go = (0, 1)
		elif self.prev_direction == "right":
			go = (1, 0)
		elif self.prev_direction == "left":
			go = (-1, 0)
		else:
			go = 0
			
		keep_going = True
		
		if direction == "up":
			if self.prev_direction != None and self.board.board[pos[1]-1][pos[0]] == "":
				
				while keep_going:
					diff = pos[0]*20 - self.rect.topleft[0]
					if self.prev_direction == "right":
						self.rect.topleft = (self.rect.topleft[0] + go[0] * diff, self.rect.topleft[1])
					elif self.prev_direction == "left":
						self.rect.topleft = (self.rect.topleft[0] - go[0] * diff, self.rect.topleft[1])
					elif self.prev_direction == "down":
						self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + self.speed)
						break
					if self.rect.topleft[0] == pos[0]*20:
						keep_going = False
				
			else:
				self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - self.speed)
			
		elif direction == "down":
			if self.prev_direction != None and self.board.board[pos[1]+1][pos[0]] == "":
					
				while keep_going:
					diff = pos[0]*20 - self.rect.topleft[0]
					if self.prev_direction == "right":
						self.rect.topleft = (self.rect.topleft[0] + go[0] * diff, self.rect.topleft[1])
					elif self.prev_direction == "left":
						self.rect.topleft = (self.rect.topleft[0] - go[0] * diff, self.rect.topleft[1])
					elif self.prev_direction == "up":
						self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - self.speed)
						break
					if self.rect.topleft[0] == pos[0]*20:
						keep_going = False
				
			else:
				self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + self.speed)
				
		elif direction == "left":
			if self.board.board[pos[1]][pos[0]-1] == "" and self.prev_direction != None:
					
				while keep_going:
					diff = pos[1]*20 - self.rect.topleft[1]					
					if self.prev_direction == "up":
						self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - go[1] * diff)
					elif self.prev_direction == "down":
						self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + go[1] * diff)
					elif self.prev_direction == "right":
						self.rect.topleft = (self.rect.topleft[0] - self.speed, self.rect.topleft[1])
						break
						
					if self.rect.topleft[1] == pos[1]*20:
						keep_going = False
			else:
				self.rect.topleft = (self.rect.topleft[0]  - self.speed, self.rect.topleft[1])		
					
		elif direction == "right":
			if self.board.board[pos[1]][pos[0]+1] == "" and self.prev_direction != None:
					
				while keep_going:
					diff = pos[1]*20 - self.rect.topleft[1]				
					if self.prev_direction == "up":
						self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - go[1] * diff)
					elif self.prev_direction == "down":
						self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + go[1] * diff)
					elif self.prev_direction == "left":
						self.rect.topleft = (self.rect.topleft[0] + self.speed, self.rect.topleft[1])
						break
						
					if self.rect.topleft[1] == pos[1]*20:
						keep_going = False
			else:
				self.rect.topleft = (self.rect.topleft[0] + self.speed, self.rect.topleft[1])		
				
		else:	
			pass
	
		if self.rect.collidelist(self.board.wall_lst) != -1: #wall symbol or indicator
			self.rect.topleft = old_pos
		
		if old_pos != self.rect.topleft: #Only switch skins when not colliding against a wall
			
			self.skin_select += 1
		
			if self.skin_select == 32:
				self.skin_select = 0
	
		self.show()
		self.prev_direction = None
			
		
	def change_dir(self, direction): # 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
		if direction != self.direction:
			self.prev_direction = self.direction
		self.direction = direction
		#print("Prev:", self.prev_direction, "Now:", self.direction)
