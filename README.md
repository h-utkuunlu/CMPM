Competitive Multiplayer PAC-MAN

Developers: Halil Utku Unlu and Stefan Niehaus

#PURPOSE:
The purpose of developing Competitive Multiplayer PAC-MAN (abreviated at CMPM) was to put a twist on the traditional Pac-Man game. 

Although the features and skins of the game remained predominantly the same with the initial game play, the board was extended to accomodate for two users and, hence, two PAC-MANs. 

The goal of an individual PAC-MAN is to "eat" all the dots on it's side of the board. Once all dots are eaten, a large red dot will spawn on the the PAC-MAN's side of the board, which, once eaten, makes it indestructible and able to eat the ghosts. Interestingly, once the ghost is eaten, the ghost does not simply disappear, but spaws on the other PAC-MAN's board (the opponent) to exact revenge. 

Therefore, eat dots and eat them fast!

#COMPONENTS:
	1) main.py
The main.py file imports components 3, 4, 5, and 6 and runs the game.

	2) board.csv
The board is defined using a CSV file, where the commas seperate individual units (i.e. the cells of the board). The "walls" are marked with "#" The starting positions of PAC-Man 1 and PAC-MAN 2 are "q" and "p", respectively.
The cells marked with "e" simply signify the spawning region of the ghosts (for organization of the board), while "s" maks their actual spawning location.

	3) board.py 
Uses the CSV file to construct the board as a list of lists.

	4) monsters.py
Contains the Monster class that includes all features of the monsters. Note that monsters do not move randomly about the board, but rather move with the path of shortest distance to the current location of the PAC-MAN they are hunting, which is only updated once the monster reaches the point that it was given once it entered the board.

	5) pacman.py
Contains the PacMan class that includes all features of the pacman.

#RUNNING THE PROGRAM:
Simply run the main.py file in the terminal once you have all the components liisted above in the same directory.

