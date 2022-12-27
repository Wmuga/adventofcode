import re 
from queue import PriorityQueue
from math import ceil

def draw(d, key, file):
	if key == None:
		return
	draw(d,d[key],file)
	bots, ores, time = key
	file.write(f'{time}: {bots=}, {ores=}')
	file.write('\n')

def time_to_cost(costs, bots, ores):
	times = [-1]*len(costs)
	for i,cost in enumerate(costs):
		max_time = 0
		for bot,ore,price in zip(bots,ores,cost):
			if price == 0:
				continue
			if bot == 0:
				max_time = -1
				break
			max_time = max(max_time, 0, ceil((price-ore)/bot))
		times[i] = max_time
	return times

def simulate(blueprint:str, time:int, NUM = 0, DEBUG = False):
	# ore, clay, obisidian, geode, rem time
	costs_raw = [int(cost) for cost in re.findall('(\d+)', blueprint)[1:]]
	costs = [(costs_raw[0],0,0,0),(costs_raw[1],0,0,0),(costs_raw[2],costs_raw[3],0,0),(costs_raw[4],0,costs_raw[5],0)]
	max_bots = [max(cost[i] for cost in costs) for i in range(len(costs[0]))]
	max_bots[-1] = time
	bots = (1,0,0,0)
	ores = (0,0,0,0)
	res = 0

	calc_max_poss = lambda t,b: 0*t*(t-1)//2 + b*t*0 + 5000000
	max_possible = calc_max_poss(time, 0)
	
	known_pos = dict()
	backtrack = dict()
	frontier = PriorityQueue()

	value = (bots,ores,time)
	frontier.put((max_possible,value))
	known_pos[time] = max_possible
	backtrack[value] = None
	res_value = ()

	while not frontier.empty():
		_, item = frontier.get()
		bots, ores, time = item
		times = time_to_cost(costs,bots,ores)
		for i,skip_time in enumerate(times):
			if skip_time == -1 or bots[i] == max_bots[i]:
				continue
			
			skip_time =  time - max(time-skip_time, 0)
			ores1 = [ore+bot*skip_time for ore,bot in zip(ores,bots)]
			time1 = time - skip_time

			if time1 == 0:
				if ores1[-1] > res:
					res = ores1[-1]
					res_value = (bots, tuple(ores1), time1)
					backtrack[res_value] = item
				continue
			
			ores1 = [ore+bot-cost for ore,bot,cost in zip(ores1,bots,costs[i])]
			bots1 = list(bots)
			bots1[i] += 1
			time1 -= 1

			if time1 == 0:
				if ores1[-1] > res:
					res = ores1[-1]
					res_value = (tuple(bots1), tuple(ores1), time1)
					backtrack[res_value] = item
				continue
			
			bots1 = tuple(bots1)
			ores1 = tuple(ores1)
			
			cur_max_possib = calc_max_poss(time1,bots[-1]) + ores1[-1]

			if (time1 in known_pos and known_pos[time1] > cur_max_possib) or cur_max_possib < res:
				continue
			
			value = bots1, ores1, time1
			known_pos[time1] = cur_max_possib
			backtrack[value] = item
			
			frontier.put((max_possible - cur_max_possib,value))

	if DEBUG:
		file = open(fr'.\2022\19\debug{NUM}.log','w')
		draw(backtrack, res_value,file)
		file.close()

	return res

def solve1(inp, DEBUG = False): 
	res = 0
	for i,line in enumerate(inp):
		geodes = simulate(line,24, i, DEBUG)
		if DEBUG:
			print(f'Blueprint {i+1}: {geodes}')
		res += (i+1)*geodes
	print(f'Solution 1: {res}')  
 
def solve2(inp,DEBUG = False): 
	res = 1
	for i,line in enumerate(inp[:3]):
		geodes = simulate(line,32, i, True)
		if DEBUG:
			print(f'Blueprint {i+1}: {geodes}')
		res *= geodes
	print(f'Solution 2: {res}')  
 
def read_input(file:str):
	return re.split('\r?\n',open(file).read())

def main(): 
	inp = read_input(r'.\2022\19\input_test.txt')  

	print('Test input:')
	# solve1(inp) 
	solve2(inp, True) 
 
	inp = read_input(r'.\2022\19\input.txt')  

	print('Actual input:')
	# solve1(inp) 
	solve2(inp, True) 


if __name__ == '__main__': 
	main() 
