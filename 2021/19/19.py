import re
from copy import deepcopy
from functools import reduce

def solve1(map):
  print(print(len(map)))

def solve2():
  print('Pog')

def overlap(scanner1:list[list[int]],scanner2:list[list[int]],overlap_count:int):
  for i in range(6):
    i1 = i%3
    i2 = (i+1+i%2)%3
    i3 = 3 - i1 - i2
    scanner2_temp1 = list(map(lambda a:(a[i1],a[i2],a[i3]),deepcopy(scanner2)))

    for j in range(8):
      scanner2_temp2 = list(map(lambda a:(a[0] if j%2==0 else -a[0],a[1] if j//2%2==0 else -a[1],a[2] if j//4%2==0 else -a[2]),deepcopy(scanner2_temp1)))
      
      x_range = max(scanner1)[0]-min(scanner2_temp2)[0]
      y_range = max(scanner1,key=lambda i: i[1])[1] - min(scanner2_temp2,key=lambda i: i[1])[1]
      z_range = max(scanner1,key=lambda i: i[2])[2] - min(scanner2_temp2,key=lambda i: i[2])[2]

      for x_offset in range(-x_range,x_range+1):
        for y_offset in range(-y_range,y_range+1):
          for z_offset in range(-z_range,z_range+1):
            scanner2_temp = list(map(lambda e: (e[0]+x_offset,e[1]+y_offset,e[2]+z_offset),deepcopy(scanner2_temp2))) # trying moving
            counts = len(set(scanner1).intersection(set(scanner2_temp)))
            if counts >= overlap_count:
              return scanner2_temp,[x_offset,y_offset,z_offset],[i1,i2,i3]

def apply_offset(offset,coords):
  return list(map(lambda a:(a[offset[1][0]]+offset[0][0],a[offset[1][1]]+offset[0][1],a[offset[1][2]]+offset[0][2]),coords))

def main():
  # scanners = [[[int(i.strip()) for i in coords.split(',')] for coords in re.split(r'\r?\n',scanner) if coords] for scanner in re.split(r'-+ scanner \d+? -+\r?\n',''.join(open('input.txt','r').readlines()))[1:]]
  scanners = [[[int(i.strip()) for i in coords.split(',')] for coords in re.split(r'\r?\n',scanner) if coords] for scanner in re.split(r'-+ scanner \d+? -+\r?\n',''.join(open('input_test.txt','r').readlines()))[1:]]
  
  scanners = [[(coord[0],coord[1],coord[2]) for coord in s] for s in scanners]
  cur_map = set(scanners[0])
  
  checked_scanners = [0]

  offsets = {'0-0':[[0,0,0],[0,1,2]]}

  for i,scanner1 in enumerate(scanners[:1]):
    for j,scanner2 in enumerate(scanners[i+1:],start=1):
      if j not in checked_scanners:
        res = overlap(scanner1,scanner2,12)
        if res:
          offsets['{}-{}'.format(j,i)] = [res[1],res[2]]
          res = apply_offset(offsets['{}-0'.format(i)],res[0])
          cur_map = cur_map.union(set(res))
          checked_scanners.append(j)

      if len(checked_scanners)==len(scanners):
        break      
    if len(checked_scanners)==len(scanners):
      break    
  print(cur_map)
  
  solve1(cur_map)
  solve2()

if __name__ == '__main__':
  main()