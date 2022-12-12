from copy import deepcopy
from functools import reduce

class Field3d:
  def __init__(self,lines:list):
    self.size = len(lines)
    self.field = [lines]

  def print_field(self):
    for layer in range(len(self.field)):
      print(f'{layer=}')
      self.print_layer(layer)

  def print_layer(self,z:int):
    for i in range(len(self.field[z])):
      print(''.join(self.field[z][i]))
  
  def count_nearby(self,x:int,y:int,z:int):
    s=0
    for x1 in range(x-1,x+2):
      for y1 in range(y-1,y+2):
        for z1 in range(z-1,z+2):
          try:
            if x1>=0 and y1>=0 and z1>=0 and not(x==x1 and y==y1 and z==z1) and self.field[z1][y1][x1]=='#':
              s+=1
          except IndexError:
            pass    
    return s  

  def count(self):
    return reduce(lambda a,b: a+reduce(lambda a1,b1:a1+reduce(lambda a2,b2:a2+(1 if b2=='#' else 0),b1,0),b,0),self.field,0)

  def iterate(self,steps:int):
    # init_size = self.size
    self.steps = steps
    for _ in range(steps+1):
      for i in range(self.size):
        self.field[0][i].insert(0,'.')
        self.field[0][i].append('.')
    
    self.size += steps+1

    for _ in range(steps+1):
      self.field[0].insert(0,['.' for _ in range(self.size+steps+1)])
      self.field[0].append(['.' for _ in range(self.size+steps+1)])  
      

    for _ in range(steps+1):
      self.field.insert(0,[['.' for _ in range(self.size+steps+1)] for _ in range(self.size+steps+1)])
      self.field.append([['.' for _ in range(self.size+steps+1)] for _ in range(self.size+steps+1)])  

    try:
      for step in range(steps):
        field1 = deepcopy(self.field)
        for z in range(len(self.field)):
          for y in range(len(self.field[z])):
            for x in range(len(self.field[z][y])):
              c = self.count_nearby(x,y,z)
              print(f'{step=} {x=} {y=} {z=} {c=} {self.field[z][y][x]}',end='\r')
              if c==3 and self.field[z][y][x]=='.':
                field1[z][y][x]='#'
              if self.field[z][y][x]=='#' and not(c==3 or c==2):
                field1[z][y][x]='.'
        self.field = deepcopy(field1)   
    except IndexError:
      print(f'\n{x=} {y=} {z=}')   
      self.print_layer(z) 
    print(f'========Completed {steps} steps========')           

def solve1(field:Field3d):
  field.iterate(6)
  print(field.count())

# def solve2(field:Field3d):
#   print('Pog')

def main():
  lines=[list(i.strip())  for i in open('input.txt','r').readlines()]
  # lines=[list(i.strip()) for i in open('input_test.txt','r').readlines()]
  field3d = Field3d(lines)
  solve1(field3d)
  # solve2(field3d)

if __name__ == '__main__':
  main()