import re 

def solve1(inp:list[list[int]]): 
	res=0  
	# False - visible. True - Invisible. Assume all invisible
	trees = [[(tree,True) if (i>0 and i<len(line)-1) else (tree, 0) for i,tree in enumerate(line)] for line in inp]
	trees[0] = [(tree,False) for tree,_ in trees[0]]
	trees[-1] = [(tree,False) for tree,_ in trees[-1]]
	
	def check_tree(max_tree:int,i:int,j:int,i_delta:int,j_delta:int)->int:
		max_tree = max(max_tree, trees[i+i_delta][j+j_delta][0])
		tree = trees[i][j]
		if tree[1] and tree[0] > max_tree:
			trees[i][j] = (tree[0], False)
		return max_tree

	max_treeu_l = [tree[0] for tree in trees[0]]
	for i in range(1,len(trees)-1):
		max_treel = trees[i][0][0]
		for j in range(1, len(trees[i])-1):
			max_treel = check_tree(max_treel,i,j,0,-1)
			max_treeu_l[j] = check_tree(max_treeu_l[j],i,j,-1,0)

	# for line in trees:
	# 	print(''.join(['1' if invis else '0' for _, invis in line]))
	
	# print('')

	max_treeu_l = [tree[0] for tree in trees[-1]]
	for i in range(len(trees)-2,0,-1):
		max_treel = trees[i][-1][0]
		for j in range(len(trees[i])-2,0,-1):
			max_treel = check_tree(max_treel,i,j,0,1)
			max_treeu_l[j] = check_tree(max_treeu_l[j],i,j,1,0)

	# for line in trees:
	# 	print(''.join(['1' if invis else '0' for _, invis in line]))

	for line in trees:
		for _, invis in line:
			if not invis:
				res+=1

	print(f'Solution 1: {res}')  
 
def solve2(inp:list[list[int]]): 
	res=0 
	for i in range(1, len(inp)-1):
		for j in range(1,len(inp)-1):
			score = []
			seen = 0
			for i1 in range(i-1,-1,-1):
				seen += 1
				if inp[i1][j] >= inp[i][j]:
					break
			score.append(seen)
			
			seen = 0
			for i1 in range(i+1,len(inp)):
				seen += 1
				if inp[i1][j] >= inp[i][j]:
					break
			score.append(seen)

			seen = 0
			for j1 in range(j-1,-1,-1):
				seen += 1
				if inp[i][j1] >= inp[i][j]:
					break
			score.append(seen)
			
			seen = 0
			for j1 in range(j+1,len(inp[i])):
				seen += 1
				if inp[i][j1] >= inp[i][j]:
					break
			score.append(seen)

			res = max(res, score[0]*score[1]*score[2]*score[3])
	print(f'Solution 2: {res}')  
 
def read_input(file:str)->list[list[int]]:
	return  [[int(tree) for tree in list(line)]for line in re.split('\r?\n',open(file).read())]

def main(): 
	inp = read_input(r'.\2022\8\input_test.txt')  

	print('Test input:')
	solve1(inp) 
	solve2(inp) 
 
	inp = read_input(r'.\2022\8\input.txt')  

	print('Actual input:')
	solve1(inp) 
	solve2(inp) 


if __name__ == '__main__': 
	main() 
