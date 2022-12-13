import re 
from ast import literal_eval
from functools import cmp_to_key

def check_pair(curL, curR)->int:
		i = 0
		while i < len(curL) and i < len(curR):
			if type(curL[i]) == int and type(curR[i]) == int:
				if curL[i] < curR[i]:
					return -1
				if curL[i] > curR[i]:
					return 1
			elif type(curL[i]) == list:
				res = check_pair(curL[i], [curR[i]] if type(curR[i]) == int else curR[i])
				if res != 0:
					return res
			elif type(curR[i]) == list:
				res = check_pair([curL[i]] if type(curL[i]) == int else curL[i],curR[i])
				if res != 0:
					return res
			i+=1
		return 0 if len(curL) == len(curR) else (-1 if len(curL) < len(curR) else 1)

def solve1(pairs:list): 
	res = []
	
	for i,pair in enumerate(zip(pairs[::2],pairs[1::2]), start=1):
		if check_pair(pair[0], pair[1]) == 1:
			res.append(i)

	print(f'Solution 1: {sum(res)}')  
 
def solve2(inp:list): 
	inp.append([[2]])
	inp.append([[6]])
	inp.sort(key=cmp_to_key(check_pair))
	ind1, ind2 = 0,0
	for i, val in enumerate(inp, start=1):
		if val == [[2]]:
			ind1 = i
		elif val == [[6]]:
			ind2 = i
	print(f'Solution 2: {ind1*ind2}')  
 
def read_input(file:str):
	return [literal_eval(line) for line in re.split('\r?\n',open(file).read()) if len(line) > 0]

def main(): 
	inp = read_input(r'.\2022\13\input_test.txt')  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\13\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
