import re 
from typing import Callable
from copy import deepcopy

def prod(lhs:int, rhs:int):
	return lhs * rhs

def sum(lhs:int, rhs:int):
	return lhs + rhs

module = 1

class Monkey:
	def __init__(self, items:list[int], op:Callable[[int,int],int], rhs:int, divisor:int, trueMonkey:int, falseMonkey:int):
		self.items = items
		self.op = op
		self.rhs = rhs
		self.divisor = divisor
		self.trueMonkey = trueMonkey
		self.falseMonkey = falseMonkey
	
	def round(self, monkeys:list['Monkey'], div:int)->list['Monkey']:
		for item in self.items:
			item = (self.op(item % module, int(self.rhs) if self.rhs != 'old' else item % module)//div)
			monkeys[self.trueMonkey if item % self.divisor == 0 else self.falseMonkey].items.append(item)
		self.items = []
		return monkeys

	def __repr__(self):
		return f'Monkey:\n\tItems: {self.items}\n\tOperation : {self.op} with {self.rhs}\n\tTest: divisible by {self.divisor}\n\t\tIf true: throw to monkey {self.trueMonkey}\n\t\tIf false: throw to monkey {self.falseMonkey}'

def round(monkeys:list[Monkey], div:int)->tuple[list[Monkey], list[int]]:
	i = 0
	items = [0 for _ in range(len(monkeys))] 
	while(i < len(monkeys)):
		items[i] = len(monkeys[i].items)
		monkeys = monkeys[i].round(monkeys,div)
		i+=1
	return monkeys, items

def makeRounds(monkeys:list[Monkey], roundCount:int, div:int)->tuple[list[Monkey], list[int]]:
	items = [0 for _ in range(len(monkeys))] 
	for _ in range(roundCount):
		monkeys, buf = round(monkeys, div)
		items = [item + buf[i] for i, item in enumerate(items)]
	return monkeys, items

def solve1(monkeys:list['Monkey']): 
	monkeys, items= makeRounds(monkeys,20, 3)
	items = sorted(items)  
	print(f'Solution 1: {items[-1]*items[-2]}')  
 
def solve2(monkeys:list['Monkey']): 
	monkeys, items= makeRounds(monkeys,10000, 1)
	items = sorted(items)  
	print(items)
	print(f'Solution 2: {items[-1]*items[-2]}') 
 
def read_input(file:str)->list[Monkey]:
	global module
	module = 1
	monkeys_raw = [re.split('\r?\n',m)[1:] for m in re.split('\r?\n\r?\n',open(file).read())]
	monkeys = list()
	for m in monkeys_raw:
		items = [int(item) for item in m[0].split(': ')[1].split(', ')]
		op = sum if m[1].split('old ')[1][0]=='+' else prod
		rhs = m[1].split(' ')[-1]
		divisor = int(m[2].split(' ')[-1])
		module *= divisor
		tm = int(m[3].split(' ')[-1])
		fm = int(m[4].split(' ')[-1])
		monkeys.append(Monkey(items, op, rhs, divisor, tm, fm))
	return monkeys

def main(): 
	inp = read_input(r'.\2022\11\input_test.txt')  

	# for monkey in inp:
	# 	print(monkey)

	print('Test input:')
	solve1(deepcopy(inp)) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\11\input.txt')  

	print('Actual input:')
	solve1(deepcopy(inp)) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
