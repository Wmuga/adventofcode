import re 

def solve1(inp:str): 
	res=0 
	for i in range(0,len(inp)-3):
		if len(set(inp[i:i+4]))==4:
			res+=4
			break
		res+=1
	print(f'Solution 1: {res}')  
 
def solve2(inp): 
	res=0  
	for i in range(0,len(inp)-13):
		if len(set(inp[i:i+14]))==14:
			res+=14
			break
		res+=1
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return  re.split('\r?\n',open(file).read())[0]

def main(): 
	inp = read_input(r'.\2022\6\input_test.txt')  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\6\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
