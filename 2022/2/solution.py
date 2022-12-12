import re 

def solve1(inp:list[list[str, str]]): 
	res=0  

	dictRound = {
		'AX': 1 + 3, # R + R
		'BX': 1 + 0, # P + R
		'CX': 1 + 6, # S + R
		'AY': 2 + 6, # R + P
		'BY': 2 + 3, # P + P
		'CY': 2 + 0, # S + P
		'AZ': 3 + 0, # R + S
		'BZ': 3 + 6, # P + S
		'CZ': 3 + 3, # S + S
	}

	for round in inp:
		res += dictRound[''.join(round)]

	print(f'Solution 1: {res}')  
 
def solve2(inp:list[list[str, str]]): 
	res=0  

	dictRound = {
		'AX': 3 + 0, # R + L
		'BX': 1 + 0, # P + L
		'CX': 2 + 0, # S + L
		'AY': 1 + 3, # R + D
		'BY': 2 + 3, # P + D
		'CY': 3 + 3, # S + D
		'AZ': 2 + 6, # R + W
		'BZ': 3 + 6, # P + W
		'CZ': 1 + 6, # S + W
	}

	for round in inp:
		res += dictRound[''.join(round)]

	print(f'Solution 2: {res}')   
 
def main(): 
	inp = [line.split(' ') for line in re.split('\r?\n',open(r'.\.\2022\2\input.txt','r').read())]
	# inp = [line.split(' ') for line in re.split('\r?\n',open(r'.\.\2022\2\input_test.txt','r').read())]

	solve1(inp) 
	solve2(inp)  


if __name__ == '__main__': 
	main() 
