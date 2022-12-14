import re 
from copy import deepcopy

def min_wt(iter:list, threshold:int):
	# iter = list(iter)
	res = max(iter)
	for item in iter:
		if item < res and item > threshold:
			res = item
	return res if res > threshold else None

def solve1(dots:dict[int,dict[int,int]]): 
	res=0  
	not_void = True
	while not_void:
		coord = (500,0)
		not_fell = True
		# moved = False
		
		while not_fell:
			# if line empty = void
			if not (coord[0] in dots):
				not_void = False
				not_fell = False
				continue
			
			# check for available ground
			test = min_wt(dots[coord[0]].keys(),coord[1])
			
			# no ground = void
			if test == None:
				not_void = False
				not_fell = False
				continue
			
			# on ground
			coord = (coord[0], test-1)

			# left line empty = slip to void
			if not (coord[0]-1 in dots):
				not_void = False
				not_fell = False
				continue
			
			# if left down is empty - go in
			if not (coord[1]+1 in dots[coord[0]-1]):
				coord = (coord[0]-1,coord[1]+1)
				continue
			
			# right line empty = void
			if not (coord[0]+1 in dots):
				not_void = False
				not_fell = False
				continue
			
			# if right down is empty = go in
			if not (coord[1]+1 in dots[coord[0]+1]):
				coord = (coord[0]+1,coord[1]+1)
				continue
			
			# else - new place
			not_fell = False
			dots[coord[0]][coord[1]] = 0
			res+=1

	print(f'Solution 1: {res}')  
 
def solve2(dots:dict[int,dict[int,int]], floor:int): 
	res=0  
	not_clogged = True
	while not_clogged:
		coord = (500,0)
		not_fell = True
		# moved = False
		
		while not_fell:
			# if line empty = floor
			if not (coord[0] in dots):
				dots[coord[0]] = {}
				dots[coord[0]][floor - 1] = 0
				res += 1
				not_fell = False
				continue
			
			# check for available ground
			test = min_wt(dots[coord[0]].keys(), coord[1])
			
			# no ground = floor
			if test == None:				
				dots[coord[0]][floor - 1] = 0
				res += 1
				not_fell = False
				continue

			# on ground		
			coord = (coord[0], test-1)

			# left line empty = slip to floor
			if not (coord[0]-1 in dots):
				dots[coord[0] - 1] = {}
				dots[coord[0] - 1][floor - 1] = 0
				res += 1
				not_fell = False
				continue
			
			# if left down is empty - go in
			if not (coord[1]+1 in dots[coord[0]-1]):
				coord = (coord[0]-1,coord[1]+1)
				continue
			
			# right line empty = floor
			if not (coord[0] + 1 in dots):
				dots[coord[0] + 1] = {}
				dots[coord[0] + 1][floor - 1] = 0
				res += 1
				not_fell = False
				continue
			
			# if right down is empty = go in
			if not (coord[1]+1 in dots[coord[0]+1]):
				coord = (coord[0]+1,coord[1]+1)
				continue
			
			# else - new place
			not_fell = False
			dots[coord[0]][coord[1]] = 0
			res+=1

			if coord[1] == 0:
				not_clogged = False 

	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	lines = [[tuple([int(coord) for coord in point.split(',')]) for point in line.split(' -> ')] for line in re.split('\r?\n',open(file).read())]
	dots = {}
	max_y = 0
	for line in lines:
		coord = line[0]
		if not (coord[0] in dots):
			dots[coord[0]] = {}
		dots[coord[0]][coord[1]] = 1
		for coord1 in line[1:]:
			dx = (coord1[0] - coord[0]) // abs((coord[0] - coord1[0])) if coord[0] != coord1[0] else 0
			dy = (coord1[1] - coord[1]) // abs((coord[1] - coord1[1])) if coord[1] != coord1[1] else 0
			while(1):
				coord = (coord[0]+dx,coord[1]+dy)
				if not (coord[0] in dots):
					dots[coord[0]] = {}
				dots[coord[0]][coord[1]] = 1

				max_y = max(max_y,coord[1])

				if coord1[0] == coord[0] and coord1[1] == coord[1]:
					break
			coord = coord1
	
	return dots, max_y+2

def main(): 
	inp, floor = read_input(r'.\.\2022\14\input_test.txt')  
	print(floor)
	print('Test input:')
	solve1(deepcopy(inp)) 
	solve2(inp, floor) 
 
	inp, floor = read_input(r'.\.\2022\14\input.txt')  

	print('Actual input:')
	solve1(deepcopy(inp)) 
	solve2(inp, floor) 


if __name__ == '__main__': 
	main() 
