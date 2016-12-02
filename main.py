import pygame
import pacman as pm
import monsters
import sub_board as board
from time import sleep


pygame.init()
screen = pygame.display.set_mode((56*20, 31*20 + 2*20))


maze = board.Board(screen)
dots = board.Dots(maze, screen)

pacman1 = pm.PacMan(screen, 0, maze)
pacman2 = pm.PacMan(screen, 1, maze)	

screen.fill((0, 0, 0))
play = True

while play:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
			break
            
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pacman1.change_dir(4)
  
			if event.key == pygame.K_RIGHT:
				pacman1.change_dir(6)
                
			if event.key == pygame.K_UP:
				pacman1.change_dir(8)
                
			if event.key == pygame.K_DOWN:
				pacman1.change_dir(2)
	
	screen.fill((0, 0, 0))
	
	maze.display()
	dots.display()
	
	pacman1.move(pacman1.direction)
	pacman2.move(pacman2.direction)
	
	pygame.display.update()
	
	sleep(2**-10)
