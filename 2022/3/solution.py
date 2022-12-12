import re 

def ItemsToPrior(msg:str)->int:
	res = 0
	for c in msg:
		num = ord(c) - ord('A')+1
		if num > 26:
			num+=ord('A')-ord('a')
			res += num
		else:
			res += num + 26
	return res

def solve1(inp:list[str]): 
	res=0  
	for rucksack in inp:
		middle = int(len(rucksack)/2)
		s1 = set(rucksack[:middle])
		s2 = set(rucksack[middle:])
		res += ItemsToPrior(''.join(s1.intersection(s2)))
	print(f'Solution 1: {res}')  
 
def solve2(inp:list[str]): 
	res=0  
	for i in range(0,len(inp),3):
		s1 = set(inp[i])
		s2 = set(inp[i+1])
		s3 = set(inp[i+2])
		res += ItemsToPrior(''.join(s1.intersection(s2).intersection(s3)))
	print(f'Solution 2: {res}')  
 
def main(): 
	inp = re.split('\r?\n',open(r'.\.\2022\3\input_test.txt','r').read())  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = re.split('\r?\n',open(r'.\.\2022\3\input.txt','r').read())  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
