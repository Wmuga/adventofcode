import re 
from copy import deepcopy
from queue import PriorityQueue

costs = {
	'A':1,
	'B':10,
	'C':100,
	'D':1000
}

def update_tuple(t,i,e):
	t1 = list(t)
	t1[i] = e
	return tuple(t1)

def get_moves(rooms, halls):
	moves = []
	# Moves from rooms
	for n, room in enumerate(rooms):
		for depth, amph in enumerate(room):
			if amph != '.':

				# if occupied exit - cant move
				if halls[2*(n+1)] != '.':
					break

				# check for full room 
				stay = amph == 'ABCD'[n]
				
				for amph1 in room[depth:]:
					if amph != amph1:
						stay = False
						break
				
				if stay:
					break
				# To the left
				for l in range(2*n+1,-1,-1):
					if halls[l] == '.':
						if l in [2,4,6,8]:
							continue
						room1 = update_tuple(rooms,n,update_tuple(room,depth,'.'))
						hall1 = update_tuple(halls,l,amph)
						moves.append((room1,hall1,(depth+2*n+3-l)*costs[amph]))
					else:
						break
				# To the right
				for l in range(2*n+3,len(halls)):
					if halls[l] == '.':
						if l in [2,4,6,8]:
							continue
						room1 = update_tuple(rooms,n,update_tuple(room,depth,'.'))
						hall1 = update_tuple(halls,l,amph)
						moves.append((room1,hall1,(depth+l-2*n-1)*costs[amph]))
					else:
						break
				break
	
	# moves to room
	for pos, amph in enumerate(halls):
		room = 0
		dest = 0
		
		if   amph == 'A':
			room = 0
			dest = 2
		elif amph == 'B':
			room = 1
			dest = 4
		elif amph == 'C':
			room = 2
			dest = 6
		elif amph == 'D':
			room = 3
			dest = 8
		else:
			continue
		# check for occupation
		can_move = True
		depth = -1
		for i,acc_amph in enumerate(rooms[room],start=-1):
			if acc_amph != '.' and acc_amph != amph:
				can_move = False
				break
			if acc_amph == amph and depth == -1:
				depth = i

		if not can_move:
			continue

		depth = depth if depth != -1 else len(rooms[room])-1
		# try to move to room
		can_move = True

		if dest != pos:
			step = abs(dest - pos)//(dest - pos)
			for l in range(pos+step, dest+step,step):
				if halls[l] != '.':
					can_move = False
					break

		if can_move:
			room1 = update_tuple(rooms,room,update_tuple(rooms[room],depth, amph))
			hall1 = update_tuple(halls,pos,'.')
			moves.append((room1,hall1,(abs(dest - pos)+depth+1)*costs[amph]))

	return moves

def solve(inp:list[list[str]]): 
	rooms = tuple([tuple(rooms) for rooms in (map(list, zip(*inp)))])
	hall = tuple(['.' for _ in range(11)])
	goal_rooms = tuple([tuple([c for _ in range(len(rooms[0]))]) for c in 'ABCD'])
	goal_hall = deepcopy(hall)

	back_track = {}
	costs = {}
	frontier = PriorityQueue()

	frontier.put((0,(rooms,hall)))
	costs[(rooms,hall)] = 0
	back_track[(rooms,hall)] = None

	while not frontier.empty():
		_, data = frontier.get()
		rooms, hall = data
		if rooms == goal_rooms:
			break

		for rooms1, hall1, cost in get_moves(rooms, hall):
			new_cost = costs[(rooms,hall)] + cost

			if not ((rooms1, hall1) in costs) or costs[(rooms1, hall1)] > new_cost:
				costs[(rooms1, hall1)] = new_cost
				frontier.put((new_cost,(rooms1, hall1)))
				back_track[(rooms1,hall1)] = (rooms,hall)
			

	print(f'Solution: {costs[(goal_rooms,goal_hall)]}')  
	return back_track

def draw(file, back_track, key):
	if back_track[key] == None:
		return
	
	draw(file, back_track, back_track[key])

	rooms, hall = key

	file.write('#'*13+'\n')
	file.write(f'#{"".join(list(hall))}#\n')
	file.write(f'###{rooms[0][0]}#{rooms[1][0]}#{rooms[2][0]}#{rooms[3][0]}###\n')
	for i in range(1,len(rooms[0])):
		file.write(f'  #{rooms[0][i]}#{rooms[1][i]}#{rooms[2][i]}#{rooms[3][i]}#  \n')
	file.write(f'  {"#"*9}  \n')
	file.write(f'\n')

def read_input(file:str):
	return  [line for line in [[c for c in line if c in 'ABCD'] for line in re.split('\r?\n',open(file).read())] if len(line)>0]

def main(): 
	inp = read_input(r'.\2021\23\input_test.txt')  

	print('Test input:')
	solve(deepcopy(inp)) 

	inp = inp[:1] + [list('DCBA'),list('DBAC')] + inp[1:]
	back = solve(inp) 

	file = open(r'.\2021\23\log_test.txt','w')
	draw(file,back,(tuple([tuple([c for _ in range(4)]) for c in 'ABCD']), tuple(['.' for _ in range(11)])))
	file.close()
 
	inp = read_input(r'.\2021\23\input.txt')  

	print('Actual input:')
	solve(deepcopy(inp))
	inp = inp[:1] + [list('DCBA'),list('DBAC')] + inp[1:]
	back = solve(inp) 

	file = open(r'.\2021\23\log.txt','w')
	draw(file,back,(tuple([tuple([c for _ in range(4)]) for c in 'ABCD']), tuple(['.' for _ in range(11)])))
	file.close()


if __name__ == '__main__': 
	main() 
