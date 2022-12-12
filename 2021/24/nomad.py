from parsed_inp import *

def make_key(state:list[int],num:int , block:int):
  try:
    # x, w aren't changing states
    return ' '.join([str(c) for c in [state[2],state[3]]] + [str(num), str(block)])
  except:
    print(num, block)
    exit(1)

def monad():
  cache = {}

  for i0 in range(9,0,-1):
    state = [0,0,0,0]

    key = make_key(state,i0,0)
    if key in cache:
      state1 = cache[key]
    else:
      x,y,z,w = state
      state1 = monad0(i0,x,y,z,w)
      cache[key] = state1

    for i1 in range(9,0,-1):
      key = make_key(state1,i1,1)
      if key in cache:
        state2 = cache[key]
      else:
        x,y,z,w = state1
        state2 = monad1(i1,x,y,z,w)
        cache[key] = state2

      for i2 in range(9,0,-1):
        key = make_key(state2,i2,2)
        if key in cache:
          state3 = cache[key]
        else:
          x,y,z,w = state2
          state3 = monad2(i2,x,y,z,w)
          cache[key] = state3
          
        for i3 in range(9,0,-1):
          key = make_key(state3,i3,3)
          if key in cache:
            state4 = cache[key]
          else:
            x,y,z,w = state3
            state4 = monad3(i3,x,y,z,w)
            cache[key] = state4
          
          for i4 in range(9,0,-1):
            key = make_key(state4,i4,4)
            if key in cache:
              state5 = cache[key]
            else:
              x,y,z,w = state4
              state5 = monad4(i4,x,y,z,w)
              cache[key] = state5

              for i5 in range(9,0,-1):
                key = make_key(state5,i5,5)
                if key in cache:
                  state6 = cache[key]
                else:
                  x,y,z,w = state5
                  state6 = monad5(i5,x,y,z,w)
                  cache[key] = state6

                for i6 in range(9,0,-1):
                  key = make_key(state6,i6,6)
                  if key in cache:
                    state7 = cache[key]
                  else:
                    x,y,z,w = state6
                    state7 = monad6(i6,x,y,z,w)
                    cache[key] = state7

                  for i7 in range(9,0,-1):
                    key = make_key(state7,i7,7)
                    if key in cache:
                      state8 = cache[key]
                    else:
                      x,y,z,w = state7
                      state8 = monad7(i7,x,y,z,w)
                      cache[key] = state8

                    for i8 in range(9,0,-1):
                      key = make_key(state8,i8,8)
                      if key in cache:
                        state9 = cache[key]
                      else:
                        x,y,z,w = state8
                        state9 = monad8(i8,x,y,z,w)
                        cache[key] = state9

                      for i9 in range(9,0,-1):
                        key = make_key(state9,i9,9)
                        if key in cache:
                          state10 = cache[key]
                        else:
                          x,y,z,w = state9
                          state10 = monad9(i9,x,y,z,w)
                          cache[key] = state10

                        for i10 in range(9,0,-1):
                          key = make_key(state10,i10,10)
                          if key in cache:
                            state11 = cache[key]
                          else:
                            x,y,z,w = state10
                            state11 = monad10(i10,x,y,z,w)
                            cache[key] = state11

                          for i11 in range(9,0,-1):
                            key = make_key(state11,i11,11)
                            if key in cache:
                              state12 = cache[key]
                            else:
                              x,y,z,w = state11
                              state12 = monad11(i11,x,y,z,w)
                              cache[key] = state12

                            for i12 in range(9,0,-1):
                              key = make_key(state12,i12,12)
                              if key in cache:
                                state13 = cache[key]
                              else:
                                x,y,z,w = state12
                                state13 = monad12(i12,x,y,z,w)
                                cache[key] = state13

                              for i13 in range(9,0,-1):                               
                                key = make_key(state13,i13,13)
                                if key in cache:
                                  state14 = cache[key]
                                else:
                                  x,y,z,w = state13
                                  state14 = monad13(i13,x,y,z,w)
                                  cache[key] = state14
                                
                                if z==0:
                                  return int(''.join([str(i) for i in [i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13]]))
