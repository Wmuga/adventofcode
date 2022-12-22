import re 
from copy import copy

FUNCS = {
	"*": lambda a, b : a *  b,
	"+": lambda a, b : a +  b,
	"-": lambda a, b : a -  b,
	"/": lambda a, b : a // b,
	"=": lambda a, b : a == b
}

def process(vars, to_proccess):
	changed = True
	while len(to_proccess) > 0 and changed:
		i = 0
		changed = False
		while i < len(to_proccess):
			try:
				re_res = to_proccess[i]
				vars[re_res[0]] = FUNCS[re_res[2]](int(vars[re_res[1]]),int(vars[re_res[3]]))
				to_proccess.pop(i)
				changed = True
			except:
				i+=1
	return vars, to_proccess


def solve1(inp:list[str]): 
	vars = {}
	def_reg = re.compile('(.+): (\d+)')
	eq_reg = re.compile('(.+): (.+) ([+*-/]) (.+)')
	to_proccess = []
	for line in inp:
		re_res = def_reg.findall(line)
		if len(re_res) != 0:
			re_res = re_res[0]
			vars[re_res[0]] = int(re_res[1])
		else:
			re_res = eq_reg.findall(line)
			re_res = re_res[0]
			to_proccess.append(re_res)
	
	return process(vars,to_proccess)
	
 
def solve2(inp:list[str]): 
	res=-1  
	
	iHumn, iRoot, v1, v2 = -1,-1,'',''
	for i, line in enumerate(inp):
		if line.startswith('root'):
			iRoot = i
			v1,v2 = re.findall('root: (.+) . (.+)', line)[0]
		elif line.startswith('humn'):
			iHumn = i
		if iHumn != -1 and iRoot != -1:
			break
	if iHumn < iRoot:
		inp.pop(iRoot)
		inp.pop(iHumn)
	else:
		inp.pop(iHumn)
		inp.pop(iRoot)

	vars, to_process = solve1(inp)
	iv1, iv2, lineV1, lineV2 = -1,-1,'',''
	for i,line in enumerate(to_process):
		if line[0] == v1:
			iv1 = i
			lineV1 = f'{line[1]}{line[2]}{line[3]}'
		elif line[0] == v2:
			iv2 = i
			lineV2 = f'{line[1]}{line[2]}{line[3]}'
		if iv1 != -1 and iv2 != -1:
			break
	
	if iv1 < iv2:
		to_process.pop(iv2)
		if iv1 != -1:
			to_process.pop(iv1)
		else:
			lineV1 = str(vars[v1])
	else:
		to_process.pop(iv1)
		if iv2 != -1:
			to_process.pop(iv2)
		else:
			lineV2 = str(vars[v2])

	i = 0
	changed = True
	while changed:
		changed = False
		for line in to_process:
			if lineV1.find(line[0]) != -1:
				changed = True
				lineV1 = lineV1.replace(line[0], f'({line[1]}{line[2]}{line[3]})')
			if lineV2.find(line[0]) != -1:
				changed = True
				lineV2 = lineV2.replace(line[0], f'({line[1]}{line[2]}{line[3]})')
	
	for var in vars.keys():
		lineV1 = lineV1.replace(var, str(vars[var]))
		lineV2 = lineV2.replace(var, str(vars[var]))

	print(f'Solution 2:\n{lineV1}\n==\n{lineV2}')  
 
def read_input(file:str):
	return  re.split('\r?\n',open(file).read())

def main(): 
	inp = read_input(r'.\2022\21\input_test.txt')  

	print('Test input:')
	vars, _ = solve1(inp) 
	print('Solution 1:', vars['root'])
	solve2(inp) 
 
	inp = read_input(r'.\2022\21\input.txt')  

	print('Actual input:')
	vars, _ = solve1(inp)
	print('Solution 1:', vars['root'])
	solve2(inp) 


if __name__ == '__main__': 
	main() 
