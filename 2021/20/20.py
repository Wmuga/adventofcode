from copy import deepcopy
from functools import reduce
import re
class img:
  def __init__(self,sheet:list[str],field:list[str]) -> None:
    self.sheet = sheet
    self.field = field
    self.padding = 0

  def draw(self):
    # out = open('out.txt','w')
    for line in self.field[self.padding:-self.padding]:
      # out.write(line[self.padding:-self.padding]+'\n')
      print(line[self.padding:-self.padding])
    
  def count(self):
    return reduce(lambda a,b:a+len(re.findall('#',b[self.padding:-self.padding])),self.field[self.padding:-self.padding],0)

  def step(self,count):
    field = []
    self.padding = count+1

    for i in range(count+self.padding):
      field.append('.'*(len(self.field[0])+(count+self.padding)*2))
    padding = '.'*(count+self.padding)  
    for line in self.field:
      field.append(f'{padding}{line}{padding}')
    for i in range(count+self.padding):
      field.append('.'*(len(self.field[0])+(count+self.padding)*2))
    
    for i in range(count):
      field1 = [list(i) for i in field]
      for i,line in enumerate(field[1:-1]):
        for j,_ in enumerate(line[1:-1]):
          bits = []
          for i1 in range(i-1,i+2):
            for j1 in range(j-1,j+2):
              bits.append('1' if field[i1][j1]=='#' else '0')    
            field1[i][j] = self.sheet[int(''.join(bits),2)]      

      field = list(''.join(i) for i in field1)
    
    self.field = field  


def solve1(image:img):
  image1 = deepcopy(image)
  image1.step(2)
  image1.draw()
  print(image1.count())

def solve2(image:img):
  image.step(50)
  image.draw()
  print(image.count())  

def main():
  lines = [i.strip() for i in open('input.txt','r').readlines()]
  # lines = [i.strip() for i in open('input_test.txt','r').readlines()]
  
  sheet = lines[0]
  lines = lines[2:]

  image = img(sheet,lines) 
  solve1(image)
  solve2(image)

  pass
if __name__ == '__main__':
  main()