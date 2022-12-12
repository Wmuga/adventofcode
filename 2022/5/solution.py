import re 
from copy import deepcopy
def solve1(cols:list[list[str]],insts:list[list[int]]): 
	res=''  
	for inst in insts:
			for _ in range(inst[0]):
				cols[inst[2]-1].append(cols[inst[1]-1].pop())
	for col in cols:
		res += col[-1] if len(col)>0 else ''
	print(f'Solution 1: {res}')  
 
def solve2(cols:list[list[str]],insts:list[list[int]]): 
	res=''  
	for inst in insts:
			cols[inst[2]-1] += cols[inst[1]-1][-inst[0]:] 
			cols[inst[1]-1] = cols[inst[1]-1][:-inst[0]] 
	for col in cols:
		res += col[-1] if len(col)>0 else ''
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	vows = set([chr(num + ord('A')) for num in list(range(0,26))])
	inps = re.split('\r?\n\r?\n',open(file).read())
	crate_lines = []
	for inp_line in re.split('\r?\n',inps[0])[:-1]:
		line = [inp_line[i:i+4] for i in range(0, len(inp_line), 4)]
		crate_lines.append([''.join(set(col).intersection(vows)) for col in line])

	crate_columns = [[c for c in col if len(c)>0] for col in list(map(list, zip(*crate_lines)))]
	instrs = [[int(line[1]),int(line[3]),int(line[5])] for line in [line.split(' ') \
						for line in re.split('\r?\n',inps[1])]]
	return [col[::-1] for col in crate_columns], instrs

def main(): 
	cols,inst = read_input(r'.\2022\5\input_test.txt')  
	print('Test input:')
	solve1(deepcopy(cols),inst) 
	solve2(cols,inst) 
 
	cols,inst = read_input(r'.\2022\5\input.txt')  

	print('Actual input:')
	solve1(deepcopy(cols),inst) 
	solve2(cols,inst) 


if __name__ == '__main__': 
	main() 
