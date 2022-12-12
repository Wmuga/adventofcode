import copy

def transpose(bits:list):
  t = [[] for _ in range(len(bits[0]))]
  for bit_line in bits:
    for i in range(len(bits[0])):
      t[i].append(bit_line[i])
  return t

def getBit(bit_line:list,f):
  d = {0:0,1:0}
  for bit in bit_line:
    d[int(bit)]+=1
  if d[0]==d[1]: return str(f(0,1))
  else: return '1' if f(d[0],d[1]) == d[1] else '0'

def getBits(bits:list,f):
  res = []
  for bit_line in bits:
    res.append(getBit(bit_line,f))
  return '0b'+''.join(res) 

def solve1(bits:list):
  gamma_rate = getBits(bits,max)
  eps_rate = getBits(bits,min)
  print(gamma_rate,eps_rate,int(gamma_rate,2)*int(eps_rate,2))

def extract_bits(bits:list,f):
  rate = copy.deepcopy(bits)
  num = 0
  while len(rate)>1:
    common = getBit(transpose(rate)[num],f)
    rate = [i for i in rate if i[num]==common]
    num += 1 
  return rate[0]  

def solve2(bits:list):
  o2rate = '0b'+''.join(extract_bits(bits,max))
  co2rate = '0b'+''.join(extract_bits(bits,min))
  print(o2rate,co2rate,int(o2rate,2)*int(co2rate,2))
  

bits = [list(i.strip()) for i in open('input.txt','r').readlines()]
# 1
# solve1(transpose(bits))
solve2(bits)


