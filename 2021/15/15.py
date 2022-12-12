import sys
sys.setrecursionlimit(26000)


def find_easiest(paths:list[list[int]],risks:list[list[int]],x:int,y:int)->int:
  if x<0 or y<0:
    return 99999999  
  if x==0 and y==0:
    return paths[x][y]  
  if risks[x][y]!=-1:
    return risks[x][y]
  level = x//len(paths) + y//len(paths[0])
  risks[x][y] = ((paths[x%len(paths)][y%len(paths[0])]+level) % 9 or 9) + min(find_easiest(paths,risks,x-1,y),find_easiest(paths,risks,x,y-1))
  
  return risks[x][y]


def solve1(lines:list[list[int]]):
  risks = [[-1 for _ in l] for l in lines]
  print(find_easiest(lines,risks,len(lines)-1,len(lines[0])-1)-lines[0][0])

# 2858 on my input. Should be
def solve2(lines:list[list[int]]):
  risks = [[-1 for _ in range(len(lines[0])*5)] for _ in range(len(lines)*5)]
  print(find_easiest(lines,risks,len(lines)*5-1,len(lines[0])*5-1)-lines[0][0])


lines = [[int(j) for j in i.strip()] for i in open('input.txt','r').readlines()]
# lines = [[int(j) for j in i.strip()] for i in open('input_test.txt','r').readlines()]


solve1(lines)
solve2(lines)