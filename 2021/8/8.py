from functools import reduce

def unpack(lines:list[str])->tuple[list[list[str]],list[list[str]]]:
  out = list()
  patterns = list()
  for line in lines:
    data = line.split(' | ')
    patterns.append(data[0].split(' '))
    out.append(data[1].split(' '))
  return patterns,out  

def solve1(out:list[list[str]]):
  print(reduce(lambda a,b: a+sum([int(len(i)<5 or len(i)==7) for i in b]),out,0))


def reducer2(prev:int,cur:tuple[list[str],list[str]]):
  d = decode(cur[0])
  return prev+reduce(lambda a,b: a*10+reduce(lambda a1,b1:b1 if set(b)==d[b1] else a1,d.keys()),cur[1],0)


def decode(pattern:list[str])->dict[int,set[str]]:
  d:dict[int,set[str]] = dict()
  pattern = [(len(i),i) for i in pattern]
  patterns_len = {i:[] for i in range(2,8)}

  for pair in pattern:patterns_len[pair[0]].append(set(pair[1]))

  d[1]=patterns_len[2][0]
  d[7]=patterns_len[3][0]
  d[4]=patterns_len[4][0]
  d[8]=patterns_len[7][0]
  # 3 has both lines which are in 1
  d[3] = reduce(lambda a,b: b if d[1].issubset(b) else a,patterns_len[5],patterns_len[5][0])
  patterns_len[5].remove(d[3])
  # 0 hasn't middle line of 3
  lines = d[3].symmetric_difference(d[1])
  d[0] = reduce(lambda a,b: b if len(list(lines.intersection((b))))!=3 else a,patterns_len[6],patterns_len[6][0])
  patterns_len[6].remove(d[0])
  # 9 has all 5 lines of 3 - 6 not
  d[9] = reduce(lambda a,b: b if d[3].issubset(b) else a,patterns_len[6],patterns_len[6][0])
  patterns_len[6].remove(d[9])
  d[6] = patterns_len[6][0]
  # 6^9 has two vertical lines, which are in 2
  verticals = d[6].symmetric_difference(d[9])
  d[2] = reduce(lambda a,b: b if len(list(verticals.intersection((b))))==2 else a,patterns_len[5],patterns_len[5][0])
  patterns_len[5].remove(d[2])
  # The last is 5
  d[5] = patterns_len[5][0]
  return d

def solve2(patterns:list[list[str]],out:list[list[str]]):
  print(reduce(reducer2,zip(patterns,out),0))

# patterns, out = unpack([i.strip() for i in open('input_test.txt','r').readlines()])
patterns, out = unpack([i.strip() for i in open('input.txt','r').readlines()])


solve1(out)
solve2(patterns,out)