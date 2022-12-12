from functools import reduce

dirs = ['N','E','S','W']


def unpack_instructions(lines:list[str])->list[tuple[str,int]]:
  return [(line[0],int(line[1:])) for line in lines]

def normalize(d:dict[str,int])->dict[str,int]:
  d['N']-=d['S']
  d['E']-=d['W']
  d['S'],d['W'] =0,0
  return d

def calc_pos1(instr:list[tuple[str,int]],face_dir:int)->dict[str,int]:
  d = {key:0 for key in dirs}
  for i in instr:
    if i[0]=='F':
      d[dirs[face_dir]]+=i[1]
      d = normalize(d)  
    elif i[0]=='R':
      face_dir = (face_dir + round(i[1]/90)+len(dirs)) % len(dirs) 
    elif i[0]=='L':
      face_dir = (face_dir - round(i[1]/90)+len(dirs)) % len(dirs)   
    else:
      d[i[0]]+=i[1]  
      d = normalize(d)  
  return d  

def calc_pos2(instr:list[tuple[str,int]],waypoint:dict[str,int])->dict[str,int]:
  d = {key:0 for key in dirs}
  for i in instr:
    if i[0]=='F':
      for key in waypoint:
        d[key]+=waypoint[key]*i[1]
        d = normalize(d)
    elif i[0]=='R':
      way1 = {}
      for key in waypoint:
        way1[dirs[(dirs.index(key) + round(i[1]/90)+len(dirs)) % len(dirs)]] = waypoint[key]
      waypoint = way1  
    elif i[0]=='L':
      way1 = {}
      for key in waypoint:
        way1[dirs[(dirs.index(key) - round(i[1]/90)+len(dirs)) % len(dirs)]] = waypoint[key]
      waypoint = way1  
    else:
      waypoint[i[0]]+=i[1]  
    waypoint = normalize(waypoint)
  return d  

def solve1(instr:list[tuple[str,int]]):
  pos = calc_pos1(instr,1)
  print(pos,abs(pos['N'])+abs(pos['E']))

def solve2(instr:list[tuple[str,int]]):
  pos = calc_pos2(instr,{'E':10,'N':1,'W':0,'S':0})
  print(pos,abs(pos['N'])+abs(pos['E']))

instr = unpack_instructions([i.strip() for i in open('input.txt','r').readlines()])

solve1(instr)
solve2(instr)