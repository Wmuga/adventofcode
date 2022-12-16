import re
from collections import defaultdict
from functools import cache
from itertools import product
V, F, D = set(), dict(), defaultdict(lambda: 10000)

@cache
def search(time, cur='AA', pipes=frozenset(F), e=False):
		return max([F[pipe] * (time-D[cur,pipe]-1) + search(time-D[cur,pipe]-1, pipe, pipes-{pipe}, e)
					 for pipe in pipes if D[cur,pipe]<time] + [search(26, pipes=pipes) if e else 0])

def solve1(): 
	res = search(30, pipes = frozenset(F))
	print(f'Solution 1: {res}')  
 
def solve2(): 
	res = search(26, pipes = frozenset(F), e=True)  
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	lines = re.split('\r?\n',open(file).read())
	reg_name = re.compile('(?<=Valve ).{2}')
	reg_flow = re.compile('(?<=rate=)\d+')
	reg_valves = re.compile('(?<=valve[s ]).+')
	V, F, D = set(), dict(), defaultdict(lambda: 10000)
	for line in lines:
		name = reg_name.search(line).group(0)
		flow = int(reg_flow.search(line).group(0))
		valve_conn = reg_valves.search(line).group(0).strip().split(', ')
		V.add(name)
		if flow != 0:
			F[name] = flow
		for valve in valve_conn:
			D[valve, name] = 1
	
	for name1, name2, name3 in product(V, V, V):
		D[name2,name3] = min(D[name2,name3], D[name2, name1]+D[name1, name3])

	return V, F, D
 
def main(): 
	global V, F, D
	V, F, D = read_input(r'.\2022\16\input_test.txt')  

	print('Test input:')
	solve1() 
	solve2() 
 
	V, F, D = read_input(r'.\2022\16\input.txt')  

	print('Actual input:')
	solve1() 
	solve2() 


if __name__ == '__main__': 
	main() 
