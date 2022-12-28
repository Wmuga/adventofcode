import re 

ROCKS = [
	['####'],
	['.#.','###','.#.'],
	['..#','..#','###'],
	['#','#','#','#'],
	["##","##"]
]
OFFSET = (2, 4)
WIDTH = 7

DEBUG = 0

def apply_offset(rock,x,field, y,pattern):
	x += pattern
	if x < 0:
		return 0
	if x + len(ROCKS[rock][0]) > WIDTH:
		return x - 1
	
	for i,rock_line in enumerate(ROCKS[rock][::-1],start = y):
		if i >= len(field):
			break
		
		line = field[i]
		if line == 0:
			continue
		
		for x1, pix in enumerate(rock_line, start=x):
			if pix == '#' and line & (1<<(WIDTH - x1 - 1)) != 0:
				return x - pattern
	
	return x

def try_fall(field,y, rock, x):
	for i, rock_line in enumerate(ROCKS[rock][::-1],start=y):
		if i >= len(field):
			return True
		line = field[i]
		for x1,pix in enumerate(rock_line,start=x):
			if pix == '#' and (line & (1<<(WIDTH - x1 - 1)) != 0):
				return False
	return True

def simulate(patterns:list, rock_count:int):
	max_y = -1
	field = [0]
	cur_pattern = 0
	cur_rock = 0
	dups = 0
	y_diff_dup = 0
	
	file = None
	if DEBUG:
		file = open(r'2022\17\debug.log','w')

	fallen_rocks = []

	for rock in range(rock_count):
		x = 2
		y = max_y + 1
		for _ in range(3):
			x = apply_offset(cur_rock, x, field, y, patterns[cur_pattern])
			cur_pattern = (cur_pattern + 1) % len(patterns)
		
		falling = True
		if len(field) <= y:	
			field.append(0)

		while falling:
			x = apply_offset(cur_rock, x, field, y, patterns[cur_pattern])
			cur_pattern = (cur_pattern + 1) % len(patterns)
		
			if y != 0 and try_fall(field,y-1, cur_rock, x):
				y -= 1
				continue

			falling = False

			for y1,line in enumerate(ROCKS[cur_rock][::-1],start=y):
				for x1, pix in enumerate(line, start=x):
					if len(field) <= y1:
						field.append(0)
					if pix == '#':
						field[y1] |= 1<<(WIDTH - x1 - 1)

			if DEBUG == 1:
				file.write(f'Rock: {rock+1}\n')
				for line in field[::-1]:
					file.write('|{}|\n'.format(''.join(['.' if bit=='0' else '#' for bit in bin(line)[2:].zfill(7)])))
				file.write('+-------+\n\n')
		# add checks for 3-10 dups in row
		for i, fallen_rock in enumerate(fallen_rocks[::-1]):
			if fallen_rock[0] == x and fallen_rock[2] == cur_rock and fallen_rock[3] == cur_pattern:
				y_diff = max_y - fallen_rock[1]
				start_rock = len(fallen_rocks) - i - 1
				cycle_rock_count = rock - start_rock
				if y_diff == y_diff_dup:
					dups += 1
				else:
					dups = 1
					y_diff_dup = y_diff
				if dups == 10:
					start_ind =  (rock_count - start_rock) % cycle_rock_count + start_rock
					y_start = fallen_rocks[start_ind][1]
					return y_start + y_diff*((rock_count -start_ind)//cycle_rock_count) + 1

		fallen_rocks.append((x,max_y,cur_rock, cur_pattern))

		max_y = len(field) -1
		while field[max_y] == 0:
			max_y -= 1
		
		if DEBUG == 2:
			file.write(f'{max_y+1}\n')

		cur_rock = (cur_rock + 1) % len(ROCKS)

	if DEBUG:
		file.close()

	return max_y+1


def solve1(patterns:list): 
	res = simulate(patterns, 2022)
	print(f'Solution 1: {res}')  
 
def solve2(patterns:list): 
	res = simulate(patterns, 1000000000000)  
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return  [-1 if p == '<' else 1 for p in re.split('\r?\n',open(file).read())[0]]

def main(): 
	inp = read_input(r'.\2022\17\input_test.txt')  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\17\input.txt')  

	if not DEBUG:
		print('Actual input:')
		solve1(inp) 
		solve2(inp) 



if __name__ == '__main__': 
	main() 
