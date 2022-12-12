from audioop import mul
import re

specialRules = ['8','11']

def solve1(rules:list[str],messages:list[str]):
  messCount = 0
  parsedRules = parseRules(rules)
  
  rePattern = re.compile(createRegexPattern(parsedRules, 0))
  for message in messages:
    messCount += int(rePattern.match(message)!=None)
  
  print(f'Solution 1: {messCount}')


def solve2(rules:list[str],messages:list[str]):
  messCount = 0
  
  parsedRules = parseRules(rules)
  parsedRules['8'].append(['42','8'])
  parsedRules['11'].append(['42','11','31'])

  rePattern = re.compile(createRegexPattern(parsedRules, 0))
  for message in messages:
    messCount += int(rePattern.match(message)!=None)
  
  print(f'Solution 2: {messCount}')

def parseRules(rules:list[str])->dict[str, list[list[str]]]:
  d = dict()
  for rule in rules:
    key, s = rule.split(': ')
    options = [[''.join(j.split('"'))for j in i.split(' ')] for i in s.split(' | ')]
    d[key] = options
  return d

def createRegexPattern(parsedRules:dict[str, list[list[str]]], curRule:int)->str:  
  possibRegx = []
  
  for possib in parsedRules[str(curRule)]:
    curReg = ''
    mult = []
    addPlus = False
    
    for rule in possib:
      try:
        if int(rule)==curRule:
          if (rule==specialRules[0]):
            curReg+='+'
          else:
            mult = [curReg]
            curReg = ''
            addPlus = True
        else: 
          curReg+=createRegexPattern(parsedRules,int(rule))      
      
      except:
        curReg+=rule
      
    if addPlus:
      mult.append(curReg)
      vars =[]
      for i in range(2,10):
        c = '{'+str(i)+'}'
        vars.append('('+ mult[0]+ c + mult[1] + c + ')')
      
      curReg = '|'.join(vars)

    possibRegx.append(curReg)

  res = f'({"|".join(possibRegx)})'
  
  if curRule==0:
    res = f'^{res}$'
  
  return res


if __name__ == '__main__':
  inp = re.split('\r?\n\r?\n',open('./2020/19/input_test.txt','r').read())
  inp = re.split('\r?\n\r?\n',open('./2020/19/input.txt','r').read())

  rules = re.split('\r?\n',inp[0])
  messages = re.split('\r?\n',inp[1])

  # solve1(rules, messages)  
  solve1(rules, messages)  
  solve2(rules, messages)