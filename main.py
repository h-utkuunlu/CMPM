import pygame
import pacman
import monsters
from time import sleep


pygame.init()
screen = pygame.display.set_mode((1000, 400))

pacman1 = pacman.PacMan(screen, 0)
pacman2 = pacman.PacMan(screen, 1)

screen.fill((0, 0, 0))
play = True


while play:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
			break
            
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pacman1.move(4)
  
			if event.key == pygame.K_RIGHT:
				pacman1.move(6)
                
			if event.key == pygame.K_UP:
				pacman1.move(8)
                
			if event.key == pygame.K_DOWN:
				pacman1.move(2)
                
	
	pacman1.show()
	pacman2.show()
	pygame.display.update()
	sleep(2**-7)
