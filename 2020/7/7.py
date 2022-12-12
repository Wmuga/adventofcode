from functools import reduce

def dict_parser(prev:dict,cur:str):
  data = cur.split(' contain ')
  key = ' '.join(data[0].split(' ')[:-1])
  value = [(' '.join(i.split(' ')[1:-1]),int(i.split(' ')[0]) if i.split(' ')[0]!='no' else 0) for i in data[1].split(', ')]
  prev[key]=value
  return prev

def create_dict(lines:list[str]):
  return reduce(dict_parser,lines,dict())

def get_colors_contain_key(bags:dict,current_key:str,start_key:str,colors:set):
  if current_key not in bags:
    return colors
 
  if current_key!= start_key: colors.add(current_key)

  cont_keys = set()
  for key in bags:
    for bag in bags[key]:
      if bag[0]==current_key:
        cont_keys.add(key)        
  if len(cont_keys)==0:
    return colors 

  return reduce(lambda a,b: a.union(b),[get_colors_contain_key(bags,cont_key,start_key,colors) for cont_key in cont_keys])

def get_bags_contains_count(bags:dict,current_bag:tuple):
  if current_bag[0] not in bags:
    return 1
  return sum([bag[1]+bag[1]*get_bags_contains_count(bags,bag) for bag in bags[current_bag[0]]])

def solve1(bags:dict):
  current_key = 'shiny gold'
  print(len(get_colors_contain_key(bags,current_key,current_key,set())))

def solve2(bags:dict):
  current_key = 'shiny gold'
  print(get_bags_contains_count(bags,(current_key,0)))



bags = create_dict([i.strip() for i in open('input.txt','r').readlines()])
solve1(bags)
solve2(bags)
