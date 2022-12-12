from functools import reduce
def unpack(lines:list[str])->tuple[int,list['int | str']]:
  return int(lines[0]),[int(i) if i!='x' else i for i in lines[1].split(',')]

def solve1(time:int,buses:list['int | str']):
  res = reduce(lambda prev,cur:prev if prev[0]<cur[0] else cur,[((int(time/bus)+1)*bus-time,bus) for bus in buses if bus!='x'],(time,0))
  print(res,res[0]*res[1])

# Stupid and time consufing AF
# def solve2(buses:list['int | str']):
#   longest = max([b for b in buses if b!='x'])
#   offsets:list[tuple[int,int]] = [(bus,i-buses.index(longest)) for i,bus in enumerate(buses) if bus!='x']
#   print(offsets)
#   k = 1
#   while(True):
#     if(reduce(lambda prev,cur: prev and cur,[((longest%offset[0])*(k%offset[0])+offset[1])%offset[0]==0 for offset in offsets],True)):
#       break
#     k+=1
#   print(k,k*longest+offsets[0][1])   

def solve2(buses:list['int | str']):
  # Chinese reminder theorem x = a1 (mod n1) ... x = ak (mod nk) => x = sum(ai*yi*zi) yi = mult(n1...nk)/ni zi = yi**-1 (mod ni)
  x_in_ring:list[int] = [bus-i for i,bus in enumerate(buses) if bus!='x'] # a's
  rings:list[int]= [bus for bus in buses if bus!='x'] # n's
  
  N = reduce(lambda a,b:a*b,rings)
  Y = [int(N/ring) for ring in rings]
  Z = [y**(ring-2)%ring for y,ring in zip(Y,rings)]
  
  print(sum([a*y*z for a,y,z in zip(x_in_ring,Y,Z)])%N)


# time,buses = unpack([i.strip() for i in open('input_test.txt','r').readlines()])
time,buses = unpack([i.strip() for i in open('input.txt','r').readlines()])
solve1(time,buses)
solve2(buses)