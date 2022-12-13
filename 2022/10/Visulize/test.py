from time import sleep
import pygame
from random import randint

WIDHT = 800
HEIGHT = 600
PIXEL_SIZE = 18
FPS = 50

OFFSET_X = 20
OFFSET_Y = 200

pygame.init()
screen = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()
# sprites = pygame.sprite.Group()

running = True
i = 0

lines = [[randint(0,1) for _ in range(40)] for _ in range(6)]

while running:
  clock.tick(FPS)
  # events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # update
  x = i  % 40
  y = i // 40
  # sprites.update()
  # draw
  screen.fill((0,0,0))
  for line in range(0,y):
    for x1, pix in enumerate(lines[line]):
      if pix == 1:
        pygame.draw.rect(screen, (255,255,255), (OFFSET_X + x1*PIXEL_SIZE,OFFSET_Y + line*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
  
  for x1, pix in enumerate(lines[y][:x]):
    if pix == 1:
      pygame.draw.rect(screen, (255,255,255), (OFFSET_X + x1*PIXEL_SIZE,OFFSET_Y + y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

  i = (i + 1) % (40 * 6)
  if i == 0:
    pygame.display.flip()
    sleep(2)
  else:
    pygame.draw.rect(screen, (0,100,255), (OFFSET_X + (x-1) * PIXEL_SIZE - 3,OFFSET_Y + y*PIXEL_SIZE - 3,PIXEL_SIZE*3+6,PIXEL_SIZE+6), 3)
    pygame.display.flip()

  # sprites.draw()
  # flip buffer