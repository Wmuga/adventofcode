import re 
from copy import deepcopy

def solve(inp:list[list[str]]): 
	rooms = list(map(list, zip(*inp)))
	print(rooms)
	hall = ['.' for _ in range(11)]

	res = 0  
	cache = {}

	print(f'Solution: {res}')  
 
def read_input(file:str):
	return  [line for line in [[c for c in line if c in 'ABCD'] for line in re.split('\r?\n',open(file).read())] if len(line)>0]

def main(): 
	inp = read_input(r'.\2021\23\input_test.txt')  

	# print(inp)

	print('Test input:')
	solve(inp) 
	inp = inp[:1] + [list('DСBA'),list('DBAC')] + inp[1:]
	solve(inp) 
 
	inp = read_input(r'.\2021\23\input.txt')  

	print('Actual input:')
	solve(inp)
	inp = inp[:1] + [list('DСBA'),list('DBAC')] + inp[1:]
	solve(inp) 


if __name__ == '__main__': 
	main() 
