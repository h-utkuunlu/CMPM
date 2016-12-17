import pygame
import pacman as pm
import monsters
import board
from time import sleep
from random import choice, randint

pygame.init()
screen = pygame.display.set_mode((57*20, 31*20 + 2*20))
big_font = pygame.font.Font(None, 40)

def monster_spawn(side):
	"""
	Spawns a monster at the specified side of the board
	"""
	
	if side:
		monster = monsters.Monster(maze, screen, 1, pacman1)
		right_monsters.append(monster)
	else:
		monster = monsters.Monster(maze, screen, 0, pacman0)
		left_monsters.append(monster)

def endgame(pacman):
	"""
	Function to take care of the end game sequence of events
	"""
	skin_list = pacman.skin_over
	direction = pacman.dir
	
	pacman.screen.fill((0, 0, 0))
	
	for skin in skin_list:
		if pacman.dir == "up":
			#print("Showing")
			skin_blit = pygame.transform.rotate(skin, 90)
		
		elif pacman.dir == "down":	
			skin_blit = pygame.transform.rotate(skin, -90)
	
		elif pacman.dir == "left":
			skin_blit = pygame.transform.rotate(skin, 180)
	
		elif pacman.dir == "right":
			skin_blit = skin
			
		pacman.screen.blit(skin_blit, (pacman.rect.topleft[0], pacman.rect.topleft[1]))
		pygame.display.update()
		sleep(1)
		pygame.draw.rect(pacman.screen, (0, 0, 0), pacman.rect)
	
	if pacman.side:
		gg = big_font.render("Game Over. Player on the right lost", True, (255, 255, 255))
	else:
		gg = big_font.render("Game Over. Player on the left lost", True, (255, 255, 255))
	
	screen.blit(gg, (350, 200))
	pygame.display.update()
	sleep(2)



#Create maze

maze = board.Board(screen)

#Create collectible dots

right_dots = board.Dots(maze, screen, 1)
left_dots = board.Dots(maze, screen, 0)

#Create players

pacman0 = pm.PacMan(screen, 0, maze)
pacman1 = pm.PacMan(screen, 1, maze)	

#Variable set up

power_up_l = None
power_up_r = None
left_monsters = []
right_monsters = []
play = True
loser = None
power_up_timer = 500

# Start screen
screen.fill((0, 0, 0))

start = big_font.render("Competitive Multiplayer PAC MAN", True, (255, 255, 255))
start2 = big_font.render("Starts in...", True, (255, 255, 255))

screen.blit(start, (300, 200))
screen.blit(start2, (300, 250))
pygame.display.update()
sleep(1)

screen.blit(big_font.render("3", True, (255, 255, 255)), (550, 300))
pygame.display.update()
sleep(1)

screen.fill((0, 0, 0))
screen.blit(big_font.render("2", True, (255, 255, 255)), (550, 200))
pygame.display.update()
sleep(1)

screen.fill((0, 0, 0))
screen.blit(big_font.render("1", True, (255, 255, 255)), (550, 200))
pygame.display.update()
sleep(1)

screen.fill((0, 0, 0))
#Main

while play:
	
	#Controls
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
			break
            
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pacman1.change_dir("left")
  
			if event.key == pygame.K_RIGHT:
				pacman1.change_dir("right")
                
			if event.key == pygame.K_UP:
				pacman1.change_dir("up")
                
			if event.key == pygame.K_DOWN:
				pacman1.change_dir("down")
	
			if event.key == pygame.K_a:
				pacman0.change_dir("left")
  
			if event.key == pygame.K_d:
				pacman0.change_dir("right")
                
			if event.key == pygame.K_w:
				pacman0.change_dir("up")
                
			if event.key == pygame.K_s:
				pacman0.change_dir("down")
	
	screen.fill((0, 0, 0))
	
	maze.display()
	
	#Check if the collectible dots are present. If there is none, change the variable to None for further use
	
	if right_dots:
		right_dots.display()
		if not right_dots.dots_lst:
			right_dots = None
	
	if left_dots:
		left_dots.display()
		if not left_dots.dots_lst:
			left_dots = None

	pacman0.show()
	pacman1.show()
	
	#Randomized monster creator. Upper limit of the random integer determines the likelihood of a monster spawning	
	
	selector = randint(0, 500)

	if selector == 1:
		if len(left_monsters) > len(right_monsters):
			monster_spawn(1)
	
		elif len(left_monsters) < len(right_monsters):
			monster_spawn(0)

		else:
			monster_spawn(choice([0,1]))
	
	#Display monsters if there are any
	
	for monster in left_monsters:
		monster.display()
		monster.proceed()
	
	for monster in right_monsters:
		monster.display()
		monster.proceed()
	
	#Power up display and check
	
	if power_up_l:
		power_up_l.display()
		if pacman0.rect.colliderect(power_up_l):
			pacman0.power = True
			power_up_l = None
			pacman0.power_time = power_up_timer
				
	if power_up_r:
		power_up_r.display()
		if pacman1.rect.colliderect(power_up_r):
			pacman1.power = True
			power_up_r = None
			pacman1.power_time = power_up_timer
	
	# Proceed with the game
	
	pacman0.proceed()
	pacman1.proceed()
	
	# Check if the monsters caught any of the players
	
	if left_monsters and not pacman0.power:	
		monster_catch = pacman0.rect.collidelist(left_monsters)
		
		if monster_catch != -1:
			loser = pacman0
			play = False
	
	if right_monsters and not pacman1.power:
		monster_catch = pacman1.rect.collidelist(right_monsters)
		
		if monster_catch != -1:
			loser = pacman1
			play = False
	
	# Check if the pacman is collecting the dots
			
	if left_dots:
		contact_dot1= pacman0.rect.collidelist(left_dots.dots_lst)
	
		if contact_dot1 != -1:
			#print("Collision: Pacman 1", contact_dot1)
			left_dots.dots_lst.remove(left_dots.dots_lst[contact_dot1])
	
	if right_dots:
		contact_dot2= pacman1.rect.collidelist(right_dots.dots_lst)
	
		if contact_dot2 != -1:
			#print("Collision: Pacman 2", contact_dot2)
			right_dots.dots_lst.remove(right_dots.dots_lst[contact_dot2])
	
	# Check for the spawning of power-up and controlling if the time expired or not
		
	if not left_dots and not power_up_l and not pacman0.power:
		#print("Pacman 1 finished the dots")
		power_up_l = board.Power(maze.board, screen)
		power_up_l.spawn(0)
		
	if not right_dots and not power_up_r and not pacman1.power:
		#print("Pacman 2 finished the dots")
		power_up_r = board.Power(maze.board, screen)
		power_up_r.spawn(1)
	
	# Power up controls and monster-eating checks
	
	if pacman0.power_time:
		pacman0.power_time -= 1

		if left_monsters:
			eaten_monster = pacman0.rect.collidelist(left_monsters)
		
			if eaten_monster != -1:
				left_monsters.remove(left_monsters[eaten_monster])
				monster_spawn(1)
		
	elif not left_dots and not power_up_l and not pacman0.power_time:
		pacman0.power = False
		left_dots = board.Dots(maze, screen, 0)
	
	if pacman1.power_time:
		pacman1.power_time -= 1
		#print("Remaining:", pacman1.power_time)
		
		if right_monsters:
			eaten_monster = pacman1.rect.collidelist(right_monsters)
		
			if eaten_monster != -1:
				right_monsters.remove(right_monsters[eaten_monster])
				monster_spawn(0)
		
	elif not right_dots and not power_up_r and not pacman1.power_time:
		pacman1.power = False
		right_dots = board.Dots(maze, screen, 1)
	
	pygame.display.update()
	sleep(2**-8)

# Game over adjustments

endgame(loser)

	
