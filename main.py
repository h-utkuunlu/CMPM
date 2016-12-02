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
				pacman2.change_dir(4)
  
			if event.key == pygame.K_RIGHT:
				pacman2.change_dir(6)
                
			if event.key == pygame.K_UP:
				pacman2.change_dir(8)
                
			if event.key == pygame.K_DOWN:
				pacman2.change_dir(2)
	
			if event.key == pygame.K_a:
				pacman1.change_dir(4)
  
			if event.key == pygame.K_d:
				pacman1.change_dir(6)
                
			if event.key == pygame.K_w:
				pacman1.change_dir(8)
                
			if event.key == pygame.K_s:
				pacman1.change_dir(2)
	
	screen.fill((0, 0, 0))
	
	maze.display()
	dots.display()
	
	pacman1.move(pacman1.direction)
	pacman2.move(pacman2.direction)
	
	contact_dot1= pacman1.rect.collidelist(dots.dots_lst)
	
	if contact_dot1 != -1:
		dots.dots_lst.remove(dots.dots_lst[contact_dot1])
	
	contact_dot2= pacman2.rect.collidelist(dots.dots_lst)
	
	if contact_dot2 != -1:
		dots.dots_lst.remove(dots.dots_lst[contact_dot2])
	
	pygame.display.update()
	
	sleep(2**-9)
