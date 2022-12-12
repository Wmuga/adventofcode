from copy import deepcopy

class Point:
  def __init__(self,p:list[int]):
    self.x:float = p[0]
    self.y:float = p[1]

  def get_vector(self,end:'Point') -> 'Point':
    return Point([end.x-self.x,end.y-self.y])

  def __str__(self) -> str:
    return '({}, {})'.format(self.x,self.y)  

class Line:
  def __init__(self,line:str):
    p1,p2 = line.split(' -> ')
    self.start:Point = Point([int(i) for i in p1.split(',')])
    self.end:Point = Point([int(i) for i in p2.split(',')])

  def __str__(self) -> str:
    return '{} -> {}'.format(str(self.start),str(self.end))

  def get_points(self) -> list[Point]:
    points:list[Point] = list()
    v = self.start.get_vector(self.end)

    step_x = v.x/abs(v.x) if v.x!=0 else 0.0
    step_y = v.y/abs(v.x) if v.x!=0 else (v.y/abs(v.y) if v.y!=0 else 0.0)

    for i in range((abs(v.x) if v.x!=0 else abs(v.y)) + 1):
      points.append(Point([int(self.start.x + step_x*i),int(self.start.y + step_y*i)]))

    return points   

class Field:
  def __init__(self,lines:list[Line]):
      self.lines:list[Line] = lines
      self.field:list[list[int]] = list()

  def generate_field(self,ignoreDiagonals:bool) -> None:
    max_x = max(max([line.start.x for line in self.lines]),max([line.end.x for line in self.lines]))+1
    max_y = max(max([line.start.y for line in self.lines]),max([line.end.y for line in self.lines]))+1
    for _ in range(max_x):
      self.field.append([0 for _ in range(max_y)])

    for line in self.lines:
      if ignoreDiagonals and line.start.x != line.end.x and line.start.y != line.end.y:
        continue
      
      for point in line.get_points():
        self.field[point.x][point.y]+=1

  def count_intersections(self) -> int:
    count = 0
    for row in self.field:
      for cell in row:
        count+=int(cell>1)
    return count  



def unpack_lines(in_lines:list[str]) -> Field:
  lines:list[Line] = list()
  for line in in_lines:
    lines.append(Line(line))
  return Field(lines)


def solve1(field:Field):
  new_field = deepcopy(field)
  new_field.generate_field(True)
  print(new_field.count_intersections())

def solve2(field:Field):
  new_field = deepcopy(field)
  new_field.generate_field(False)
  print(new_field.count_intersections())

field = unpack_lines([i.strip() for i in open('input.txt','r').readlines()])


solve1(field)
solve2(field)