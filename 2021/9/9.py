from functools import reduce
from copy import deepcopy
def check_nearest(lines:list[list[int]],x:int,y:int)->bool:
  return (lines[x-1][y]>lines[x][y] if x>0  else True) and (lines[x+1][y]>lines[x][y] if x<len(lines)-1 else True) and (lines[x][y+1]>lines[x][y] if y<len(lines[0])-1 else True) and (lines[x][y-1]>lines[x][y] if y>0 else True)


def get_lowest(lines:list[list[int]])->list[tuple[int,int,int]]:
  l = list()
  for x,line in enumerate(lines):
    for y,height in enumerate(line):
      if (check_nearest(lines,x,y)): l.append((height,x,y))
  return l    

def set_basins(lines:tuple[list[list[int]],list[list[int]]],x:int,y:int):
  if lines[1][x][y]: return
  if (lines[0][x][y]!=9):
     lines[1][x][y] = 1
     if x>0:
       set_basins(lines,x-1,y)
     if y>0:
       set_basins(lines,x,y-1)  
     if x<len(lines[0])-1:
       set_basins(lines,x+1,y)
     if y<len(lines[0][0])-1:
       set_basins(lines,x,y+1)   

def get_basins_length(lines:tuple[list[list[int]],list[list[int]]])->list[int]:
  lowest = get_lowest(lines[0])
  res = []
  for _,coords in enumerate(lowest):
    n_lines = deepcopy(lines)
    set_basins(n_lines,coords[1],coords[2])
    res.append(reduce(lambda a,b: a+ sum(b),n_lines[1],0))
  return res


def get_basins(lines:list[list[int]]):
  lines = lines,[[0 for _ in range(len(line))] for _,line in enumerate(lines)]
  res = get_basins_length(lines)  
  return reduce(lambda a,b:a*b,sorted(res)[-3:],1)

def solve1(lines:list[list[int]]):
  print(reduce(lambda a,b: a+b[0]+1, get_lowest(lines),0))

def solve2(lines:list[list[int]]):
  print(get_basins(lines))  

lines = [[int(b) for b in list(i.strip())] for i in open('input.txt','r').readlines()]  
# lines = [[int(b) for b in list(i.strip())] for i in open('input_test.txt','r').readlines()]  

solve1(lines)
solve2(lines)