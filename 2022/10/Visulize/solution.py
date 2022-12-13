import re 
import pygame
from time import sleep

WIDHT = 800
HEIGHT = 400
PIXEL_SIZE = 18
FPS = 15

OFFSET_X = 20
OFFSET_Y = 100

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)

def draw_pixel(x:int,y:int,screen:pygame.Surface, color:tuple[int,int,int]):
	pygame.draw.rect(screen, color, (OFFSET_X + x*PIXEL_SIZE,OFFSET_Y + y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

def draw_tube(x:int,y:int,screen:pygame.Surface):
	pygame.draw.rect(screen, RED, (OFFSET_X + (x-1) * PIXEL_SIZE - 3,OFFSET_Y + y*PIXEL_SIZE - 3,PIXEL_SIZE*3+6,PIXEL_SIZE+6), 3)

def reset():
	return 1, [[' ' for _ in range(40)] for _ in range(6)]
 
def read_input(file:str):
	inp = sum([*[[0] if line[0] == 'noop' else [0, int(line[1])] for line in [line.split(' ') for line in re.split('\r?\n',open(file).read())]]],[])
	return inp if len(inp) >= 240 else inp + [0 for _ in range(240-len(inp))]

def main(): 
	inp = read_input(r'.\2022\10\input.txt')  

	pygame.init()
	screen = pygame.display.set_mode((WIDHT, HEIGHT))
	pygame.display.set_caption("Day 10")
	clock = pygame.time.Clock()
	running = True
	cycle = 0
	x = 1
	rows = []

	while running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if cycle == 0:
			x, rows = reset()
		
		pos = cycle % 40 
		row = cycle // 40		
		rows[row][pos] = '#' if -1 <= x - pos <= 1 else ' '

		screen.fill(BLACK)

		for line in range(0, row):
			for x1, pix in enumerate(rows[line]):
				if pix == '#':
					draw_pixel(x1,line,screen, WHITE) 

		for x1, pix in enumerate(rows[row][:pos+1]):
			if pix == '#':
				draw_pixel(x1,row,screen, WHITE) 

		cycle = (cycle + 1) % 240
  	
		if cycle == 0:
			pygame.display.flip()
			sleep(2)
		else:
			draw_pixel(pos,row,screen,GREEN)
			draw_tube(x,row,screen)
			pygame.display.flip()
		
		x += inp[cycle-1]


if __name__ == '__main__': 
	main() 
