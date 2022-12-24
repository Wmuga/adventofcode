import re 
from functools import reduce
from copy import deepcopy
def solve1(elves:dict[set[int]], rounds = 10, DEBUG = False): 
	deb = None
	res=0
	ymin,ymax = reduce(lambda a,b:(min(a[0],b),max(a[1],b)),elves.keys(),(10000,0))
	xmin,xmax = reduce(lambda a,b:(min(a[0],b[0]),max(a[1],b[1])) , [reduce(lambda a,b:(min(a[0],b),max(a[1],b)),elves[key],(10000,0)) for key in elves.keys()],(10000,0))
	prior = 0

	if DEBUG:
		deb = open(r'.\2022\23\debug.log','w')
	
	for _ in range(rounds):
		movement = []
		for y in elves.keys():
			for x in elves[y]:
				
				counts = 0
				for x1 in range(x-1,x+2):
					for y1 in range(y-1,y+2):
						if (y1 in elves) and (x1 in elves[y1]):
							counts += 1
				if counts == 1:
					continue
				
				prior1 = prior

				for pr in range(4):
					can_move = True
					if   prior1 == 0:
					# North
						if (y - 1) in elves:
							for x1 in range(x-1,x+2):
								if x1 in elves[y-1]:
									can_move = False
									break
						if can_move:
							movement.append(((x,y),(x,y-1)))
					elif prior1 == 1:
					# South
						if (y + 1) in elves:
							for x1 in range(x-1,x+2):
								if x1 in elves[y+1]:
									can_move = False
									break
						if can_move:
							movement.append(((x,y),(x,y+1)))
					elif prior1 == 2:
					# West
						for y1 in range(y-1,y+2):
							if y1 in elves and ((x - 1) in elves[y1]):
								can_move = False
								break
						if can_move:
							movement.append(((x,y),(x-1,y)))
					else:
						# East
						for y1 in range(y-1,y+2):
							if y1 in elves and ((x + 1) in elves[y1]):
								can_move = False
								break
						if can_move:
							movement.append(((x,y),(x+1,y)))
					
					prior1 = (prior1 + 1) % 4
					if can_move:
						break
					
		i = 0
		while i < len(movement):
			start_pos, end_pos = movement[i]
			x,y = end_pos
			i1 = i + 1
			skip = False
			while i1 < len(movement):
				if movement[i1][1] == end_pos:
					movement.pop(i1)
					movement.pop(i)
					skip = True
					break
				i1+=1
			if skip:
				continue
			i += 1
			if not (y in elves):
				elves[y] = set()
			elves[y].add(x)
			x,y = start_pos
			elves[y].remove(x)
			if len(elves[y]) == 0:
				elves.pop(y, None)

		ymin,ymax = reduce(lambda a,b:(min(a[0],b),max(a[1],b)),elves.keys(),(10000,0))
		xmin,xmax = reduce(lambda a,b:(min(a[0],b[0]),max(a[1],b[1])) , [reduce(lambda a,b:(min(a[0],b),max(a[1],b)),elves[key],(10000,0)) for key in elves.keys()],(10000,0))
		prior = (prior + 1) % 4
		
		if DEBUG:
			for y in range(ymin,ymax+1):
				line = list('.'*(xmax-xmin+1))
				if y in elves:
					for x in elves[y]:
						line[x-xmin] = '#'
				deb.write(f'.{"".join(line)}.\n')
			deb.write('\n')

	res = (ymax-ymin+1)*(xmax-xmin+1)
	for y in range(ymin,ymax+1):
		if y in elves:
			res -= len(set(range(xmin,xmax+1)).intersection(elves[y]))
	
	if DEBUG:
		deb.close()

	print(f'Solution 1: {res}')  
 
def solve2(elves): 
	res=0
	prior = 0
	
	moved = True
	while moved:
		moved = False
		movement = []
		for y in elves.keys():
			for x in elves[y]:
				
				counts = 0
				for x1 in range(x-1,x+2):
					for y1 in range(y-1,y+2):
						if (y1 in elves) and (x1 in elves[y1]):
							counts += 1
				if counts == 1:
					continue
				
				moved = True
				prior1 = prior

				for pr in range(4):
					can_move = True
					if   prior1 == 0:
					# North
						if (y - 1) in elves:
							for x1 in range(x-1,x+2):
								if x1 in elves[y-1]:
									can_move = False
									break
						if can_move:
							movement.append(((x,y),(x,y-1)))
					elif prior1 == 1:
					# South
						if (y + 1) in elves:
							for x1 in range(x-1,x+2):
								if x1 in elves[y+1]:
									can_move = False
									break
						if can_move:
							movement.append(((x,y),(x,y+1)))
					elif prior1 == 2:
					# West
						for y1 in range(y-1,y+2):
							if y1 in elves and ((x - 1) in elves[y1]):
								can_move = False
								break
						if can_move:
							movement.append(((x,y),(x-1,y)))
					else:
						# East
						for y1 in range(y-1,y+2):
							if y1 in elves and ((x + 1) in elves[y1]):
								can_move = False
								break
						if can_move:
							movement.append(((x,y),(x+1,y)))
					
					prior1 = (prior1 + 1) % 4
					if can_move:
						break
					
		i = 0
		while i < len(movement):
			start_pos, end_pos = movement[i]
			x,y = end_pos
			i1 = i + 1
			skip = False
			while i1 < len(movement):
				if movement[i1][1] == end_pos:
					movement.pop(i1)
					movement.pop(i)
					skip = True
					break
				i1+=1
			if skip:
				continue
			i += 1
			if not (y in elves):
				elves[y] = set()
			elves[y].add(x)
			x,y = start_pos
			elves[y].remove(x)
			if len(elves[y]) == 0:
				elves.pop(y, None)

		prior = (prior + 1) % 4
		res += 1

	print(f'Solution 2: {res}')  
 
def read_input(file:str)->dict[set[int]]:
	elves:dict[set[int]] = dict()
	for y,line in enumerate(re.split('\r?\n',open(file).read())):
		for x, sim in enumerate(line):
			if sim == '#':
				if not (y in elves):
					elves[y] = set()
				elves[y].add(x)
	return elves

def main(): 
	inp = read_input(r'.\2022\23\input_test.txt')  

	print('Test input:')
	solve1(deepcopy(inp), DEBUG = True) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\23\input.txt')  

	print('Actual input:')
	solve1(deepcopy(inp))
	solve2(inp) 


if __name__ == '__main__': 
	main() 
