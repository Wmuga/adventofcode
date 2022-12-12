def count_incs(nums:list):
  prev = 0
  incs = -1
  for num in nums:
    if num>prev:
      incs+=1
    prev = num
  print(incs)

def three_measurement(nums:list):
  nums2 = list()
  for i in range(len(nums)-2):
    try:
      three_mes = nums[i]+nums[i+1]+nums[i+2]
      nums2.append(three_mes)
    except IndexError:
      break
  return nums2 

nums = [int(i.strip()) for i in open('input.txt','r').readlines()];  
# 1 
#count_incs(nums)
# 2
count_incs(three_measurement(nums))