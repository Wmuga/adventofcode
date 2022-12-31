import re 
from itertools import product
# For debug purposes
DEBUG_ROTS = [
	[
		lambda x,y,z: (x,y,z),
		lambda x,y,z: (x,-z,y),
		lambda x,y,z: (x,-y,-z),
		lambda x,y,z: (x,z,-y)
	],
	[
		lambda x,y,z: (x,y,z),
		lambda x,y,z: (-z,y,x),
		lambda x,y,z: (-x,y,-z),
		lambda x,y,z: (z,y,-x)
	],
	[
		lambda x,y,z: (x,y,z),
		lambda x,y,z: (y,-x,z),
		lambda x,y,z: (-x,-y,z),
		lambda x,y,z: (-y,x,z)
	]
]
# Actual unique rotations
ROTS = [
	lambda x,y,z: (y, z, x),
	lambda x,y,z: (y, x, -z),
	lambda x,y,z: (-y, z, -x),
	lambda x,y,z: (z, y, -x),
	lambda x,y,z: (z, x, y),
	lambda x,y,z: (-z, y, x),
	lambda x,y,z: (-z, x, -y),
	lambda x,y,z: (-y, x, z),
	lambda x,y,z: (x, -z, y),
	lambda x,y,z: (-z, -x, y),
	lambda x,y,z: (x, -y, -z),
	lambda x,y,z: (y, -x, z),
	lambda x,y,z: (y, -z, -x),
	lambda x,y,z: (-y, -x, -z),
	lambda x,y,z: (-x, -y, z),
	lambda x,y,z: (-z, -y, -x),
	lambda x,y,z: (-x, z, y),
	lambda x,y,z: (x, y, z),
	lambda x,y,z: (x, z, -y),
	lambda x,y,z: (-x, y, -z),
	lambda x,y,z: (z, -y, x),
	lambda x,y,z: (z, -x, -y),
	lambda x,y,z: (-y, -z, x),
	lambda x,y,z: (-x, -z, -y)
]
# Generating unique rotations
def gen_rotations():
	rots = set()
	for r0,r1,r2 in product(range(4),range(4),range(4)):
		rot = DEBUG_ROTS[0][r0](*DEBUG_ROTS[1][r1](*DEBUG_ROTS[2][r2](1,2,3)))
		rots.add(rot)
	rots = list(rots)
	st = ['x','y','z','-z','-y','-x']
	for rot in rots:
		f,s,l = [n-1 if n >0 else n for n in rot]
		f1,s1,l1 = st[f],st[s],st[l]
		print(f'lambda x,y,z: ({f1}, {s1}, {l1}),')

def apply_offset(beacons:set[tuple[int,int,int]], offset):
	return set([tuple([x+xc for xc, x in zip(offset, beacon)]) for beacon in beacons])

def change_base_point(beacons:set[tuple[int,int,int]], new_base):
	return set([tuple([x-xc for xc, x in zip(new_base, beacon)]) for beacon in beacons])

def recalculate_offsets(beacons:set[tuple[int,int,int]], current_offset):
	corner = (10000,10000,10000)
	for b in beacons:
		if b[2] < corner[2]:
			corner = b
		elif b[2] == corner[2]:
			if b[1] < corner[1]:
				corner = b
			elif b[1] == corner[1]:
				if b[0] < corner[0]:
					corner = b
	return change_base_point(beacons, corner), tuple(x+xc for x,xc in zip(corner,current_offset))

# too lazy. Got function from tests
def calc(nums,v,v1,v2,v3):
  return nums[0][0]*v + nums[1][0]*v1 + nums[2][0]*v2 + nums[3][0]*v3, \
    nums[0][1]*v + nums[1][1]*v1 + nums[2][1]*v2 + nums[3][1]*v3, \
    nums[0][2]*v + nums[1][2]*v1 + nums[2][2]*v2  + nums[3][2]*v3

def get_information(scanners:list[set[tuple[int,int,int]]], min_beacon_count = 12, DEBUG = False): 
	# Store coords of left-up most beacon. All relative to him. Recalculate. Try apply everything. If < 12 - sad 
	Ways = [None for _ in range(len(scanners))]
	beacons, offset = recalculate_offsets(set(scanners[0]), (0,0,0))
	checked = [0]
	while len(checked) != len(scanners):
		for scan_num, scanner in enumerate(scanners[1:], start=1):
			if scan_num in checked:
				continue

			found = False
			for i, rot in enumerate(ROTS):
				if found: break
				# (-offset1) - scanner coord (need to add point b)
				beacons_rot, offset1 = recalculate_offsets(set([rot(*b) for b in scanner]),(0,0,0))
				for b1 in beacons_rot:
					if found: break
					beacons_rot_changed = change_base_point(beacons_rot, b1)
					for b in beacons:
						beacons_rot_offseted = apply_offset(beacons_rot_changed, b)
						inters = beacons.intersection(beacons_rot_offseted)
						if len(inters) >= min_beacon_count:
							# -offset - base. -offset1 - cur_scanner, b1 - new base point, b - offset
							# -offset1+b1-b
							Ways[scan_num] = (i, calc((offset,offset1,b1,b),1,-1,-1,1))
							beacons, offset = recalculate_offsets(beacons.union(beacons_rot_offseted), offset)
							checked.append(scan_num)
							if DEBUG:
								print('Found', scan_num)
							found = True
							break
					
			if not found and DEBUG:
				print('Not found', scan_num)
	return beacons, Ways, offset

def solve1(beacons:set[tuple[int,int,int]]): 
	print(f'Solution 1: {len(beacons)}')  
 
def solve2(ways:list[tuple], s0:tuple[int,int,int]): 
	res = 0
	scanners = [(0,0,0)]
	for sc in ways[1:]:
		_, scanner = sc
		scanners.append(scanner)
	for coord,coord1 in product(scanners,scanners):
		if coord1 == coord:
			continue
		res = max(res, sum([abs(c-c1) for c,c1 in zip(coord, coord1)]))
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return [set([tuple([int(n) for n in beacon.split(',')]) for beacon in re.split('\r?\n',scanner)[1:]]) for scanner in re.split('\r?\n\r?\n',open(file).read())]

def main(): 
	# inp = read_input(r'.\2021\19\input_test0.txt')  
	# print('Pre test')
	# solve1(inp, 3) 

	inp = read_input(r'.\2021\19\input_test.txt')  

	print('Test input:')
	beacons, ways, s0_coord = get_information(inp,DEBUG=True)
	solve1(beacons) 
	solve2(ways, s0_coord) 
 
	inp = read_input(r'.\2021\19\input.txt')  

	print('Actual input:')
	beacons, ways, s0_coord = get_information(inp)
	solve1(beacons) 
	solve2(ways, s0_coord) 

def check_rots():
	a = set()
	# got from reddit
	b = set([(1, 2, 3), (-2, 1, 3), (-1, -2, 3), (2, -1, 3), (-3, 2, 1), (-2, -3, 1), (3, -2, 1), (2, 3, 1), (-1, 2, -3), (-2, -1, -3), (1, -2, -3), (2, 1, -3), (3, 2, -1), (-2, 3, -1), (-3, -2, -1), (2, -3, -1), (1, -3, 2), (3, 1, 2), (-1, 3, 2), (-3, -1, 2), (1, 3, -2), (-3, 1, -2), (-1, -3, -2), (3, -1, -2)])
	for rot in ROTS:
		a.add(rot(1,2,3))
	print(len(b.difference(a)))

if __name__ == '__main__': 
	# gen_rotations()
	# check_rots()
	main() 
