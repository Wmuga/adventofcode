import re

def convertToBinary(line:str):
  line = re.sub(r'F|L','0',line)
  line = re.sub(r'B|R','1',line)
  return '0b'+line


def solve1(seatIds:list):
  print(max(seatIds))

def solve2(seatIds:list):
  for i in range(min(seatIds),max(seatIds)):
    if i not in seatIds:
      print(i)
      break

seatIds = [int(convertToBinary(i.strip()),2) for i in open('input.txt','r').readlines()]

solve1(seatIds)
solve2(seatIds)