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

		self.speed = 1
		
		self.dir = "right"
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
		
		self.rect = pygame.Rect(self.pos[0]*20, self.pos[1]*20, 20, 20)
		
		#self.point = self.set_dest()
		#self.show()
	"""
				
	

	def set_destination(self, direction = None):
		
		if not self.move_pos and not direction:
			# No directions on where to go
			# Check the current movement path
			
			self.pos = ((self.rect.topleft[0]//20), (self.rect.topleft[1]//20))
			
			if self.prev_direction == "up": # and self.board.board[self.pos[1]-1][self.pos[0]] == "":
				self.move_pos = (self.pos[0], self.pos[1] - 1)
			elif self.prev_direction == "down": # and self.board.board[self.pos[1]+1][self.pos[0]] == "":
				self.move_pos = (self.pos[0], self.pos[1] + 1)
			elif self.prev_direction == "left": # and self.board.board[self.pos[1]][self.pos[0]-1] == "":
				self.move_pos = (self.pos[0] - 1, self.pos[1]) 
			elif self.prev_direction == "right": # and self.board.board[self.pos[1]][self.pos[0]+1] == "":
				self.move_pos = (self.pos[0] + 1, self.pos[1]) 
		
		elif direction:
			#Override normal destination checks to set the direction if motion in given direction is possible
			#Determine the center position of the pacman at the moment, altering the centerpoint to correct missing corridor errors 
			
			if self.direction != direction:
				self.prev_direction = self.direction	
			self.direction = direction	
			
			if self.direction == "up":
				temp_pos = ((self.rect.topleft[0]//20), ((self.rect.topleft[1] - 8)//20))
			elif self.direction == "down":
				temp_pos = ((self.rect.topleft[0]//20), ((self.rect.topleft[1] + 8)//20))
			elif self.direction == "left":
				temp_pos = (((self.rect.topleft[0] - 8)//20), (self.rect.topleft[1]//20))
			elif self.direction == "right":
				temp_pos = ((self.rect.topleft[0] + 8)//20, (self.rect.topleft[1]//20))
			
			print(temp_pos)
			
			#Checking if the direction is clear
			if direction == "up" and self.board.board[temp_pos[1]-1][temp_pos[0]] == "":
				self.turn_pos = (temp_pos[0], temp_pos[1] - 1)
			elif direction == "down" and self.board.board[temp_pos[1]+1][temp_pos[0]] == "":
				self.turn_pos = (temp_pos[0], temp_pos[1] + 1)
			elif direction == "left" and self.board.board[temp_pos[1]][temp_pos[0]-1] == "":
				self.turn_pos = (temp_pos[0] - 1, temp_pos[1]) 
			elif direction == "right" and self.board.board[temp_pos[1]][temp_pos[0]+1] == "":
				self.turn_pos = (temp_pos[0] + 1, temp_pos[1])
	
	def find_direction(self):
		
	"""
	# Check the direction pacman is supposed to move 
	"""
		
		pos = ((self.rect.topleft[0]//20), (self.rect.topleft[1]//20))
		
		if self.move_pos:

			if (pos[0] - self.move_pos[0]) == 1: #move right
				move = "right"
			elif (pos[0] - self.move_pos[0]) == -1: #move left
				move = "left"
			elif (pos[1] - self.move_pos[1]) == 1: #move up
				move = "left"		
			elif (pos[1] - self.move_pos[1]) == -1: #move right
				move = "left"

		elif not self.move_pos and self.turn_pos:

			if (pos[0] - self.move_pos[0]) == 1: #move right
				move = "right"
			elif (pos[0] - self.move_pos[0]) == -1: #move left
				move = "left"
			elif (pos[1] - self.move_pos[1]) == 1: #move up
				move = "left"		
			elif (pos[1] - self.move_pos[1]) == -1: #move right
				move = "left"

		else:
			move = None
	
		print("Going", move)
		
		return move
	
	
	def change_dir(self, direction):
		if direction != self.direction:
			self.prev_direction = self.direction
		self.direction = direction
		
		print("Prev:", self.prev_direction, "Now:", self.direction)
	
	
	def destination_reach(self):
	"""
	# Check if pacman is in its target position
	"""
		
		curr_pos = self.rect.topleft
		
		if self.move_pos and not self.turn_pos: #Going straight
			print("Move pos:", (self.move_pos[0]*20, self.move_pos[1]*20), "Curr. pos:", curr_pos)
		
			if (self.move_pos[0]*20, self.move_pos[1] * 20) == curr_pos:
				self.move_pos = None
		
		elif not self.move_pos and self.turn_pos: #Went straight, turning
			print("Turn pos:", (self.turn_pos[0]*20, self.turn_pos[1]*20), "Curr. pos:", curr_pos)
			if (self.turn_pos[0]*20, self.turn_pos[1] * 20) == curr_pos:
				self.turn_pos = None
		
		if not self.move_pos and not self.turn_pos: #No path defined. Define a path
			print("I don't have a path")
			self.set_destination()	
	
	"""	
	
	def show(self):
		
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		
		if self.dir == "up":
			#print("Showing")
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], 90)
			
		elif self.dir == "down":	
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], -90)
			
		elif self.dir == "left":
			skin = pygame.transform.rotate(self.skin_main[self.skin_select // 8], 180)
		
		elif self.dir == "right":
			skin = self.skin_main[self.skin_select // 8]
			
					
		self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
	
	
	def move(self, direction): 

		"""
		 	#Move the pacman based on given direction, check collisions, and change skin if it is moving
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

		if self.board.board[point[1]][point[0]] == "e" or self.board.board[point[1]][point[0]] == "#":
			print("Move not allowed")
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
			print("Setting new point:", self.point)
			return		

		direction = self.find_direction(self.point)
		
		if not direction: #Pacman reached to the destination point
			self.point = self.set_dest()
			return
		
		self.move(direction)
		
		"""
		if not point: # The movement is not valid
			return
		
		#self.pos = (self.rect.topleft[0]//20, self.rect.topleft[1]//20)
		direction = self.find_direction(point)
		
		if not direction: # Pacman is at the destination. Must pick a new point
			self.point = self.set_dest()
			
		else:
			self.move(direction)
			
		"""
