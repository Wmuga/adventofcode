import re 
from copy import copy, deepcopy

DELTAS = [(1,0),(0,1),(-1,0),(0,-1)]
ARROWS = {1:'>',11:'v',101:'<',1001:'^'}
DIR_TO_ARR = [1,11,101,1001]

def draw(file,gen,blizs, elves,size):
	field = [[0 for _ in range(size[0])] for _ in range(size[1])]
	for x,y in elves:
		if 0<=y<size[1]:
			field[y][x] = -1
	for dir in range(4):
		for x,y in blizs[dir]:
			field[y][x] = DIR_TO_ARR[dir] if field[y][x]==0 else (field[y][x]%10 + 1)
	draw_field = [[('E' if s==-1 else (ARROWS[s] if s in ARROWS else ('.' if s == 0 else str(s)))) for s in line] for line in field]
	file.write(f'Generation {gen}:\n')
	file.write('#'*(size[0]+2)+'\n')
	for line in draw_field:
		file.write(f'#{"".join(line)}#\n')
	file.write('#'*(size[0]+2)+'\n\n')

def get_neigbours(pos,size,end_pos):
	x,y = pos
	x_max, y_max = size
	return [(x,y) for x,y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if (x,y)==end_pos or (0<=x<x_max and 0<=y<y_max)]

def cellular_automation(blizs,start_pos, end_pos,size, DEBUG = False):
	file = None
	if DEBUG:
		file = open(r'.\2022\24\debug.log','w')
	Elves = {start_pos}
	generations = 0
	while not(end_pos in Elves):
		# simulte wind
		for wind_dir in blizs:
			dx,dy = DELTAS[wind_dir]
			blizs[wind_dir] = [((x+dx) % size[0],(y+dy) % size[1]) for x,y in blizs[wind_dir]]
		# simulate elv
		Elves1 = copy(Elves)
		for elv in Elves1:
			neighbours = get_neigbours(elv,size, end_pos)
			for x,y in neighbours:
				can_move = True
				for i in range(4):
					if (x,y) in blizs[i]:
						can_move = False
						break
				if can_move:
					Elves.add((x,y))
		# kill elves in bliz
		for wind_dir in blizs:
			for x,y in blizs[wind_dir]:
				if (x, y) in Elves:
					Elves.remove((x,y))
		generations += 1
		if DEBUG:
			draw(file, generations, blizs, Elves, size)

	if DEBUG:
		file.close()

	return generations, blizs

def solve1(inp, size:tuple[int, int], DEBUG = False): 
	start_pos = (0,-1)
	end_pos = size[0]-1,size[1]
	res, _ = cellular_automation(inp, start_pos, end_pos,size, DEBUG)
	print(f'Solution 2: {res}')
 
def solve2(inp, size:tuple[int, int], DEBUG = False): 
	start_pos = (0,-1)
	end_pos = size[0]-1,size[1]
	res1, inp = cellular_automation(inp, start_pos, end_pos,size)
	if DEBUG:
		print('Trip 1:',res1)
	res2, inp = cellular_automation(inp, end_pos, start_pos,size)
	if DEBUG:
		print('Trip 2:',res2)
	res3, inp = cellular_automation(inp, start_pos, end_pos,size)
	if DEBUG:
		print('Trip 3:',res3)

	res = sum([res1,res2,res3])
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	arrows = '>v<^'
	lines = [line[1:-1] for line in re.split('\r?\n',open(file).read())[1:-1]]
	size = len(lines[0]), len(lines)
	bliz = {i:[] for i in range(4)}
	for y, line in enumerate(lines):
		for x, simb in enumerate(line):
			if simb != '.':
				bliz[arrows.find(simb)].append((x,y))
	return bliz, size


def main(): 
	bliz, size = read_input(r'.\2022\24\input_test.txt')  
	print('Test input:')
	solve1(deepcopy(bliz), size, True) 
	solve2(bliz, size, True) 
 
	bliz, size = read_input(r'.\2022\24\input.txt')  
	print('Actual input:')
	solve1(deepcopy(bliz), size) 
	solve2(bliz, size) 


if __name__ == '__main__': 
	main() 
