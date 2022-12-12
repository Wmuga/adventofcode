import re

def solve1(rules:list[str],messages:list[str]):
  messCount = 0
  parsedRules = parseRules(rules)
  
  for message in messages:
    res = checkMessage(parsedRules, 0, message, 0)
    print(res)
    res = list(filter(lambda val: val[0]==True,res))
    messCount+=len(res)
  
  print(f'Solution 1: {messCount}')


def solve2(rules:list[str],messages:list[str]):
  messCount = 0
  
  parsedRules = parseRules(rules)
  parsedRules['8'].append(['42','8'])
  parsedRules['11'].append(['42','11','31'])
  
  for message in messages:
    res = checkMessage(parsedRules, 0, message, 0)
    print(res)
    res = list(filter(lambda val: val[0]==True,res))
    messCount+=len(res)
  
  print(f'Solution 2: {messCount}')

def parseRules(rules:list[str])->dict[str, list[list[str]]]:
  d = dict()
  for rule in rules:
    key, s = rule.split(': ')
    options = [[''.join(j.split('"'))for j in i.split(' ')] for i in s.split(' | ')]
    d[key] = options
  return d

# м.б list[tuple[bool, int]]???? Типа False - только один эл-т, Или много True
def checkMessage(parsedRules:dict[str,list[list[str]]], curRule:int, message:str, index:int)->list[tuple[bool,int]]:
  res = []

  if (index >= len(message)): 
    return (False, index)
  
  for possib in parsedRules[str(curRule)]:
    possibRes = False
    indeces = [(True,index)]
    
    for rule in possib:
      newIndeces = []
      possibResIndex = False
      
      for _,index1 in indeces:    
        try:
          indeces1 = checkMessage(parsedRules, int(rule), message, index1)
          indeces1 = list(filter(lambda el: el[0]==True, indeces1))
          possibResIndex = len(indeces1)>0
          newIndeces+=indeces1
        except:
          possibResIndex = message[index1]==rule
          if possibResIndex:
            newIndeces.append((possibResIndex, index1+1))

      if possibResIndex:
        possibRes = True    
        indeces = newIndeces
      else:
        possibRes = False
      
    
    if possibRes:
      res += indeces

  if (curRule == 0):
    res = list(filter(lambda val: val[1]==index,res))
  
  return res if len(res) else [(False, index)]



if __name__ == '__main__':
  inp = re.split('\r?\n\r?\n',open('./2020/19/input_test.txt','r').read())
  # inp = re.split('\r?\n\r?\n',open('./2020/19/input.txt','r').read())

  rules = re.split('\r?\n',inp[0])
  messages = re.split('\r?\n',inp[1])

  # solve1(rules, messages)  
  solve1(rules, messages)  
  solve2(rules, messages)