from functools import reduce

def unpack(lines:list):
  nums = [int(i) for i in lines[0].split(',')]

  boards = list()
  board = list()
  for line in lines[2:]:
    if len(line)==0:
      boards.append(board)
      board = list()
      continue
    
    board.append([int(i) for i in line.split(' ') if len(i)>0])

  if len(board)>0:
    boards.append(board)

  return nums,boards    

def check_row(nums:list,row:list):
  for num in row:
    if num not in nums:
      return False
  return True        

def check_column(nums:list,board:list,column_num:int):
  for i in range(len(board)):
    if board[i][column_num] not in nums:
      return False
  return True

def calc_rest(nums:list,board:list):
  res = 0
  for line in board:
    for num in line:
      if num not in nums:
        res+=num
  return res

def calc_board(nums:list,board:list):
  for i, num in enumerate(nums):
    for line_num,line in enumerate(board):
      if check_row(nums[:i+1],line) or check_column(nums[:i+1],board,line_num):
        return i+1,calc_rest(nums[:i+1],board)*num

def calc_boards(nums:list,boards:list,reducer,start:tuple):
  res = reduce(reducer,
  [calc_board(nums,board) for board in boards],
  start)
  return res


def solve1(nums:list,boards:list):
  res = calc_boards(nums,boards,lambda prev,cur: cur if prev[0]>cur[0] else prev,(len(nums),1))
  print(res)

def solve2(nums:list,boards:list):
  res = calc_boards(nums,boards,lambda prev,cur: cur if prev[0]<cur[0] else prev,(0,1))
  print(res)


lines = [i.strip() for i in open('input.txt','r').readlines()]
nums, boards = unpack(lines)

solve1(nums,boards)
solve2(nums,boards)