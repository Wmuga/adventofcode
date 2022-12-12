def flash(octs:list[list[int]],x:int,y:int):
  for x1 in range(x-1,x+2):
    for y1 in range(y-1,y+2):
      try:
        if x1>=0 and y1>=0 and octs[x1][y1]!=0:
          octs[x1][y1]+=1
      except IndexError:
        pass    
  return octs


def get_coords(octs:list[list[int]])->list[tuple[int,int]]:
  res = list()
  for x, line in enumerate(octs):
    for y,v in enumerate(line):
      if v>9:
        res.append((x,y))
  return res

def emulate(octs:list[list[int]],end_step:int)->int:
  flashes = 0 
  for step in range(end_step):
    octs = [[j+1 for j in line] for line in octs]
    changed = True
    while(changed):
      changed = False
      coords = get_coords(octs)
      flashes+=len(coords)
      for x,y in coords:
        octs[x][y]=0
        octs = flash(octs,x,y)
        changed = True
    # print(step,flashes)
    # for line in octs:  
    #   print(line)
  return flashes,octs      


def solve1(octs:list[list[int]]):
  res = emulate(octs,100)
  print(res[0])

def solve2(octs:list[list[int]]):
  step =  0
  stop = False
  while(not stop):
    stop = True
    step+=1
    res = emulate(octs,1)
    octs = res[1]
    for line in octs:
      for v in line:
        if not stop:
          break
        if v!=0:
          stop = False
  print(step)

octs = [[int(j) for j in list(i.strip())] for i in open('input.txt','r').readlines()]

solve1(octs)
solve2(octs)    