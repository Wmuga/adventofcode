import re 

def solve1(inp:list[list[int]]): 
	res=max([sum(elf) for elf in inp])
	print(f'Solution 1: {res}')  
 
def solve2(inp:list[list[int]]): 
	res=sum(sorted([sum(elf) for elf in inp],reverse=True)[:3])
	print(f'Solution 2: {res}')  
 
def main(): 
	inp = [[int(i) for i in re.split('\r?\n', elf)] for elf in re.split('\r?\n\r?\n',open(r'.\.\2022\1\input.txt','r').read())]  
	# inp = [[int(i) for i in re.split('\r?\n', elf)] for elf in re.split('\r?\n\r?\n',open(r'.\.\2022\1\input_test.txt','r').read())]  
	
	# print(inp)

	solve1(inp) 
	solve2(inp)  


if __name__ == '__main__': 
	main() 
