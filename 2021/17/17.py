def solve1(area):
  vel = abs(area[1][0])
  print(vel*(vel-1)/2)
 
def get_up_time(vel):
  return vel*2

def get_times(vel,x):
  b = 2*vel+1
  return [(b-(b*b-8*x)**0.5)/2,(b+(b*b-8*x)**0.5)/2]

def solve2(area):
  max_vely = abs(area[1][0])
  min_vely = area[1][0]
  s = 0
  for vel_y in range(min_vely,max_vely):
    for vel_x in range(1,area[0][1]+1):
      n_vel_x = vel_x
      n_vel_y = vel_y
      x = 0 
      y = 0
      while(True):
        x+=n_vel_x
        y+=n_vel_y
        n_vel_x = 0 if n_vel_x==0 else n_vel_x-1
        n_vel_y -= 1
        if area[0][0]<=x<=area[0][1] and area[1][0]<=y<=area[1][1]:
            s+=1
            break
        if x>area[0][1] or y<area[1][0]:
          break
  print(s)

area = [[int(i) for i in coord.split('=')[1].split('..')] for coord in open('input.txt').readline().strip().split(', ')]
# area = [[int(i) for i in coord.split('=')[1].split('..')] for coord in open('input_test.txt').readline().strip().split(', ')]

solve1(area)
solve2(area)