import re 

def solve1(inp:list[list[int]]): 
	res=0  
	for line in inp:
		if (line[2]>=line[0] and line[3]<=line[1]) or (line[2]<=line[0] and line[3]>=line[1]): res+=1
	print(f'Solution 1: {res}')  
 
def solve2(inp:list[list[int]]): 
	res=0  
	for line in inp:
		if (line[0]<=line[2] and line[1]>=line[2]) or (line[0]<=line[3] and line[1]>=line[3]) \
		or (line[2]<=line[0] and line[3]>=line[0]) or (line[2]<=line[1] and line[3]>=line[1]): res+=1
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return [[int(dig) for dig in line.split(' ')] for line in re.split('\r?\n',re.sub('[,-]',' ',open(file).read()))]

def main(): 
	inp = read_input(r'.\2022\4\input_test.txt')  

	print(inp)

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\4\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
