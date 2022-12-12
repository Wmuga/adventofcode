import copy

def get_diffs(nums:list[int]):
  d = {1:0,2:0,3:0}
  for i, num in enumerate(nums[1:]):
    d[num-nums[i]]+=1
  d[nums[0]-0]+=1  
  d[3]+=1  
  return d  

def addElem(a:list,b:int):
  c = copy.copy(a)
  c[len(c):] = [b]
  return c

def count_connections(nums:list[int],connection_line:list[int],counts:dict):
  if (connection_line[-1]==nums[-1]):
    return 1
  if (connection_line[-1]!=0 and connection_line[-1] not in nums):
    return 0
  if connection_line[-1] not in counts:
    counts[connection_line[-1]] = count_connections(nums,addElem(connection_line,connection_line[-1]+1),counts)+count_connections(nums,addElem(connection_line,connection_line[-1]+2),counts)+count_connections(nums,addElem(connection_line,connection_line[-1]+3),counts) 
  return counts[connection_line[-1]]


def solve1(nums:list[int]):
  diffs = get_diffs(nums)
  print(diffs[1]*diffs[3])

def solve2(nums:list[int]):
  print(count_connections(nums,[0],dict()))

nums = sorted([int(i.strip()) for i in open('input.txt','r').readlines()])
solve1(nums)
solve2(nums)