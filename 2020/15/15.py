def calc_turn(nums:list[int],end_turn:int)->int:
  d = {num:i for i,num in enumerate(nums[:-1])}
  # print(d)
  last = nums[-1]
  new_last = 0
  for turn in range(len(nums)-1,end_turn-1):
    if last in d:
      new_last = turn-d[last]
    else:
      new_last = 0  
    # print(last,new_last,turn+1)
    d[last]=turn
    last = new_last
  return last  
      

def solve1(nums:list[int]):
  print(calc_turn(nums,2020))

def solve2(nums:list[int]):
  print(calc_turn(nums,30000000))

nums = [int(i.strip()) for i in open('input.txt','r').readline().split(',')]

solve1(nums)
solve2(nums)