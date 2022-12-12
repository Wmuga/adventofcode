import re

cache = {}

def solve1(rules:list[str],messages:list[str]):
  cache = {}
  
  parsedRules = parseRules(rules)
  print('Parsed rules for 1')
  
  possibleMessages = createPossibles(parsedRules, 0, cache, 0)
  print('Parsed messages for 1')
  
  messCount = 0
  for message in messages:
    messCount += int(message in possibleMessages)

  print(f'Solution 1: {messCount}')

def solve2(rules:list[str],messages:list[str]):
  cache = {}
  
  parsedRules = parseRules(rules)
  parsedRules['8'].append(['42','8'])
  parsedRules['11'].append(['42','11','31'])
  print('Parsed rules for 2')
  
  possibleMessages = createPossibles(parsedRules, 0, cache, 0)
  print('Parsed messages for 2')
  
  messCount = 0
  
  for message in messages:
    messCount += int(message in possibleMessages)
  
  print(f'Solution 2: {messCount}')

def parseRules(rules:list[str])->dict[str, list[list[str]]]:
  d = dict()
  for rule in rules:
    key, s = rule.split(': ')
    options = [[''.join(j.split('"'))for j in i.split(' ')] for i in s.split(' | ')]
    d[key] = options
  return d

def createPossibles(parsedRules:dict[str, list[list[str]]], rule:int, cache:dict[str, list[str]], same:int)->list[str] | None:
  if (rule in cache): 
    return cache[rule]
  
  poss = list()
 
  for possib in parsedRules[str(rule)]:
    poss1 = list()
    for rule1 in possib:
      if (rule1 == str(rule) and same==10):
        poss1 = list()
        break

      try:
        rule1 = int(rule1)
        poss1.append(createPossibles(parsedRules, rule1, cache, same+1 if rule==rule1 else 0))
      except:
        poss1.append(rule1)
    
    strs = list()
    combineStrs(poss1, 0, '', strs)
    for s in strs:
      poss.append(s) 
  

  if (rule != 0): 
    cache[rule] = poss

  return poss

def combineStrs(strVars:list[list[str]],index:int, startStr:str, strs:list[str]):
  if (index == len(strVars)):
    strs.append(startStr)
    return
  for curStr in strVars[index]:
    combineStrs(strVars,index+1, startStr+curStr, strs)

if __name__ == '__main__':
  # inp = re.split('\r?\n\r?\n',open('./2020/19/input.txt','r').read())
  inp = re.split('\r?\n\r?\n',open('./2020/19/input_test.txt','r').read())

  rules = re.split('\r?\n',inp[0])
  messages = re.split('\r?\n',inp[1])

  solve1(rules, messages)  
  solve2(rules, messages)