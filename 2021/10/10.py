from functools import reduce

d ={'(':1,'[':2,'{':3,'<':4,'>':-4,'}':-3,']':-2,')':-1}
prices = [0,3,57,1197,25137]

def convert(line:str)->list[int]:
  return [d[i] for i in line]

def check_corruption(line:list[int],prev:list[int])->tuple[int,list[int]]:
  if not line:
    return 0,prev
  if line[0]>0:
    prev.append(line[0])
    return check_corruption(line[1:],prev)
  if line[0]<0:
    if not prev or abs(line[0])!=prev[-1]:
      return abs(line[0]),prev
    else:
      prev.pop()
      return check_corruption(line[1:],prev)  


def solve1(lines:str):
  print(reduce(lambda a,b: a+prices[check_corruption(convert(b),[])[0]],lines,0))

def solve2(lines:str):
  lines = [i for i in lines if not check_corruption(convert(i),[])[0]]
  res = sorted([reduce(lambda a,b: a*5+b,list(reversed(check_corruption(convert(line),[])[1])),0) for line in lines])
  print(res[int(len(res)/2)])

lines = [i.strip() for i in open('input.txt','r').readlines()]

solve1(lines)
solve2(lines)