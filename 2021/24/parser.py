import re 

 
def read_input(file:str):
	return  [line.split(' ') for line in re.split('\r?\n',open(file).read())]

def parse(inp:list[list[str]]):
	file = open(r'.\2021\24\parsed_inp.cpp','w')
	# rewrite. parse 
	lines = ['#include <vector>\n','#include <inttypes.h>\n']
	block = 0
	for line in inp:
		if (line[0]=='inp'):
			if block != 0:
				lines.append('	return std::vector<int64_t>({x,y,z,w});\n}\n\n')
			lines.append(f'std::vector<int64_t> monad{block}(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w)'+'{\n')
			lines.append(f'	{line[1]} = number;\n')
			block+=1
		elif (line[0]=='add'):
			lines.append(f'	{line[1]} += {line[2]};\n')
		elif (line[0]=='mul'):
			lines.append(f'	{line[1]} *= {line[2]};\n')
		elif (line[0]=='div'):
			lines.append(f'	{line[1]} /= {line[2]};\n')
		elif (line[0]=='mod'):
			lines.append(f'	{line[1]} = {line[1]} % {line[2]};\n')
		elif (line[0]=='eql'):
			lines.append(f'	{line[1]} = {line[1]} == {line[2]} ? 1 : 0;\n')
		else:
			print('Bullshit:',line)
			exit(-1)
	lines.append('	return std::vector<int64_t>({x,y,z,w});\n}\n\n')
	file.writelines(lines)
	file.close()

if __name__ == '__main__': 
	inp = read_input(r'.\2021\24\input.txt')  
	parse(inp)
