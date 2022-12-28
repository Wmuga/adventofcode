import re 
from math import log
def solve1(inp, DEBUG_S_10 = False): 
	num10=0 
	for line in inp:
		num = 0
		for i, dig in enumerate(line[::-1]):
			if dig == '-':
				num -= pow(5,i)
			elif dig == '=':
				num -= 2*pow(5,i)
			else:
				num += int(dig)*pow(5,i)
		if DEBUG_S_10:
			print(line, 'is' ,num)		
		num10 += num
	res = []
	power5 = pow(5,int(log(num10, 5)))
	res10 = num10

	if num10 // power5 > 2:
		res.append(0)
	
	while power5 > 0:
		num = num10//power5
		num10 = num10 % power5
		power5 = power5//5
		if num > 2:
			res[-1] += 1
			i = len(res) - 1
			while res[i] > 2:
				if i == 0:
					res = [0] + res
					i += 1
				res[i-1] += 1
				res[i] -= 5
				i -= 1
			num -= 5
		res.append(num)
	
	res = ['-' if i==-1 else ('=' if i==-2 else str(i)) for i in res]
	print(f'Solution 1: {res10} = {"".join(res)}')  
 
def solve2(inp): 
	res=0  
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return  re.split('\r?\n',open(file).read())

def main(): 
	inp = read_input(r'.\2022\25\input_test.txt')  

	print('Test input:')
	solve1(inp, False) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\25\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
