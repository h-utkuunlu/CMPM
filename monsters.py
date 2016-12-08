from random import choice

class Monster:

	def __init__(self, board, screen):
		self.board = board
		self.screen = screen
		self.color = choice([0, 1, 2]) #Green = 0, Blue = 1, Red = 2
		
		
	def iseaten(self):
		pre_side = [0, 1].remove(self.side)
		self.board = pre_side[0]
		
	def spawn(self):
		self.side = choice([0, 1])
		
		if self.side:
			self.pos = (510, 200) # Will depend on the actual board size
		#else:
			
	def show(self):
		
		pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
		self.screen.blit(skin, (self.rect.topleft[0], self.rect.topleft[1]))
