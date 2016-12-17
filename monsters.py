import pygame
import queue

class Monster:
	"""
	Class that maintains anything related to the monsters
	"""
	def __init__(self, board, screen, side, pacman):
		
		self.board = board
		self.screen = screen
		#self.color = choice([0, 1, 2]) #Green = 0, Blue = 1, Red = 2
		self.skin = pygame.image.load("skins/ghost.png")
		self.speed = 1
		
		self.pacman = pacman
		
		self.target_point = None
		
		if side:
			self.rect = pygame.Rect(29*20, 14*20, 20, 20)
		else:
			self.rect = pygame.Rect(27*20, 14*20, 20, 20)
		
		self.path = self.shortest_path()
		
	def display(self):
		"""
		Function to show the monsters
		"""
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		self.screen.blit(self.skin, (self.rect.topleft[0], self.rect.topleft[1]))
	
		
	# Path finding algorithm
	
	def is_empty(self, x, y):
		"""
		Controls if a given position is a valid movement for the monsters
		"""
		return self.board.board[y][x] != '#' 

	def neighbours(self, x, y):
		"""
		4-neighbourhood check for a given position to determine points to be tracked in breadth first search
		"""
		neighbourhood = []
		if self.is_empty(x+1, y):
			neighbourhood.append((x+1, y))
		if self.is_empty(x, y+1):
			neighbourhood.append((x, y+1))
		if self.is_empty(x-1, y):
			neighbourhood.append((x-1, y))
		if self.is_empty(x, y-1):
			neighbourhood.append((x, y-1))
		return neighbourhood
	
	# Breadth First Search
	def shortest_path(self):
		"""
		Determine the shortest path to the pacman position
		"""
		#print("Start path finding")
		
		start = (self.rect.topleft[0]//20, self.rect.topleft[1]//20)
		target = (self.pacman.rect.topleft[0]//20, self.pacman.rect.topleft[1]//20)
		
		#print("Start:", start, "Target:", target)
		
		x1 = start[0]
		y1 = start[1]
	
		tarx = target[0]
		tary = target[1]
	
		currentDist = 0
		distance = []
	
		for i in range(57):
			row = []
			for j in range(31):
				row.append(-1)
			distance.append(row)
	
		q = queue.Queue()
		q.put((x1, y1))
		distance[x1][y1] = 0
	
		#print(distance)
	
		while not q.empty():
			#print("There is an element")
			cur = q.get()
			x = cur[0]
			y = cur[1]
			dist = distance[x][y]
			
			if dist > currentDist:
				currentDist = dist
			
			if x == tarx and y == tary:
				result = []
				result.append((x, y))

				while dist > 0:
					for neighbour in self.neighbours(x, y):
						if distance[neighbour[0]][neighbour[1]] == dist-1:
							x = neighbour[0]
							y = neighbour[1]
							dist = distance[x][y]
							result.append((x, y))
							break
				
				#print(result)
				return result
			
			#print("Checking neighbours")
			for neighbour in self.neighbours(x, y):
				if distance[neighbour[0]][neighbour[1]] == -1:
					q.put((neighbour[0], neighbour[1]))
					distance[neighbour[0]][neighbour[1]] = dist+1
		#print(distance)
		print("No result")
		return -1
	
	# Movement
	
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
	
		# If monster is at position
		elif self.rect.topleft == (point[0]*20, point[1]*20):
			move = None
		
		return move
	
	def proceed(self):
		"""
		Given a point adjacent to the pacman's position, sequences the events required to reach to that point
		"""
		
		if not self.path:
			self.path = self.shortest_path()
		
		if not self.target_point:
			self.target_point = self.path.pop()

		direction = self.find_direction(self.target_point)
		
		if not direction:
			self.target_point = None
			return
		
		self.move(direction)
		
