from functools import reduce

def get_answers_count(lines:list):
  answers_count = list()
  group = set()
  for line in lines:
    if len(line)==0:
      answers_count.append(len(group))
      group = set()
      continue

    for answer in line:
      group.add(answer)

  if len(group)>0:
    answers_count.append(len(group))

  return answers_count         

def get_same_answers_count(lines:list):
  answers = list()
  group = list()
  for line in lines:
    if len(line)==0:
      answers.append(len(reduce(lambda a,b: a.intersection(b), group)))
      group = list()
      continue

    group.append(set(line))

  if len(group)>0:
    answers.append(len(reduce(lambda a,b: a.intersection(b), group)))  

  return answers     

def solve1(lines:list):
  print(reduce(lambda prev,cur: prev+cur, get_answers_count(lines),0))

def solve2(lines:list):
  print(reduce(lambda prev,cur: prev+cur, get_same_answers_count(lines),0))

lines =[i.strip() for i in open('input.txt','r').readlines()]

solve1(lines)
solve2(lines)

