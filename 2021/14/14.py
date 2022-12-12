import re
from copy import deepcopy
from functools import reduce

def unpack(lines:list[str])->tuple[str,dict[str,str]]:
  template = lines[0]
  growth = dict()
  for line in lines[2:]:
    key,value = line.split(' -> ')
    growth[key] = value
  return template, growth  

def grow_polymer(template:str,growth:dict[str,str],ticks:int):
  for _ in range(ticks):
    i = 0
    while(i<len(template)):
      if(template[i:i+2] in growth):
        template = '{}{}{}'.format(template[:i+1],growth[template[i:i+2]],template[i+1:])
        i+=1
      i+=1  
  uniques = set(template)
  counts = list()
  for s in uniques:
    counts.append(len(list(re.findall(s,template))))
  return max(counts)-min(counts)  


def grow_polymer2(template:str,growth:dict[str,str],ticks:int):
  polymer = dict()
  for i in range(len(template)-1):
    key = template[i:i+2]
    if key in polymer:
      polymer[key]+=1
    else:
      polymer[key]=1

  for _ in range(ticks):
    new_polymer = deepcopy(polymer)

    for key in polymer:
      if key in growth:
        new_polymer[key]-=polymer[key]
        if new_polymer[key]==0:
          new_polymer.pop(key)
        keys = ['{}{}'.format(key[:1],growth[key]),'{}{}'.format(growth[key],key[1:])]
        for nk in keys:
          if nk in new_polymer:
            new_polymer[nk]+=polymer[key]
          else:
            new_polymer[nk]=polymer[key]


    polymer = new_polymer    
  
  counts = dict()

  for key in polymer.keys():
    s = key[1]
    if s in counts:
      counts[s] += polymer[key]
    else:
      counts[s] = polymer[key]  
    
  mx = reduce(lambda a,b: a if a > counts[b] else counts[b], counts.keys(), 0)      
  mn = reduce(lambda a,b: a if a < counts[b] else counts[b], counts.keys(), counts[list(counts.keys())[0]]) 

  return mx-mn     



def solve1(template:str,growth:dict[str,str]):
  print(grow_polymer2(template,growth,10))

def solve2(template:str,growth:dict[str,str]):
  print(grow_polymer2(template,growth,40))

template,growth = unpack([i.strip() for i in open('input.txt','r').readlines()])
# template,growth = unpack([i.strip() for i in open('input_test.txt','r').readlines()])


solve1(template,growth)
solve2(template,growth)


