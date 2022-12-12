from functools import reduce

def decode(word):
  try:
    v = int(word[:3],2)
    id = int(word[3:6],2)
    word = word[6:]
    content = ''
    res = [0]
    if id==4:
      leadbit = 1
      while leadbit:
        temp = word[:5]
        word = word[5:]
        leadbit = int(temp[0])
        content = '{}{}'.format(content,temp[1:])
      content = int(content,2)  
    else:
      content = list()
      lengthId = int(word[0])
      if not lengthId:
        length = int(word[1:16],2)
        res = decode(word[16:16+length])
        while(res):
          content.append(res[:-1])
          res = decode(res[-1])
        word = word[16+length:]
      else:
        count = int(word[1:12],2)
        res = decode(word[12:])
        content.append(res[:-1])
        word = res[-1]
        try:
          for _ in range(1,count):
            res = decode(word)
            word = res[-1]
            content.append(res[:-1])
        except TypeError as e:
          print(e.args)
          print(word,content,count)
          exit()    
    return [v,id,content, word]  
  
  except ValueError:
    return None  


def id_counter(res):
  sum = res[0]
  if isinstance(res[2],int):
    return sum
  else:
    for subp in res[2]:
      sum += id_counter(subp)
  return sum      

def eval(res)->int:
  # try:
    if res[1]==0:
      return eval(res[2][0]) if len(res[2])==1 else reduce(lambda a,b: a+eval(b), res[2],0)
    if res[1]==1:
      return eval(res[2][0]) if len(res[2])==1 else reduce(lambda a,b: a*eval(b), res[2],1)
    if res[1]==2:
      return eval(res[2][0]) if len(res[2])==1 else reduce(lambda a,b: min(a,eval(b)), res[2],99999999999)
    if res[1]==3:
      return eval(res[2][0]) if len(res[2])==1 else reduce(lambda a,b: max(a,eval(b)), res[2],1)
    if res[1]==4:
      return res[2]
    if res[1]==5:
      return int(eval(res[2][0])>eval(res[2][1]))
    if res[1]==6:
      return int(eval(res[2][0])<eval(res[2][1]))
    if res[1]==7:
     return int(eval(res[2][0])==eval(res[2][1]))
  # except IndexError as e:
    # print(e)
    # print(res)
    # exit()   

def solve1(word:str):
  w1 = str(word)
  res = decode(w1)
  print(res)
  print('1:',id_counter(res))

def solve2(word:str):
  res = decode(word)
  # print(res)
  print('2:',eval(res))

def hextobin(word:list[str]):
  d = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
  }
  return ''.join(list(map(lambda a: d[a],word)))

# word = hextobin(list(open('input.txt','r').readline().strip()))
word = hextobin(list(open('input_test.txt','r').readline().strip()))

solve1(word)
solve2(word)