import pygame
import re
from copy import deepcopy, copy

WIDTH = 950
HEIGHT = 700
FIELD = (900,600)
OFFSET = (40,40)
GENERATION_TEXT_OFFSET = (20,20)
FPS = 30

WHITE = (255,255,255)
GREEN = (0,255,0)

DELTAS = [(1,0),(0,1),(-1,0),(0,-1)]
ARROWS = {1:'>',11:'v',101:'<',1001:'^'}
DIR_TO_ARR = [1,11,101,1001]
GENERATION_FONT = None


def draw_line(line, y,pix_size,screen):
  for x, pix in enumerate(line):
    pix_offset = (x*pix_size[0]+OFFSET[0],y*pix_size[1]+OFFSET[1])
    draw_pix = font.render(pix,True,GREEN if pix == 'E' else WHITE)
    screen.blit(draw_pix, pix_offset)

def draw(blizs, elves, end_pos,size, pix_size, generation,screen):
  # Prepare field for drawing
  field = [[0 for _ in range(size[0])] for _ in range(size[1])]
  for x,y in elves:
    if 0<=y<size[1]:
      field[y][x] = -1
  for dir in range(4):
    for x,y in blizs[dir]:
      field[y][x] = DIR_TO_ARR[dir] if field[y][x]==0 else (field[y][x]%10 + 1)
  draw_field = [[('E' if s==-1 else (ARROWS[s] if s in ARROWS else (' ' if s == 0 else str(s)))) for s in line] for line in field]
  # Draw generation
  gen_text = GENERATION_FONT.render(f'Generation {generation}', True, WHITE)
  screen.blit(gen_text,GENERATION_TEXT_OFFSET)
  # Draw field
  draw_line('#E'+'#'*size[0],0,pix_size,screen)
  for i,line in enumerate(draw_field,start=1):
    draw_line(f'#{"".join(line)}#',i,pix_size,screen)
  draw_line('#'*size[0]+('E' if end_pos in elves else ' ')+'#',size[1]+1,pix_size,screen)

def get_neigbours(pos,size,end_pos):
  x,y = pos
  x_max, y_max = size
  return [(x,y) for x,y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if (x,y)==end_pos or (0<=x<x_max and 0<=y<y_max)]

# pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Day 24")
clock = pygame.time.Clock()
running = True

GENERATION_FONT = pygame.font.SysFont('Times New Roman',14)
# read input
arrows = '>v<^'
lines = [line[1:-1] for line in re.split('\r?\n',open(r'.\2022\24\input.txt').read())[1:-1]]
size = len(lines[0]), len(lines)
start_bliz = {i:[] for i in range(4)}
for y, line in enumerate(lines):
  for x, simb in enumerate(line):
    if simb != '.':
      start_bliz[arrows.find(simb)].append((x,y))

# Get font size
fontName = 'Arial'
fontSize = 5
font = pygame.font.SysFont(fontName,fontSize)
pix = font.render('E',True,WHITE)
pix_size = pix.get_width(), pix.get_height()
while pix_size[0] < FIELD[0]//(size[0]+1) and pix_size[1] < FIELD[1]//(size[1]+1):
  fontSize += 1
  font = pygame.font.SysFont(fontName,fontSize)
  pix = font.render('E',True,WHITE)
  pix_size = pix.get_width(), pix.get_height()

# Cycle init
start_pos = (0,-1)
end_pos = size[0]-1,size[1]
generation = 0
blizs = deepcopy(start_bliz)
Elves = {start_pos}

while running:
  clock.tick(FPS)
  # events 
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      running = False
  # draw
  screen.fill((0,0,0))
  draw(blizs,Elves, end_pos,size,pix_size,generation,screen)
  pygame.display.flip()
  # simulate
  if not(end_pos in Elves):
    for wind_dir in blizs:
      dx,dy = DELTAS[wind_dir]
      blizs[wind_dir] = [((x+dx) % size[0],(y+dy) % size[1]) for x,y in blizs[wind_dir]]
    # simulate elv
    Elves1 = copy(Elves)
    for elv in Elves1:
      neighbours = get_neigbours(elv,size, end_pos)
      for x,y in neighbours:
        can_move = True
        for i in range(4):
          if (x,y) in blizs[i]:
            can_move = False
            break
        if can_move:
          Elves.add((x,y))
    # kill elves in bliz
    for wind_dir in blizs:
      for x,y in blizs[wind_dir]:
        if (x, y) in Elves:
          Elves.remove((x,y))
    generation += 1
  else:
    generation = 0
    blizs = deepcopy(start_bliz)
    Elves = {start_pos}
    pygame.time.wait(2000)