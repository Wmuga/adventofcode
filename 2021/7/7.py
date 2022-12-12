from functools import reduce


def calc_fuel(nums:list[int],fuel_burn):
  return reduce(lambda prev,cur:
  (lambda a,b:a if a[0]<b[0] else b)
  (prev,
    (lambda x: (sum([x[j][0] for j in range(len(x))]),x[0][1]))
    ([(fuel_burn(abs(cur-i)),cur) for i in nums])
  )
  ,range(max(nums)),(999999999,0))

def solve1(nums:list[int]):
  print(calc_fuel(nums,lambda x: x))

def solve2(nums:list[int]):
  print(calc_fuel(nums,lambda x: (x+1)*x/2)) #sum(range(x+1)


nums = [int(i.strip()) for i in open('input.txt','r').readline().split(',')]

print('Answer, position:')
solve1(nums)
solve2(nums)