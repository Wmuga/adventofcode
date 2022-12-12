from functools import reduce
import re
from copy import deepcopy

def solve1(map):
  print(print(len(map)))

def solve2(map):
  print('Pog')


def check_coords(c1,c2,axis,count):
  deltas = []
  for coord1 in c1:
    for coord2 in c2:
      deltas.append(coord2[axis] - coord1[axis])
  res = (0,0)
  for delta in deltas:
    sum = 0    
    for coord1 in c1:
      for coord2 in c2:
        sum += int((coord2[axis] - coord1[axis])==delta)
    if sum>res[0]:
      res = (sum,delta)     
      if sum>=count:
        # print(res)
        return res   
  # print(res)    
  return res

class Scanner:
  def __init__(self,coords:list[tuple[int,int,int]]):
    self.coords = deepcopy(coords)

  def rotate(self,type:int):
    rot = type//2//8
    corner = type%8
    mapper = lambda a: (a[0],a[1],a[2])
    if corner==0:
      mapper = lambda a: (a[0],a[1],a[2])
    elif corner==1:
      mapper = lambda a: (-a[0],a[1],a[2])
    elif corner==2:
      mapper = lambda a: (-a[0],-a[1],a[2])
    elif corner==3:
      mapper = lambda a: (a[0],-a[1],a[2])
    elif corner==4:
      mapper = lambda a: (a[0],a[1],-a[2])
    elif corner==5:
      mapper = lambda a: (-a[0],a[1],-a[2])
    elif corner==6:
      mapper = lambda a: (-a[0],-a[1],-a[2])
    else:
      mapper = lambda a: (a[0],-a[1],-a[2]) 

    self.coords = list(map(mapper,self.coords))
    self.coords = list(map(lambda a:(a[rot],a[(rot+1)%3],a[(rot+2)%3]),self.coords))  
    if (type//8%2):
      self.coords = list(map(lambda a:(a[0],a[2],a[1]),self.coords))  
      
    

  def overlap(self,other:'Scanner',count:int):
    for type in range(0,48):
      other2 = Scanner(other.coords)
      other2.rotate(type)

      # X axis
      c,delta_x = check_coords(self.coords,other2.coords,0,count)
      if c>=count:  
        # Y axis
        c,delta_y = check_coords(self.coords,other2.coords,1,count)
        if c>=count:  
          # Z axis
          c,delta_z = check_coords(self.coords,other2.coords,2,count)
         
          if c>=count:
            other2.coords = list(map(lambda a: (a[0]+delta_x,a[1]+delta_y,a[2]+delta_z),other2.coords))
            return other2,[delta_x,delta_y,delta_z],type


def apply_offsets(offset:list,scanner:Scanner):
  scanner.rotate(offset[2])
  for i,m in enumerate(offset[1]):
    if m: scanner.swap_dir(i)
  scanner.coords = list(map(lambda a: (a[0]+offset[0][0],a[1]+offset[0][1],a[2]+offset[0][2]),scanner.coords))  

def main():
  # scanners = [[[int(i.strip()) for i in coords.split(',')] for coords in re.split(r'\r?\n',scanner) if coords] for scanner in re.split(r'-+ scanner \d+? -+\r?\n',''.join(open('input.txt','r').readlines()))[1:]]
  scanners = [[[int(i.strip()) for i in coords.split(',')] for coords in re.split(r'\r?\n',scanner) if coords] for scanner in re.split(r'-+ scanner \d+? -+\r?\n',''.join(open('input_test.txt','r').readlines()))[1:]]
 
 
  scanners = [Scanner([(coord[0],coord[1],coord[2]) for coord in s]) for s in scanners]
  offsets = {'0-0':[[0,0,0],[0,0,0],0,0]}

  scanned = [0]

  map = set(scanners[0].coords)

  for i,s1 in enumerate(scanners):   
    for j,s2 in enumerate(scanners):
      if i!=j and j not in scanned:
        print('Scan:',i,j)
        res = s1.overlap(s2,12)
        if res:
          n_s2 = res[0]
          scanned.append(j)
          print(res[1:])
          offsets[f'{j}-{i}'] = res[1:]

  print(scanned)
  print(offsets.keys())
  
  # solve1()
  # solve2()

def test():
  res = set()
  for type in range(48):
    a = Scanner([(1,2,3)])
    a.rotate(type)
    res.add(a.coords[0])
    print(a.coords[0])
  print(len(res))  

if __name__ == '__main__':
  main()
  # test()