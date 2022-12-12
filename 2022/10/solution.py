import re 
from typing import Callable

def base_sol(inp:list[int], tick:Callable[[int,int], int]):
	x = 1
	for i,add in enumerate(inp, start=1):
		
		if (tick):
			tick(x,i)
		
		x += add

def solve1(inp:list[list[str]]): 
	stages = [20, 60, 100, 140, 180, 220]
	st = [0]

	def tick(x:int,cycle:int)->int:
		if cycle in stages:
			st[0] += x * cycle

	base_sol(inp, tick)
	
	print(f'Solution 1: {st[0]}')  
 
def solve2(inp:list[list[str]]):   
	print(f'Solution 2:')  
	rows = [[' ' for _ in range(40)] for _ in range(6)]

	def tick(x:int, cycle:int):
		pos = (cycle - 1) % 40 
		row = (cycle - 1) // 40		
		rows[row][pos] = '#' if -1 <= x - pos <= 1 else ' '
	
	base_sol(inp, tick)
	print('\n'.join([''.join(row) for row in rows]))


 
def read_input(file:str):
	inp = sum([*[[0] if line[0] == 'noop' else [0, int(line[1])] for line in [line.split(' ') for line in re.split('\r?\n',open(file).read())]]],[])
	return inp if len(inp) >= 240 else inp + [0 for _ in range(240-len(inp))]



def main(): 
	inp = read_input(r'.\2022\10\input_test.txt')  
	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\10\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
