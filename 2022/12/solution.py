import re 
from queue import PriorityQueue

def get_neighbours(cur:tuple[int,int], max:tuple[int,int]):
	n = []

	if cur[0]+1 != max[0]:
		n.append((cur[0]+1, cur[1]))
	if cur[1]+1 != max[1]:
		n.append((cur[0], cur[1]+1))
	if cur[0] != 0:
		n.append((cur[0]-1, cur[1]))
	if cur[1] != 0:
		n.append((cur[0], cur[1]-1))

	return n

def Dijkstra(start:tuple[int,int], end:tuple[int,int], map:list[list[int]]):
	nodes_from = {} # not needed
	costs = {}
	nodes_from[start] = None 
	costs[start] = 0
	paths = PriorityQueue()
	paths.put(start, 0)
	max_coord = (len(map),len(map[0]))
	
	while not paths.empty():
		cur = paths.get()

		neighbours = [n for n in get_neighbours(cur, max_coord) if map[n[0]][n[1]] - map[cur[0]][cur[1]] <= 1]

		for next in neighbours:
			new_cost = costs[cur] + 1

			if not (next in costs) or costs[next] > new_cost:
				costs[next] = new_cost
				paths.put(next, new_cost)
				nodes_from[next] = cur

	return costs[end] if end in costs else 999999 

def solve1(start:tuple[int,int], end:tuple[int,int], map:list[list[int]]):
	print(f'Solution 1: {Dijkstra(start, end, map)}')  
 
def solve2(_:tuple[int,int], end:tuple[int,int], map:list[list[int]]): 
	res = min([Dijkstra(start, end, map) for start in sum([[(i,j) for j,cur in enumerate(line) if cur==0] for i,line in enumerate(map)],[])])

	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	lines = re.split('\r?\n',open(file).read())
	start, end = [0,0], [0,0]
	for i in range(len(lines)):
		line = list(lines[i])
		for j in range(len(line)):
			sym = line[j]
			if sym == 'S':
				line[j] = 0
				start = (i,j)
			elif sym == 'E':
				line[j] = 25
				end = (i,j)
			else:
				line[j] = ord(sym) - ord('a')
		lines[i] = line
	return start, end, lines

def main(): 
	start, end, map = read_input(r'.\2022\12\input_test.txt')  

	print('Test input:')
	solve1(start, end, map) 
	solve2(start, end, map) 
 
	start, end, map = read_input(r'.\2022\12\input.txt')  

	print('Actual input:')
	solve1(start, end, map) 
	solve2(start, end, map) 


if __name__ == '__main__': 
	main() 
