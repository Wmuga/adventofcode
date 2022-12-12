import re 

def solve1(inp:list[list[str]]): 
	res = 0  
	x = 1
	stages = [20, 60, 100, 140, 180, 220]

	i = 0
	passed = 0
	to_pass = 1
	to_add = 0

	for cycle in range(0,221):
		passed+=1

		if cycle in stages:
			res += x * cycle

		if passed == to_pass:
			passed = 0
			command = inp[i]
			x += to_add
			if command[0] == 'noop':
				to_pass = 1
				to_add = 0
			elif command[0] == 'addx':
				to_pass = 2
				to_add = int(command[1])
			else:
				print('Wrong input: ', command)
			i+=1
		
	print(f'Solution 1: {res}')  
 
def solve2(inp:list[list[str]]):   
	print(f'Solution 2:')  
	x = 1
	i = 1
	passed = 0
	to_pass = 2 if inp[0][0] == 'addx' else 1
	to_add = int(inp[0][1]) if inp[0][0] == 'addx' else 0
	
	for _ in range(6):
		row = [' ' for _ in range(40)]
		for pos in range(40):
			passed +=1

			row[pos] = ('#' if -1 <= x - pos <= 1 else ' ')

			if passed == to_pass:
				passed = 0
				command = inp[i] if i < len(inp) else ['noop']
				x += to_add
				if command[0] == 'noop':
					to_pass = 1
					to_add = 0
				elif command[0] == 'addx':
					to_pass = 2
					to_add = int(command[1])
				else:
					print('Wrong input: ', command)
				i+=1
		print(''.join(row))


 
def read_input(file:str):
	return [line.split(' ') for line in re.split('\r?\n',open(file).read())]

def main(): 
	inp = read_input(r'.\2022\10\input_test.txt')  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\10\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
