import re 

def intersection(l:list[int],r:list[int])->list[int]:
	mm = [lambda a,b:-b,max,min,max,min,max,min]
	n = [mm[i](l[i],r[i]) for i in range(7)]
	return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n

def countoncubes(cores):
    oncount = 0
    for c in cores:
        oncount += c[0] * (c[2]-c[1]+1) * (c[4]-c[3]+1) * (c[6]-c[5]+1)
    return oncount

def solve1(inp:list[list[int]]): 
	cores = []
	for cuboid in inp:
		cuboid = intersection(cuboid, [1, -50, 50, -50, 50, -50, 50])
		if cuboid:
			toadd = [cuboid] if cuboid[0] == 1 else [] # add cuboid to core if 'on'
			for core in cores:
				inter = intersection(inter, core)
				if inter:
					toadd += [inter] # if nonempty, add to the core later
			cores += toadd 
	print(f'Solution 1: {countoncubes(cores)}')  
 
def solve2(inp:list[list[int]]): 
	cores = []
	for cuboid in inp:
		toadd = [cuboid] if cuboid[0] == 1 else [] # add cuboid to core if 'on'
		for core in cores:
			inter = intersection(cuboid,core)
			if inter:
				toadd += [inter] # if nonempty, add to the core later
		cores += toadd 
	print(f'Solution 2: {countoncubes(cores)}')  
 
def main(): 
	inp = re.split('\r?\n',open(r'.\.\2021\22\input_test.txt','r').read()
	.replace('x=','').replace(',y=',' ').replace(',z=',' ').replace('..',' ')
	.replace('on','1').replace('off','0'))  
	inp = [[int(i) for i in line.split(' ')] for line in inp]

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = re.split('\r?\n',open(r'.\.\2021\22\input.txt','r').read()
	.replace('x=','').replace(',y=',' ').replace(',z=',' ').replace('..',' ')
	.replace('on','1').replace('off','0'))  
	inp = [[int(i) for i in line.split(' ')] for line in inp]

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
