from copy import deepcopy

def count_occupied(field:list[list[str]]):
  return sum([row.count('#') for row in field])


def count_occupied_nearby(field:list[list[str]],x:int,y:int):
  return count_occupied([row[max(0,y-1):min(len(field[0]),y+2)] for row in field[max(0,x-1):min(len(field),x+2)]])-(1 if field[x][y]=='#' else 0) 


def count_occupied_visibly(field:list[list[str]],x:int,y:int):
  count = 0
  # column
  for i in range(min(x+1,len(field)),len(field)):
    if field[i][y] != '.':
      count += 1 if field[i][y] == '#' else 0
      break
  for i in reversed(range(0,max(x,0))):
    if field[i][y] != '.':
      count += 1 if field[i][y] == '#' else 0
      break  
  # row
  for i in range(min(y+1,len(field[0])),len(field[0])):
    if field[x][i] != '.':
      count += 1 if field[x][i] == '#' else 0
      break
  for i in reversed(range(0,max(y,0))):
    if field[x][i] != '.':
      count += 1 if field[x][i] == '#' else 0
      break 
  # diagonal
  for i in range(1,min(len(field)-x,len(field[0])-y)+1):
    try:
      if field[x+i][y+i] != '.':
        count += 1 if field[x+i][y+i] == '#' else 0
        break
    except IndexError:
      break  
  for i in range(1,min(x,y)+1):
    try:
      if field[x-i][y-i] != '.':
        count += 1 if field[x-i][y-i] == '#' else 0
        break 
    except IndexError:
      break
  for i in range(1,min(len(field)-x,y)+1):
    try:
      if field[x+i][y-i] != '.':
        count += 1 if field[x+i][y-i] == '#' else 0
        break 
    except IndexError:
      break
  for i in range(1,min(x,len(field[0])-y)+1):
    try:
      if field[x-i][y+i] != '.':
        count += 1 if field[x-i][y+i] == '#' else 0
        break   
    except IndexError:
      break        
  return count

def round(field:list[list[str]],count_occ,toleracy:int):
  new_field = deepcopy(field)
  changed = 0
  for i in range(len(field)):
    for j in range(len(field[i])):
      occupied = count_occ(field,i,j)
      if occupied==0 and field[i][j]=='L':
        new_field[i][j]='#'
        changed +=1
      elif occupied>toleracy and field[i][j]=='#':
        new_field[i][j]='L'  
        changed +=1
  return new_field,changed      

def solve1(field:list[list[str]]):
  new_field = deepcopy(field)
  while(True):
    new_field,changed = round(new_field,count_occupied_nearby,3)
    if not changed:
      break
  print(count_occupied(new_field))

def solve2(field:list[list[str]]):
  new_field = deepcopy(field)
  while(True):
    new_field,changed = round(new_field,count_occupied_visibly,4)
    if not changed:
      break
  print(count_occupied(new_field))

field = [list(i.strip()) for i in open('input.txt','r').readlines()]

solve1(field)
solve2(field)