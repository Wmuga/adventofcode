import copy

class Operand:
  def __init__(self,line:str):
    data = line.split(' ')
    self.opType:str = data[0]
    self.opValue:int = int(data[1])
    self.visited:bool = False
  def __str__(self):
    return '{} {} {}'.format(self.opType,self.opValue,self.visited)  

class Program:
  def __init__(self,lines:list[str]):

    self.operands:list[Operand] = list()
    self.currentOperand:int = 0
    self.acc:int = 0
    self.term:bool = False

    for line in lines:
      self.operands.append(Operand(line))

  def __str__(self):
    return ', '.join([str(i) for i in self.operands])
  
  def getOperand(self):
    try:
      return self.operands[self.currentOperand]
    except IndexError:
      print(self.currentOperand,self.term)
      op = Operand("nop 0 ")
      op.visited = True
      return op  

  def next(self):
    self.getOperand().visited = True 

    if self.getOperand().opType=="acc":
      self.acc += self.getOperand().opValue

    elif self.getOperand().opType=="jmp":
      self.currentOperand+=self.getOperand().opValue-1
    
    self.currentOperand+=1

    if self.currentOperand>=len(self.operands):
      self.term = True
    
    return self.term or self.getOperand().visited

  def reset(self):
    def mf(x:Operand):
      x.visited = False
      return x 

    self.operands = list(map(mf,self.operands))
    self.currentOperand = 0
    self.acc = 0
    self.term = False
    

def solve1(lines:list[str]):
  prog = Program(lines)
  while(not prog.next()):
    pass
  print(prog.acc)

def reverse_op(op:Operand):
  new_op = copy.copy(op)
  if new_op.opType == "nop":
    new_op.opType = "jmp"
  elif new_op.opType == "jmp":
    new_op.opType = "nop"
  return new_op  

def solve2(lines:list[str]):
  prog = Program(lines)
  i = -1
  while(not prog.term):
    for i,op in enumerate(prog.operands[i+1:],start=i+1):
      if op.opType == "nop" or op.opType=="jmp":
        prog.operands[i]=reverse_op(op)
        break
    while(not prog.next()):
      pass
    if (not prog.term):
      prog.operands[i] = reverse_op(prog.operands[i])
      prog.reset()
  print(prog.acc)

lines = [i.strip() for i in open('input.txt','r').readlines()]

solve1(lines)
solve2(lines)