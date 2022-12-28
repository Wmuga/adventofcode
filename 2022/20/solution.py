import re 

class ListNode:
	def __init__(self, elem = 0, prev:'ListNode' = None, next:'ListNode' = None):
		self.elem = elem
		self.prev = prev
		self.next = next

	def __repr__(self):
		prev = 'ListNode - ' if self.prev != None else ''
		next = ' - ListNode' if self.next != None else ''
		return f'{prev}| {self.elem} | {next}'

def convert(inp:list[int])->list[ListNode]:
	head = ListNode(int(inp[0]))
	elems = [head]
	tail = head
	for num in inp[1:]:
		tail.next = ListNode(int(num))
		tail.next.prev = tail
		tail = tail.next
		elems.append(tail)
	tail.next = head
	head.prev = tail
	return elems

def find_num(head:ListNode, num:int):
	cur = head
	while cur.elem != num:
		cur = cur.next
	return cur

def shuffle(inp:list[int], shuffle_rounds = 1, dec_key = 1, DEBUG = False)->ListNode:
	elems = convert(inp)
	for elem in elems:
		elem.elem *= dec_key
	
	m = len(inp) - 1
	for _ in range(shuffle_rounds):
		for cur in elems:
			steps = cur.elem % m

			if steps == 0:
				continue
			
			cur.prev.next = cur.next
			cur.next.prev = cur.prev
	
			new_prev = cur.prev
			for _ in range(steps):
				new_prev = new_prev.next
	
			cur.prev = new_prev
			cur.next = new_prev.next
			cur.prev.next = cur
			cur.next.prev = cur

			if DEBUG:
				print(f'|{cur.prev.elem}| - |{cur.elem}| - |{cur.next.elem}|')
		
	return cur

def solve1(inp:list[int], DEBUG = False): 
	head = find_num(shuffle(inp, DEBUG = DEBUG),0)
	steps = [1000 % len(inp), 2000 % len(inp), 3000 % len(inp)]
	nums = []
	for step in steps:
		cur = head
		for _ in range(step):
			cur = cur.next
		nums.append(cur.elem)
	if DEBUG:
		print(nums)
	print(f'Solution 1: {sum(nums)}')  
 
def solve2(inp:list[int], DEBUG = False): 
	head = find_num(shuffle(inp, 10, 811589153, DEBUG),0)
	steps = [1000 % len(inp), 2000 % len(inp), 3000 % len(inp)]
	nums = []
	for step in steps:
		cur = head
		for _ in range(step):
			cur = cur.next
		nums.append(cur.elem)
	if DEBUG:
		print(nums)
	print(f'Solution 2: {sum(nums)}')  
 
def read_input(file:str):
	return  [int(line) for line in re.split('\r?\n',open(file).read())]

def main(): 
	inp = read_input(r'.\2022\20\input_test.txt')  

	print('Test input:')
	solve1(inp, True) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\20\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
