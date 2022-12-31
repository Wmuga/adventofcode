import re 
from copy import deepcopy
def simulate(field:list[list[int]], DEBUG = False):
	if DEBUG:
		file = open(r'.\2021\25\debug.log','w')
		draw_field = [[DRAW_FIELD[dot] for dot in line] for line in field]
		file.write(f'Step 0:\n')
		file.write('\n'.join([''.join(line) for line in draw_field]))
		file.write('\n\n')
	steps = 0
	changed = True
	while changed:
		changed = False
		steps += 1
		for cur in range(2):
			field1 = deepcopy(field)
			for y,line in enumerate(field):
				for x, dot in enumerate(line):
					if dot != cur:
						continue
					x1,y1 = (x+(cur+1)%2)%len(field[0]) , (y+cur)%len(field)
					
					if field[y1][x1] != -1:
						continue

					changed = True
					field1[y1][x1] = cur
					field1[y][x] = -1
			field = field1
		if DEBUG:
			draw_field = [[DRAW_FIELD[dot] for dot in line] for line in field]
			file.write(f'Step {steps}:\n')
			file.write('\n'.join([''.join(line) for line in draw_field]))
			file.write('\n\n')
	return steps

def solve1(field:list[list[int]], DEBUG = False): 
	res = simulate(field, DEBUG)  
	print(f'Solution 1: {res}')  
 
def solve2(inp): 
	res=0  
	print(f'Solution 2: {res}')  

FIELD = {'.':-1,'>':0,'v':1}
DRAW_FIELD = '>v.'

def read_input(file:str):
	return [[FIELD[dot] for dot in line] for line in re.split('\r?\n',open(file).read())]


def main(): 
	inp = read_input(r'.\2021\25\input_test.txt')  

	print('Test input:')
	solve1(inp, True) 
	solve2(inp) 
 
	inp = read_input(r'.\2021\25\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
