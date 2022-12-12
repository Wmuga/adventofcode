import re 

def base_solution(inp:list[list[str,int]],snake_length:int)->int:
	cache = set()
	cache.add('0,0')
	snake = [[0,0] for _ in range(snake_length)]

	for direction,count in inp:
		for _ in range(count):
			if direction == 'L':
				snake[0][0] -= 1
			elif direction == 'R':
				snake[0][0] += 1
			elif direction == 'D':
				snake[0][1] -= 1
			elif direction == 'U':
				snake[0][1] += 1
			else:
				print('Unknown input')
				print(direction, count)
				exit(-1)
			
			for i in range(1,snake_length):
				delta_hor = snake[i-1][0] - snake[i][0]
				delta_ver = snake[i-1][1] - snake[i][1]
				
				if abs(delta_ver) == 2 and abs(delta_hor) == 2:
					snake[i] = [snake[i][0]+delta_hor//2, snake[i][1] + delta_ver//2] 
				elif abs(delta_ver) == 2:
					snake[i] = [snake[i][0]+delta_hor, snake[i][1] + delta_ver//2] 
				elif abs(delta_hor) == 2:
					snake[i] = [snake[i][0]+delta_hor//2, snake[i][1] + delta_ver]
			
			cache.add(f'{snake[snake_length-1][1]},{snake[snake_length-1][0]}')
	return len(cache)

def solve1(inp:list[list[str,int]]): 
	print(f'Solution 1: {base_solution(inp,2)}')  
 
def solve2(inp:list[list[str,int]]): 
	print(f'Solution 2: {base_solution(inp,10)}')  
 
def read_input(file:str):
	return  [(lambda a:[a[0],int(a[1])])(line) for line in [line.split() for line in re.split('\r?\n',open(file).read())]]

def main(): 
	inp = read_input(r'.\2022\9\input_test.txt')  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\9\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
