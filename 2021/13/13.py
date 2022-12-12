from copy import deepcopy
from functools import reduce

def unpack(lines:list[str])->tuple[list[tuple[int,int]],list[tuple[int,int]]]:
  dots = list()
  folds = list()
  for i,line in enumerate(lines):
    if len(line)==0:
      break
    data = line.split(',')
    dots.append((int(data[0]),int(data[1])))
  for line in lines[i+1:]:
    data = line.split('=')
    folds.append((int('y' in data[0]),int(data[1])))
  return dots,folds  

def fold(dots:list[tuple[int,int]],cfold:tuple[int,int])->list[tuple[int,int]]:
  if not cfold[0]:
    for i,dot in enumerate(dots):
      if dot[0]>cfold[1] and (cfold[1]-(dot[0]-cfold[1]))>=0:
        dots[i] = (cfold[1]-(dot[0]-cfold[1]),dot[1])
  else:
    for i,dot in enumerate(dots):
      if dot[1]>cfold[1] and (cfold[1]-(dot[1]-cfold[1]))>=0:
       dots[i] = (dot[0],cfold[1]-(dot[1]-cfold[1]))   
  return list(set(dots))     

def draw(dots:list[tuple[int,int]]):
  max_x = reduce(lambda a,b: max(a,b[0]),dots,0)
  max_y = reduce(lambda a,b: max(a,b[1]),dots,0)
  field = [['#' if (x,y) in dots else '.' for x in range(max_x+1)] for y in range(max_y+1)]
  for line in field:
    print(''.join(line))

def solve1(dots:list[tuple[int,int]],ffold:tuple[int,int]):
  ndots = fold(deepcopy(dots),ffold)
  print(len(ndots))

def solve2(dots:list[tuple[int,int]],folds:list[tuple[int,int]]):
  for cfold in folds:
    dots = fold(dots,cfold)
  draw(dots)

data = unpack([i.strip() for i in open('input.txt','r').readlines()])
# data = unpack([i.strip() for i in open('input_test.txt','r').readlines()])

solve1(data[0],data[1][0])
solve2(data[0],data[1])