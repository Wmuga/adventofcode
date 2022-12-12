import re
import copy

class Tree:
  def __init__(self,left:'Tree' = None,right:'Tree' = None, val:str = None):
    self.left:Tree = left
    self.right:Tree = right
    self.val:str = val

# + * ( )
def buildTree(eq:list[str], start:int, isPlus:bool)->tuple[Tree,int]:
  i = start
  nullTerm = Tree(val = '0')
  cur = Tree(nullTerm, nullTerm, '+')
  
  while(i < len(eq)):
    if (eq[i] == '+'):
      if not isPlus:
        cur = Tree(cur, val='+')
      else:
        cur.right = Tree(cur.right, val='+')
        if eq[i+1] == '(':
          cur.right.right, i = buildTree(eq, i+1, isPlus)
        else:
          cur.right.right = Tree(val=eq[i+1])
          i+=1
    elif (eq[i] == '*'):
      cur = Tree(cur, val='*')
    elif (eq[i] == '('):
      cur.right, i = buildTree(eq, i+1, isPlus)
    elif (eq[i] == ')'):
      return cur, i
    else:
      cur.right = Tree(val=eq[i])
    i+=1
  return cur, i

def evalTree(head:Tree)->int:
  if(head.val=='+'):
    return evalTree(head.left) + evalTree(head.right)
  elif(head.val=='*'):
    return evalTree(head.left) * evalTree(head.right)
  else:
    return int(head.val)

def solve1(inp:list[list[str]]):
  res = 0
  for eq in inp:
    tree = buildTree(eq, 0, False)[0]
    res1 = evalTree(tree)
    # print(res1)
    res += res1
  print(f'Solution 1: {res}')

def solve2(inp:list[list[str]]):
  res = 0
  for eq in inp:
    tree = buildTree(eq, 0, True)[0]
    res1 = evalTree(tree)
    # print(res1)
    res += res1
  print(f'Solution 2: {res}')

if __name__ == '__main__':
  inp = [re.split(' *',i) for i in re.split('\r?\n',open('./2020/18/input.txt','r').read())]
  # inp = [re.split(' *',i) for i in re.split('\r?\n',open('./2020/18/input_test.txt','r').read())]

  inp = [list(filter(lambda item: len(item)>0,i)) for i in inp]

  # print(inp)

  solve1(inp)  
  solve2(inp)