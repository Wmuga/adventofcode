@echo off

if "%~1"=="" goto :blank
SET "TAB=	"
:: file names
SET task_file=.\%1\task.txt
SET input_file=.\%1\input.txt
SET test_input_file=.\%1\input_test.txt
SET solution_file=.\%1\solution.py

mkdir .\%1
:: Create blank files
echo task_here > %task_file%
echo input_here > %input_file%
echo test_input_here > %test_input_file%
:: Create base solution
echo import re > %solution_file%
echo(>> %solution_file%
:: solution 1
echo def solve1(inp): >> %solution_file%
echo(%TAB%res=0 >> %solution_file% 
echo(%TAB%print(f'Solution 1: {res}') >> %solution_file% 
echo( >> %solution_file%
:: solution 2 
echo def solve2(inp): >> %solution_file%
echo(%TAB%res=0 >> %solution_file% 
echo(%TAB%print(f'Solution 2: {res}') >> %solution_file% 
echo( >> %solution_file%
:: main
echo(def read_input(file:str):>> %solution_file%
echo(%TAB%return  re.split('\r?\n',open(file).read())>> %solution_file%
echo(>> %solution_file%
echo def main(): >> %solution_file%
echo(%TAB%inp = read_input(r'%test_input_file%') >> %solution_file% 
echo(>> %solution_file%
echo(%TAB%print('Test input:')>> %solution_file%
echo(%TAB%solve1(inp) >> %solution_file%
echo(%TAB%solve2(inp) >> %solution_file%
echo(>> %solution_file% 
echo(%TAB%inp = read_input(r'%input_file%') >> %solution_file% 
echo(>> %solution_file%
echo(%TAB%print('Actual input:')>> %solution_file%
echo(%TAB%solve1(inp) >> %solution_file%
echo(%TAB%solve2(inp) >> %solution_file%
echo(>> %solution_file%
echo(>> %solution_file%
:: execution
echo if __name__ == '__main__': >> %solution_file%
echo(%TAB%main() >> %solution_file%

echo Done
goto :end
:blank
	echo No folder 
:end