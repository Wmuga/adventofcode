import ast

class SnailNumber:
  def __init__(self,line:list['int|SnailNumber'],nest:int,parent:'SnailNumber|None')->None:
    self.left = 0
    self.right = 0
    self.nest = nest
    
    self.parent = parent

    if (isinstance(line[0],list)):
      self.left = SnailNumber(line[0],nest+1,self)
    else:
      self.left = line[0]
    if (isinstance(line[1],list)):
      self.right = SnailNumber(line[1],nest+1,self)
    else:
      self.right = line[1]  

  def __str__(self)->str:
    return '[{}, {}]'.format(str(self.left),str(self.right))     

  def _repr__(self)->str:
      return '[{}, {}]'.format(self.left,self.right)

  def tryExplode(self)->bool:
    if self.nest==4 and isinstance(self.left,int) and isinstance(self.right,int):

      self.parent.addLeft(self.left,self)
      self.parent.addRight(self.right,self)
      self.parent.setZero(self)
      return True

    else: 
      isExpl = False
      if isinstance(self.left,SnailNumber):
        isExpl = self.left.tryExplode()
      
      if not isExpl and isinstance(self.right,SnailNumber):
        isExpl = self.right.tryExplode()

      return isExpl  

  def setZero(self,fr):
    if fr==self.left:
      self.left = 0
    else:
      self.right= 0   

  def addLeft(self,num:int,fr:'SnailNumber'):
    if (fr==self.left):
      if (self.parent):
        self.parent.addLeft(num,self)

    elif fr==self.right:
      if isinstance(self.left,int):
        self.left+=num
      else:
        self.left.addLeft(num,self) 
    else:
      if isinstance(self.right,int):
        self.right+=num
        return
      else:
        self.right.addLeft(num,self)  

  def addRight(self,num:int,fr:'SnailNumber'):
    if (fr==self.right):
      if (self.parent):
        self.parent.addRight(num,self)
    elif fr==self.left:
      if isinstance(self.right,int):
        self.right+=num
      else:
        self.right.addRight(num,self) 
    else:
      if isinstance(self.left,int):
        self.left+=num
        return
      else:
        self.left.addRight(num,self)      

  def trySplit(self):
    if isinstance(self.left,int):
      if self.left>9:
        self.left = SnailNumber([self.left//2,self.left-self.left//2],self.nest+1,self)
        return True
    else:
      if (self.left.trySplit()):
        return True

    if isinstance(self.right,int):
      if self.right>9:
        self.right = SnailNumber([self.right//2,self.right-self.right//2],self.nest+1,self)
        return True
    else:
      if (self.right.trySplit()):
        return True    
    return False      

  def eval(self):
    return 3*(self.left if isinstance(self.left,int) else self.left.eval()) + 2*(self.right if isinstance(self.right,int) else self.right.eval())




def cut(res:SnailNumber):
  while(True):
    f = res.tryExplode()
    if not f:
      f = res.trySplit()
    if not f:
      break 
  return res  

def solve1(nums:list[SnailNumber]):
  res = SnailNumber(nums[0],0,None)
  for num in nums[1:]:
    l = [ast.literal_eval(str(res)),num]
    res = SnailNumber(l,0,None)
    res = cut(res)

  print('1:', res.eval())

def solve2(nums:list[SnailNumber]):
  m = 0
  for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
      res = SnailNumber([nums[i],nums[j]],0,None)
      res = cut(res)
      m = max(m,res.eval()) 
      res = SnailNumber([nums[j],nums[i]],0,None)
      res = cut(res)
      m = max(m,res.eval())
  print('2:',m)    


nums = [ast.literal_eval(i.strip()) for i in open('input.txt','r').readlines()]
# nums = [ast.literal_eval(i.strip()) for i in open('input_test.txt','r').readlines()]

solve1(nums)
solve2(nums)