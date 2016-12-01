class Pac_Man:
	def __init__(self, screen, board):
		self.screen = screen
		self.board = board
		self.side = choice([0, 1])
		self.skin_up1 = ""
		self.skin_up2 = ""
		self.skin_down1 = ""
		self.skin_down2 = ""
		self.skin_left1 = ""
		self.skin_left2 = ""
		self.skin_right1 = ""
		self.skin_right2 = ""
		
		if self.side:
			self.direction = 6
		else:
			self.direction = 4
		self.speed = 2
		
		if self.side:
			self.pos = (screen.getwidth()//4, screen.getheight()//2) # depends on the board
		else:
			self.pos = ((screen.getwidth()//4)*3, screen.getheight()//2) # depends on the board
		
	def show(self):
		#Function that places the pacman onto the board
	
	def move(self, direction): 
		if direction = 4
			opposite = 6
			self.pos = (self.pos[0] - self.speed, self.pos[1])
		elif direction = 6
			opposite = 4
			self.pos = (self.pos[0] + self.speed, self.pos[1])
		elif direction = 8
			opposite = 2
			self.pos = (self.pos[0], self.pos[1]  - self.speed)		
		elif direction = 2
			opposite = 8
			self.pos = (self.pos[0], self.pos[1]  + self.speed)
		
		if self.board[self.pos[0]][self.pos[1]] = "#": #wall symbol or indicator
			self.move(opposite) # Not sure if this will work 
			
		self.show()
			
		
	def change_dir(self, direction): # 8 = up, 2 = down, 4 = left, 6 = right (check numpad)
		self.direction = direction
