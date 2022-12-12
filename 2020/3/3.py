def count_trees(lines:list,step_right:int,step_down:int):
  column = 0
  trees = 0
  for row in range(step_down,len(lines),step_down):
    column = (column + step_right + len(lines[0]))%len(lines[0])
    if lines[row][column]=='#':
      trees+=1
  return trees

def solve1(lines:list):
  print(count_trees(lines,3,1))

def solve2(lines:list):
  res = count_trees(lines,1,1) 
  res *= count_trees(lines,3,1) 
  res *=count_trees(lines,5,1) 
  res *=count_trees(lines,7,1) 
  res *=count_trees(lines,1,2) 
  print(res)


lines = [i.strip() for i in open('input.txt','r').readlines()]

solve1(lines)
solve2(lines)