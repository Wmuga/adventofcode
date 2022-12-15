import re 

def solve1(sensors:list[tuple[int,int,int]],beacons:list[tuple[int,int]],y:int): 
	res=0  
	coords = {}

	for sensor in sensors:
		xs, ys, r = sensor
		
		if abs(ys - y) <= r:
			start = xs - (r - abs(ys - y))
			end = xs +  (r - abs(ys - y))
			for x in range(start,end+1): coords[x] = 1

	for x in coords.keys():
		if not ((x,y) in beacons):
			res+=1

	print(f'Solution 1: {res}')  


class RangeList:
	def __init__(self):
		self.ranges:list[tuple[int,int]] = []
		pass
	
	def add(self, new_r:tuple[int,int]):
		self.ranges.append(new_r)
		
		while 1:
			changed = False
			i = 0
			while i < len(self.ranges) - 1:
				i1 = i+1
				sn,en = self.ranges[i]
				while i1 < len(self.ranges):
					sr,er = self.ranges[i1]
					if sr <= sn <= er or sr <= en <= er or sn <= sr <= en or sn <= er <= en:
						self.ranges[i] = (min(sr,sn),max(en,er))
						self.ranges.pop(i1)
						changed = True
					else:
						i1 += 1
				i+=1

			if not changed:
				break

	def __repr__(self):
		return str(self.ranges if len(self.ranges)!=1 else self.ranges[0])

def solve2(sensors:list[tuple[int,int,int]], max_c:int): 
	res=0  

	for y in range(0, max_c+1):
		
		y_list = RangeList()

		for sensor in sensors:
			xs, ys, r = sensor

			if abs(ys - y) <= r:
				start = min(max(xs - (r - abs(ys - y)),0),max_c)
				end = min(max(xs +  (r - abs(ys - y)),0),max_c)
				y_list.add((start,end))
		
		if len(y_list.ranges) > 1:
			r = y_list.ranges[0 if y_list.ranges[0][0]==0 else 1]
			res = (r[1]+1)*4000000+y
			break

	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	sensors = []
	beacons = []

	for line in  re.split('\r?\n',open(file).read()):
		xs, ys, xb, yb = [int(i) for i in re.findall('(?<=[xy]=)-?\d+',line)]
		r = abs(xs-xb) + abs(ys-yb)
		sensors.append((xs,ys,r))
		beacons.append((xb,yb))
	
	return sensors, beacons

def main(): 
	sensors, beacons = read_input(r'.\2022\15\input_test.txt')  

	print('Test input:')
	solve1(sensors, beacons, 10) 
	solve2(sensors, 20) 
 
	sensors, beacons = read_input(r'.\2022\15\input.txt')  

	print('Actual input:')
	solve1(sensors, beacons, 2000000) 
	solve2(sensors, 4000000) 


if __name__ == '__main__': 
	main() 
