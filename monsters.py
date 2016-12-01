from random import choice

class Monster:

	def __init__(self, board, screen):
		self.board = board
		self.screen = screen
		self.color = choice([  ])
		
	def iseaten(self):
		pre_side = [0, 1].remove(self.side)
		self.board = pre_side[0]
		
	def spawn(self):
		self.side = choice([0, 1])
		
		if self.side:
			self.pos = (510, 200) # Will depend on the actual board size
		#else:
			
