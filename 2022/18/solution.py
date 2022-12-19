import re
from itertools import product
from functools import reduce
from queue import Queue
from matplotlib import pyplot as plt

DEBUG = False

def solve1(inp:list[tuple[int,int,int]]): 
	res = 0 
	field = [[[0 for _ in range(20)] for _ in range(20)] for _ in range(20)]
	for x,y,z in inp:
		field[x][y][z] = 1

	for x,y,z in product(range(20),range(20),range(20)):
		if field[x][y][z] == 1:
			res += 6
			neighbours = [(x1,y1,z1) for x1,y1,z1 in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1),] if 0<=x1<20 and 0<=y1<20 and 0<=z1<20]
			for x1,y1,z1 in neighbours:
				if field[x1][y1][z1] == 1:
					res-=1
				
	print(f'Solution 1: {res}')  
	return res
 
def solve2(inp:list[tuple[int,int,int]], all:int): 
	ins=0  
	field = [[[0 for _ in range(20)] for _ in range(20)] for _ in range(20)]
	for x0,y0,z0 in inp:
		field[x0][y0][z0] = 1

	minx,miny,minz = reduce(lambda a,b: (min(a[0],b[0]),min(a[1],b[1]),min(a[2],b[2])), inp, (20,20,20))
	maxx,maxy,maxz = reduce(lambda a,b: (max(a[0],b[0]),max(a[1],b[1]),max(a[2],b[2])), inp, (0,0,0))

	for x0,y0,z0 in product(range(minx,maxx),range(miny,maxy),range(minz,maxz)):
		ins_temp = 0
		frontier = Queue()
		painted = set()
		visited = []
		
		if field[x0][y0][z0] == 0:
			frontier.put((x0,y0,z0))
			field[x0][y0][z0] = 2
			visited.append((x0,y0,z0))

			while not frontier.empty():
				x,y,z = frontier.get()
				
				if not (minx<x<maxx and miny<y<maxy and minz<z<maxz):
					ins_temp = 0
					painted = set()
					for x1, y1, z1 in visited:
						field[x1][y1][z1] = 0
					break

				neighbours = [(x1,y1,z1) for x1,y1,z1 in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]]
				for x1,y1,z1 in neighbours:
					if not (minx<=x1<=maxx and miny<=y1<=maxy and minz<=z1<=maxz):
						ins_temp = 0
						painted = set()
						for x2, y2, z2 in visited:
							field[x2][y2][z2] = 0
						visited = []
						break

					if field[x1][y1][z1] == 0:
						frontier.put((x1,y1,z1))
						visited.append((x1,y1,z1))
						field[x1][y1][z1] = 2
					
					elif field[x1][y1][z1] == 1:
						ins_temp += 1
						painted.add((x,y,z))
				
				if len(visited) == 0:
					break

			if len(visited) != 0:
				for x,y,z in painted:
					field[x][y][z] = 3
				ins += ins_temp
			
			if len(painted) == 0:
				for x,y,z, in visited:
					field[x][y][z] = 0

	if DEBUG:
		for z in range(20):
			fig,plot = plt.subplots()
			for x, y in product(range(20),range(20)):
				if field[x][y][z] == 2:
					plot.scatter(x,y, color="green", marker='s')
				if field[x][y][z] == 1:
					plot.scatter(x,y, color="black", marker='s')
				if field[x][y][z] == 3:
					plot.scatter(x,y, color="blue", marker='s')
			fig.savefig(f'.\\2022\\18\\plots\\{z}.jpg')
			plt.close(fig)

	print(f'Solution 2: {all-ins}')  
 
def read_input(file:str):
	return [tuple([int(i) for i in line.split(',')]) for line in re.split('\r?\n',open(file).read())]

def main(): 
	inp = read_input(r'.\2022\18\input_test.txt')  

	print('Test input:')
	all = solve1(inp) 
	solve2(inp, all) 
 
	inp = read_input(r'.\2022\18\input.txt')  

	print('Actual input:')
	all = solve1(inp)
	solve2(inp, all) 


if __name__ == '__main__': 
	main() 
