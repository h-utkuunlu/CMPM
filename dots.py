"""
Author: Halil Utku Unlu & Stefan Niehaus
"""

import pygame
screen = pygame.display.set_mode((56*10, 31*10 + 20)) 

class Dots:
	
	def __init__(self):
	
	#dots
	self.color = (255, 255, 0)
	self.screen = screen
	pygame.draw.circle(screen, color, center, radius)
		
	def 
