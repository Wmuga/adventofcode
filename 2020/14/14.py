import re
from functools import reduce
# TODO make return lists 4 apply to mem
def apply_mask1(value:int,mask:dict[int,int])->int:
  value_bits = list(reversed(bin(value)[2:]))
  value_bits.extend([0 for _ in range(len(value_bits),max(mask.keys())+1)])
  for offset in mask:
    value_bits[offset]=mask[offset]
  return int('0b{}'.format(''.join([str(i) for i in reversed(value_bits)])),2)

def parse_mask(mask:str)->dict[int,int]:
  return {i:int(num) for i,num in enumerate(reversed(list(mask))) if num!='X'}

def set_values(values_bits:str)->int:
  xs = [i for i,b in enumerate(reversed(values_bits)) if b=='X']
  value = list(values_bits.replace('X','0'))
  value = int('0b'+''.join(value),2)
  values = list(value for _ in range(2**len(xs)))
  for x_num,x_pos in enumerate(xs):
    for i,_ in enumerate(values):
      if i%(2**(x_num+1))>=(2**(x_num)):
        values[i]+=2**x_pos
  return values

def apply_mask2(value:int,mask:str)->list[int]:
  value_bits = list(reversed(list(bin(value)[2:])))
  value_bits.extend(['0' for _ in range(len(value_bits),len(mask))])
  value_bits = list(reversed(value_bits))
  value_bits = [vm if vm!='0' else str(vb) for vb,vm in zip(value_bits,mask)]
  return set_values(''.join(value_bits))

def solve1(lines:list[list[str]]):
  mem:dict[int,int] = dict()
  mask:dict[int,int] = dict()
  for line in lines:
    if (line[0]=='mask'):
      mask = parse_mask(line[1])
    else:
      mem[int(line[0][4:-1])] = apply_mask1(int(line[1]),mask) 
  print(sum(mem.values()))

def solve2(lines:list[list[str]]):
  mem:dict[int,list[int]] = dict()
  mask:str = ''
  for line in lines:
    if (line[0]=='mask'):
      mask = line[1]
    else:
      values = apply_mask2(int(line[0][4:-1]),mask) 
      for _, value in enumerate(values):
        mem[value]=int(line[1])
  print(sum(mem.values())) 

lines = [i.strip().split(' = ') for i in open('input.txt','r').readlines()]
# lines = [i.strip().split(' = ') for i in open('input_test.txt','r').readlines()]

solve1(lines)
solve2(lines)  