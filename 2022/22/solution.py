import re 
from functools import reduce
def solve1(field:list[str], commands:str): 
	steps = [int(i) for i in re.findall('(\d+)', commands)]
	rots = [1 if rot == 'R' else -1 for rot in re.findall('([RL])', commands)]
	# padding to steps len == rots len
	comms_length = max(len(steps),len(rots))
	steps += [0 for _ in range(comms_length - len(steps))]
	rots += [0 for _ in range(comms_length - len(rots))]
	# Movement
	pos0 = [field[0].find('.'), 0, 0]
	height = len(field)
	width = len(field[0])
	for stepCount, rotation in zip(steps,rots):
		# get current movement
		delta_x = ((pos0[2] + 1) % 2) * (1 if pos0[2] < 2 else -1)
		delta_y = ((pos0[2]) % 2) * (1 if pos0[2] < 2 else -1)
		for _ in range(stepCount):
			# try to move
			pos = [(pos0[0] + delta_x) % width, (pos0[1] + delta_y) % height, pos0[2]]
			if field[pos[1]][pos[0]] == ' ':
				# warp around
				if pos[2] == 0:
					pos[0] = 0
					while field[pos[1]][pos[0]] == ' ':
						pos[0] += 1
				elif pos[2] == 2:
					pos[0] = width -1
					while field[pos[1]][pos[0]] == ' ':
						pos[0] -= 1
				elif pos[2] == 1:
					pos[1] = 0
					while field[pos[1]][pos[0]] == ' ':
						pos[1] += 1
				else:
					pos[1] = height - 1
					while field[pos[1]][pos[0]] == ' ':
						pos[1] -= 1   
			# if not stuck at wall - change position
			if field[pos[1]][pos[0]] == '#':
				break
			else:
				pos0 = pos
		# rotate	
		pos0[2] = (pos0[2] + rotation) % 4
	res = (pos0[1]+1) * 1000 + 4 * (pos0[0]+1) + pos0[2]
	# print('Coords:', pos0)
	print(f'Solution 1: {res}')  
 
def solve2(field:list[str], commands:str): 
	res=0  
	steps = [int(i) for i in re.findall('(\d+)', commands)]
	rots = [1 if rot == 'R' else -1 for rot in re.findall('([RL])', commands)]
	# padding to steps len == rots len
	comms_length = max(len(steps),len(rots))
	steps += [0 for _ in range(comms_length - len(steps))]
	rots += [0 for _ in range(comms_length - len(rots))]
	# Inital
	pos0 = [0, 0, 0, 1]
	# Zones
	zones_corners = [
		[50,0],
		[100,0],
		[50,50],
		[0,100],
		[50,100],
		[0,150]
	]
	# Movement
	for stepCount, rotation in zip(steps,rots):
		for _ in range(stepCount):
			# get current movement
			delta_x = ((pos0[2] + 1) % 2) * (1 if pos0[2] < 2 else -1)
			delta_y = ((pos0[2]) % 2) * (1 if pos0[2] < 2 else -1)
			# try to move
			pos = [pos0[0] + delta_x, pos0[1] + delta_y, pos0[2], pos0[3]]
			if not (0<=pos[0]<50 and 0<=pos[1]<50):
				if   pos[3] == 1:
					if pos[2] == 0:
						pos[3] = 2
						pos[0] = 0
					elif pos[2] == 1:
						pos[3] = 3
						pos[1] = 0
					elif pos[2] == 2:
						pos[3] = 4
						pos[1] = (-pos[1]-1) % 50
						pos[0] = 0
						pos[2] = 0
					else:
						pos[3] = 6
						pos[1] = pos[0]
						pos[0] = 0
						pos[2] = 0
				elif pos[3] == 2:
					if pos[2] == 0:
						pos[3] = 5
						pos[1] = (-pos[1]-1) % 50
						pos[0] = 49
						pos[2] = 2
					elif pos[2] == 1:
						pos[3] = 3
						pos[1] = pos[0]
						pos[0] = 49
						pos[2] = 2
					elif pos[2] == 2:
						pos[3] = 1
						pos[0] = 49
					else:
						pos[3] = 6
						pos[1] = 49
				elif pos[3] == 3:
					if pos[2] == 0:
						pos[3] = 2
						pos[0] = pos[1]
						pos[1] = 49
						pos[2] = 3
					elif pos[2] == 1:
						pos[3] = 5
						pos[1] = 0
					elif pos[2] == 2:
						pos[3] = 4
						pos[0] = pos[1]
						pos[1] = 0
						pos[2] = 1
					else:
						pos[3] = 1
						pos[1] = 49
				elif pos[3] == 4:
					if pos[2] == 0:
						pos[3] = 5
						pos[0] = 0
					elif pos[2] == 1:
						pos[3] = 6
						pos[1] = 0
					elif pos[2] == 2:
						pos[3] = 1
						pos[0] = 0
						pos[1] = (-pos[1]-1) % 50
						pos[2] = 0
					else:
						pos[3] = 3
						pos[1] = pos[0]
						pos[0] = 0
						pos[2] = 0
				elif pos[3] == 5:
					if pos[2] == 0:
						pos[3] = 2
						pos[0] = 49
						pos[1] = (-pos[1]-1) % 50
						pos[2] = 2
					elif pos[2] == 1:
						pos[3] = 6
						pos[1] = pos[0]
						pos[0] = 49
						pos[2] = 2
					elif pos[2] == 2:
						pos[3] = 4
						pos[0] = 49
					else:
						pos[3] = 3
						pos[1] = 49
				else            :
					if pos[2] == 0:
						pos[3] = 5
						pos[0] = pos[1]
						pos[1] = 49
						pos[2] = 3
					elif pos[2] == 1:
						pos[3] = 2
						pos[1] = 0
					elif pos[2] == 2:
						pos[3] = 1
						pos[0] = pos[1]
						pos[1] = 0
						pos[2] = 1
					else:
						pos[3] = 4
						pos[1] = 49
			# if not stuck at wall - change position
			x,y = pos[0] + zones_corners[pos[3]-1][0], pos[1] + zones_corners[pos[3]-1][1]
			if field[y][x] == '#':
				break
			else:
				pos0 = pos
		# rotate	
		pos0[2] = (pos0[2] + rotation) % 4
	x,y = pos0[0] + zones_corners[pos0[3]-1][0], pos0[1] + zones_corners[pos0[3]-1][1]
	res = (y+1) * 1000 + 4 * (x+1) + pos0[2]
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	field, commands =  re.split('\r?\n\r?\n',open(file).read())
	lines = re.split('\r?\n',field)
	max_length = reduce(lambda a,b: max(a,len(b)), lines, 0)
	lines = [line + ' '*(max_length-len(line))for line in lines]
	return lines, commands

def main(): 
	field, commands = read_input(r'.\2022\22\input_test.txt')  
	print('Test input:')
	solve1(field, commands) 
	# solve2(field, commands) 
 
	field, commands = read_input(r'.\2022\22\input.txt')  

	print('Actual input:')
	solve1(field, commands) 
	solve2(field, commands) 


if __name__ == '__main__': 
	main()

"""
1 right -> 2. x = 0     y = same  face = right
1 down  -> 3. x = same  y = 0     face = down
1 left  -> 4. x = 0.    y = -y.   face = right
1 up    -> 6. x = 0.    y = x     face = right

2 right -> 5. x = last. y = -y.   face = left
2 down  -> 3. x = last. y =  x.   face = left
2 left  -> 1. x = last. y = same  face = left
2 up    -> 6. x = same. y = last. face = up

3 right -> 2. x = y     y = last  face = up 
3 down  -> 5. x = same  y = 0     face = down
3 left  -> 4. x = y     y = 0     face = down
3 up    -> 1. x = same  y = last  face = up

4 right -> 5. x = 0     y = same  face = right 
4 down  -> 6. x = same  y = 0     face = down
4 left  -> 1. x = 0     y = -y    face = right
4 up    -> 3. x = 0     y = x     face = right 

5 right -> 2. x = last  y = -y    face = left
5 down  -> 6. x = last  y = x     face = left
5 left  -> 4. x = last  y = same  face = left
5 up    -> 3. x = same  y = last  face = up

6 right -> 5. x = y     y = last  face = up
6 down  -> 2. x = same  y = 0     face = down
6 left  -> 1. x = y     y = 0     face = down
6 up    -> 4. x = same  y = last  face = up
"""