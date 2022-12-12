import re 
from collections.abc import Callable

class Tree:
	def __init__(self, type:str, data:str | int, connections:dict[str, 'Tree'], prev:'Tree'):
		self.type = type
		self.connections = connections
		self.data = data
		self.prev = prev

	def __repr__(self):
		return f'TreeNode: {self.type}, {self.data=}, {self.connections=}'
		

def form_dirs(lines:list[list[str]]):
	head = Tree('dir', '/', dict(), None)
	cur = head
	i = 0
	while i < len(lines):
		line = lines[i]
		if line[0] == '$':
			if line[1] == 'cd':
				if line[2] == '/':
					cur = head
				elif line[2] == '..':
					cur = cur.prev
				else:
					cur = cur.connections[line[2]]
				i+=1
			elif line[1] == 'ls':
				i+=1
				line = lines[i]
				while line[0] != '$':
					if line[0] == 'dir':
						cur.connections[line[1]] = Tree('dir', line[1], dict(), cur)
					else:
						cur.connections[line[1]] = Tree('file', int(line[0]), dict(), cur)
					i+=1
					if (i<len(lines)): 
						line = lines[i]
					else:
						break
	return head

def calc_size(dir:Tree, callback:Callable[[int],None])->int:
		res = 0
		for key in dir.connections:
			tree = dir.connections[key]
			if tree.type == 'file':
				res += tree.data
			elif tree.type == 'dir':
				res += calc_size(tree, callback)
			else:
				print(f'Хто? {tree.type=}')
				exit(-1)
		
		if callback: callback(res)

		return res

def solve1(head:Tree): 
	res=0  
	dirs = []

	def callback(res:int):
		if res <= 100000:
			dirs.append(res)

	calc_size(head, callback)

	for dir in dirs:
		res += dir

	print(f'Solution 1: {res}')  
 
def solve2(head:Tree): 
	res=0  
	dirs = []

	def callback(res:int):
		dirs.append(res)

	main_size = calc_size(head, callback)
	rem = 30000000 - (70000000 - main_size)
	diff = main_size
	for dir in dirs:
		if dir >= rem and diff > (dir - rem):
			diff = dir-rem
			res = dir

	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return  [line.split(' ') for line in re.split('\r?\n',open(file).read())]

def main(): 
	inp = read_input(r'.\2022\7\input_test.txt')  

	dirs = form_dirs(inp)
	# print(dirs)

	print('Test input:')
	solve1(dirs) 
	solve2(dirs) 
 
	inp = read_input(r'.\2022\7\input.txt')  

	dirs = form_dirs(inp)
	# print(dirs)

	print('Actual input:')
	solve1(dirs) 
	solve2(dirs) 


if __name__ == '__main__': 
	main() 
