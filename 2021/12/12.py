def unpack(lines:list[str])->dict[str,list[str]]:
  paths:dict[str,list[str]] = dict()
  for line in lines:
    data = line.split('-')
    if data[0] not in paths:
      paths[data[0]]=list()
    if data[1] not in paths:
      paths[data[1]]=list()  
    paths[data[0]].append(data[1]) 
    paths[data[1]].append(data[0]) 
  return paths

def count_paths(paths:dict[str,list[str]],current_cave:str,small_cave_vis:list[str],vis:bool)->int:
  small_cave_vis = list(small_cave_vis)
  if current_cave == 'end':
    return 1  
  if current_cave.lower()==current_cave:
    if current_cave in small_cave_vis:
      vis=True
    small_cave_vis.append(current_cave)
  return sum([count_paths(paths,i,small_cave_vis,vis) for i in paths[current_cave] if i !='start' and (not vis or (i not in small_cave_vis))])      

def solve1(paths:dict[str,list[str]]):
  print(count_paths(paths,'start',[],True))

def solve2(paths:dict[str,list[str]]):
  print(count_paths(paths,'start',[],False))


# paths = unpack([i.strip() for i in open('input_test.txt','r').readlines()])
paths = unpack([i.strip() for i in open('input.txt','r').readlines()])

solve1(paths)
solve2(paths)