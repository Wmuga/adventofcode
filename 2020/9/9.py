def check_nums(nums:list[int]):
  for num in nums:
    if nums[-1]-num in nums:
      return True
  return False


def get_wrong(nums:list[int]):
  for i in range(len(nums)-26):
    if not check_nums(nums[i:i+26]):
      return nums[i+25]

def get_terms(nums:list[int],target:int):
  for start in range(len(nums)-1):
    current_sum = 0
    i = start
    while(current_sum<target):
      current_sum+=nums[i]
      i+=1
    if(current_sum==target):
      return nums[start:i]  

def solve1(nums:list[int]):
  print(get_wrong(nums))

def solve2(nums:list[int]):
  wrong_num = get_wrong(nums)
  terms = get_terms(nums,wrong_num)
  print(min(terms)+max(terms))  

nums = [int(i.strip()) for i in open('input.txt','r').readlines()]

solve1(nums)
solve2(nums)