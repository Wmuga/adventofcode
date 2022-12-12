import re
from functools import reduce

class TicketValidation:
  def __init__(self,ranges:list[str]):
    self.ranges = {}
    for line in ranges:
      data = line.split(': ')
      self.ranges[data[0]] = [tuple(int(num) for num in range.split('-')) for range in data[1].split(' or ')]
  
  def __parse_value(self,value):
    valid_keys = list()
    for key,ranges in self.ranges.items():
      if reduce(lambda a,b: a or any(b),[[range[0]<=value<=range[1]] for range in ranges],False):
        valid_keys.append(key)
    if valid_keys:
      return (True,valid_keys,value)
    return (False,value)    

  def parse(self,ticket:tuple):
    return [self.__parse_value(value) for value in ticket]        
  
  def __str__(self):
    return str(self.ranges)

def solve1(validation:TicketValidation,other:list):
  s = 0
  for ticket in other:
    res = validation.parse(ticket)
    s+= sum([r[1] for r in res if not r[0]])
  print(s)

def solve2(validation:TicketValidation,other:list,your:tuple):
  parsed = []
  for ticket in other:
    res = validation.parse(ticket)
    if not all([r[0] for r in res]):
      continue
    parsed.append([r[1] for r in res])
  fields = [0 for _ in parsed[0]]
  
  not_parsed = [i for i in range(len(parsed[0]))]
  
  while not_parsed:
    for i,field in enumerate(parsed[0]):
      if i in not_parsed:
        field1 = set(field)
        field1 = field1.difference(set(fields))
        if len(field1)>1:
          for ticket in parsed[1:]:
            field1 = field1.intersection(set(ticket[i]))
        if len(field1)>1:
          for an_field in parsed[0][i+1:]:
            field1 = field1.difference(set(an_field))   
        if len(field1)==1:
          fields[i] = list(field1)[0]
          not_parsed.remove(i)
    
    count = 0   
    for i,f in enumerate(fields):
      if isinstance(f,str) and 'departure' in f:
        count+=1
    
    if count==6:
      res = 1   
      for i,f in enumerate(fields):
        if isinstance(f,str) and 'departure' in f:
          count+=1
          res *= your[i]
      print(res)     
      break     
    

def main():
  lines=[i.strip() for i in re.split(r'\r?\n\r?\n',open('input.txt','r').read())]
  # lines=[i.strip() for i in re.split(r'\r?\n\r?\n',open('input_test.txt','r').read())]
  validation = TicketValidation(re.split(r'\r?\n',lines[0]))
  your = tuple(int(i) for i in re.split(r'\r?\n',lines[1])[1].split(','))
  other = [tuple(int(i) for i in ticket.split(',')) for ticket in re.split(r'\r?\n',lines[2])[1:]]

  solve1(validation,other)
  solve2(validation,other,your)

if __name__ == '__main__':
  main()