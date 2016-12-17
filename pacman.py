from random import choice
import pygame
from time import sleep

class PacMan:
	"""
	Main class that stores and governs anything related to the pacmans
	"""
	def __init__(self, screen, side, board):
		self.screen = screen
		self.board = board
		self.side = side
				
		self.skin_main1 = pygame.image.load("skins/main1_s.png")
		self.skin_main2 = pygame.image.load("skins/main2_s.png")
		self.skin_main3 = pygame.image.load("skins/main3_s.png")
		
		self.skin_power1 = pygame.image.load("skins/power1_s.png")
		self.skin_power2 = pygame.image.load("skins/power2_s.png")
		self.skin_power3 = pygame.image.load("skins/power3_s.png")
		
		self.skin_over1 = pygame.image.load("skins/over1_s.png")
		self.skin_over2 = pygame.image.load("skins/over2_s.png")
		self.skin_over3 = pygame.image.load("skins/over3_s.png")
		
		self.skin_main = [self.skin_main1, self.skin_main2, self.skin_main3, self.skin_main2]
		self.skin_power = [self.skin_power1, self.skin_power2, self.skin_power3, self.skin_power2]
		self.skin_over = [self.skin_over1, self.skin_over2, self.skin_over3]
		
		self.skin_select = 0

		self.speed = 2
		self.power = False
		self.power_time = 0
		
		self.next_dir = None
		self.point = None
		
		if self.side:
			found = False
			for i_row in range(len(self.board.board)):
				for i_col in range(len(self.board.board[i_row])):
					if self.board.board[i_row][i_col] == 'p':
						start_pos = (i_col, i_row)
						found = True
					
					if found:
						break
				if found:
					break
			self.pos = start_pos # depends on the board
			self.dir = "right"	
		else:
			found = False
			for i_row in range(len(self.board.board)):
				for i_col in range(len(self.board.board[i_row])):
					if self.board.board[i_row][i_col] == 'q':
						start_pos = (i_col, i_row)
						found = True
					
					if found:
						break
				if found:
					break
			self.pos = start_pos # depends on the board
			self.dir = "left"
		self.rect = pygame.Rect(self.pos[0]*20, self.pos[1]*20, 20, 20)
		
		#self.point = self.set_dest()
		#self.show()
	
	def show(self):
		"""
		Displays the pacman with correct orientation
		"""
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
	
		if self.power:
			skin_list = self.skin_power
		else:
			skin_list = self.skin_main
	
	
		if self.dir == "up":
			#print("Showing")
			skin = pygame.transform.rotate(skin_list[self.skin_select // 8], 90)
		
		elif self.dir == "down":	
			skin = pygame.transform.rotate(skin_list[self.skin_select // 8], -90)
		
		elif self.dir == "left":
			skin = pygame.transform.rotate(skin_list[self.skin_select // 8], 180)
	
		elif self.dir == "right":
			skin = skin_list[self.skin_select // 8]
		
				
		self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
		"""
		else:
			
			skin_list = self.skin_over
		
			if self.dir == "up":
				#print("Showing")
				skin = pygame.transform.rotate(skin_list[0], 90)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				skin = pygame.transform.rotate(skin_list[1], 90)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				skin = pygame.transform.rotate(skin_list[2], 90)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				
			elif self.dir == "down":	
				
				skin = pygame.transform.rotate(skin_list[0], -90)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				skin = pygame.transform.rotate(skin_list[1], -90)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				skin = pygame.transform.rotate(skin_list[2], -90)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
			elif self.dir == "left":
				skin = pygame.transform.rotate(skin_list[0], 180)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				skin = pygame.transform.rotate(skin_list[1], 180)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				
				skin = pygame.transform.rotate(skin_list[2], 180)
				self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				skin = pygame.transform.rotate(skin_list[self.skin_select // 8], 180)
		
			elif self.dir == "right":
				self.screen.blit(skin_list[0], (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				self.screen.blit(skin_list[1], (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
				self.screen.blit(skin_list[2], (self.rect.topleft[0], self.rect.topleft[1]))
				pygame.display.update()
				sleep(2)
			"""
	def move(self, direction): 
		"""
		Moves the pacman based on given direction, check collisions, and change skin if it is moving
		"""
		
		#print(pos)
		old_pos = self.rect.topleft
		
		if direction == "up":
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] - self.speed)
			
		elif direction == "down":
			self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + self.speed)
			
		elif direction == "left":
			self.rect.topleft = (self.rect.topleft[0]  - self.speed, self.rect.topleft[1])
		
		elif direction == "right":
			self.rect.topleft = (self.rect.topleft[0] + self.speed, self.rect.topleft[1])
		
		else:	
			pass

		#print(self.pos)
		
		if self.rect.collidelist(self.board.wall_lst) != -1: #wall symbol or indicator
			self.rect.topleft = old_pos
		
		if old_pos != self.rect.topleft: #Only switch skins when not colliding against a wall
			self.skin_select += 1
		
			if self.skin_select == 32:
				self.skin_select = 0

		#self.show()
	
	def find_direction(self, point):
		"""
		Given a point, finds the direction to be taken to reach to that given adjacent point
		"""
		
		if (self.rect.topleft[0] - point[0]*20) > 0: 
			move = "left"
		elif (self.rect.topleft[0] - point[0]*20) < 0:
			move = "right"
		elif (self.rect.topleft[1] - point[1]*20) > 0:
			move = "up"
		elif (self.rect.topleft[1] - point[1]*20) < 0:
			move = "down"
	
		# If pacman is at position
		elif self.rect.topleft == (point[0]*20, point[1]*20):
			move = None
		
		return move
		
	def set_dest(self):
		"""
		Determines the course of action / sets next movement point based on the input. There is no set point when this function runs, and pacman is in an exact position
		"""
		
		self.pos = (self.rect.topleft[0]//20, self.rect.topleft[1]//20)
		
		# If a direction change occured while the program was running
		
		if self.next_dir != None:
			self.dir = self.next_dir
			self.next_dir = None
		
		if self.dir == "up":
			point = (self.pos[0], self.pos[1]-1)
		elif self.dir == "down":
			point = (self.pos[0], self.pos[1]+1)
		elif self.dir == "left":
			point = (self.pos[0] - 1, self.pos[1])
		elif self.dir == "right":
			point = (self.pos[0] + 1, self.pos[1])

		if self.board.board[point[1]][point[0]] == "s" or self.board.board[point[1]][point[0]] == "#":
			#print("Move not allowed")
			point = None
		
		return point
		
	def change_dir(self, direction):
		"""
		Based on the user input, set future direction
		"""
		
		# Do not accept double pressing
		if self.dir != direction and self.next_dir == None:
			self.next_dir = direction
		
	def proceed(self):
		"""
		Given a point adjacent to the pacman's position, sequences the events required to reach to that point
		"""
		
		
		if not self.point:
			self.point = self.set_dest()
			#print("Setting new point:", self.point)
			return		

		direction = self.find_direction(self.point)
		
		if not direction: #Pacman reached to the destination point
			self.point = self.set_dest()
			return
		
		self.move(direction)

