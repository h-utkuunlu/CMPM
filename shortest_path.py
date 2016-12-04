def is_empty(x, y):
	return maze.board[x][y] == '' or maze.board[x][y] == 'e'

def neighbours(x, y):
	result = []
	if is_empty(x+1, y):
		result.append((x+1, y))
	if is_empty(x, y+1):
		result.append((x, y+1))
	if is_empty(x-1, y):
		result.append((x-1, y))
	if is_empty(x, y-1):
		result.append((x, y-1))
	return result
	

# Breadth First Search
def shortest_path(n, x1, y1, tarx, tary):
	queuedChanges = [(x1, y1)]
	currentDist = 0
	distance = [[-1 for i in range(n)] for j in range(n)]
	q = queue.Queue()
	q.put((x1, y1))
	distance[x1][y1] = 0
	while not q.empty():
		cur = q.get()
		x = cur[0]
		y = cur[1]
		dist = distance[x][y]
		if dist > currentDist:
			currentDist = dist
			for point in queuedChanges:
				screen.blit(pygame.font.Font(None, 18).render(str(dist-1), True, (255, 255, 255)), (20*point[1]+1, 20*point[0]+1))
			pygame.display.update()
			queuedChanges = []
		if x == tarx and y == tary:
			result = []
			result.append((x, y))

			while dist > 0:
				for neighbour in neighbours(x, y):
					if distance[neighbour[0]][neighbour[1]] == dist-1:
						x = neighbour[0]
						y = neighbour[1]
						dist = distance[x][y]
						result.append((x, y))
						break
			return result
			
		#print(x, y, neighbours(x, y))
		for neighbour in neighbours(x, y):
			#print(neighbour)
			if distance[neighbour[0]][neighbour[1]] == -1:
				q.put((neighbour[0], neighbour[1]))
				distance[neighbour[0]][neighbour[1]] = dist+1
		queuedChanges.append((x, y))
#		pygame.draw.rect(screen, ((10*dist)%256, (10*dist)%256, (10*dist)%256), pygame.Rect(20*y, 20*x, 20, 20))
#		pygame.display.update()
#		sleep(0.1)
#		print(q.empty())
	return -1
	
maze.display()
pygame.display.update()

x, y = map(int, input().split())
short = shortest_path(100, 1, 1, x, y)

#for point in short:
#	pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(20*point[1], 20*point[0], 20, 20))
#pygame.display.update()
while True:
	pass
