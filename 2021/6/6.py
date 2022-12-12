class Pool:
  def __init__(self,timers:list[int],fish_init:int,new_fish_init:int)->None:
    self.fish_init:int = fish_init
    self.new_fish_init:int = new_fish_init
    self.fishes:dict[int,int] = dict()
    for day in range(self.new_fish_init+2):
      self.fishes[day]=0
    for timer in timers:
      self.fishes[timer]+=1

  def simulate(self,days:int)->int:
    for _ in range(days):
      new_fishes = self.fishes[0]
      for i in range(1,self.new_fish_init+1): self.fishes[i-1]=self.fishes[i]
      self.fishes[self.new_fish_init] = new_fishes    
      self.fishes[self.fish_init] += new_fishes    
    return sum([self.fishes[key] for key in self.fishes])

def solve1(inp:list[int]):
  pool = Pool(inp,6,8)
  print(pool.simulate(80))

def solve2(inp:list[int]):
  pool = Pool(inp,6,8)
  print(pool.simulate(256))

pool = [int(i) for i in open('input.txt','r').readline().split(',')]

solve1(pool)  
solve2(pool)