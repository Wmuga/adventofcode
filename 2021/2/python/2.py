def calc_path(lines:list):
  hor,depth = 0,0
  for line in lines:
    path = line.split(' ')
    if (path[0]=='forward'):
      hor+=int(path[1])
    if (path[0]=='down'):
      depth+=int(path[1])
    if (path[0]=='up'):
      depth-=int(path[1])
  print(hor,depth,hor*depth)

def calc_path2(lines:list):
  hor,depth = 0,0
  aim = 0
  for line in lines:
    path = line.split(' ')
    if (path[0]=='forward'):
      hor+=int(path[1])
      depth+=aim*int(path[1])
    if (path[0]=='down'):
      aim+=int(path[1])
    if (path[0]=='up'):
      aim-=int(path[1])
  print(hor,depth,hor*depth)  

lines = [i.strip() for i in open('input.txt','r').readlines()]
# 1
# calc_path(lines)
# 2
calc_path2(lines)