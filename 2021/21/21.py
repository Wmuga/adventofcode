from functools import lru_cache

def solve1(pos:list):
  pos1 = list(pos)
  scores = [0,0]
  dice = 1
  p = 0
  i = 0
  while(scores[0]<1000 and scores[1]<1000):
    pos1[p] = (pos1[p] + 3*dice+3)% 10 or 10 
    scores[p] += pos1[p]
    dice+=3
    p = (p+1)%2
    i+=3
  print(i*min(scores))

# throws = [3,4,5,6,7,8,9]
# d6 test
throws = list(range(3,6*3+1))
possibs = [0 for i in range(len(throws))]

def calc_pos(max):
  for c1 in range(1,max+1):
    for c2 in range(1,max+1):
      for c3 in range(1,max+1):
        possibs[c1+c2+c3-3]+=1

@lru_cache(None)
def count_wins(pos:tuple[int,int],scores:tuple[int,int],p):
  wins = [0,0]
  for throw,possib in zip(throws,possibs):
    cur_pos = list(pos)
    cur_scores = list(scores)
    cur_pos[p] = (cur_pos[p]+throw)%10 or 10
    cur_scores[p] += cur_pos[p]
    if cur_scores[p]>=21:
      wins[p]+=possib
    else:
      res = count_wins(tuple(cur_pos),tuple(cur_scores),(p+1)%2)
      wins[0]+=possib*res[0]  
      wins[1]+=possib*res[1]  

  return wins  

def solve2(pos):
  print(max(count_wins(tuple(pos),(0,0),0)))

def main():
  pos = [int(i.split(':')[1].strip()) for i in open('input.txt').readlines()]
  # pos = [int(i.split(':')[1].strip()) for i in open('input_test.txt').readlines()]
  solve1(pos)
  calc_pos(6)
  solve2(pos)

if __name__ == '__main__':
  main()


  