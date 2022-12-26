import pygame
import re
from controls import FolderItem

WIDTH = 400
HEIGHT = 600
FPS = 30
MAX_ITEMS = 6
ITEM_SIZE = (250,50)
FONT = 'Comic Sans'
FONT_SIZE = 16
BW_DISTANCE = 20
ITEM_OFFSET = ((WIDTH - ITEM_SIZE[0])//2,(HEIGHT - (MAX_ITEMS+1)*(BW_DISTANCE + ITEM_SIZE[1]))//2)

WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255,165,0)
WHITE_GREYISH = (251,244,232)
YELLOW = (195,145,67)

class Tree:
	def __init__(self, type:str, data:str | int, connections:dict[str, 'Tree'], prev:'Tree', size = 0):
		self.type = type
		self.connections = connections
		self.data = data
		self.prev = prev
		self.size = size

	def __repr__(self):
		return f'TreeNode: {self.type}, {self.data=}, {self.connections=}'
		

def form_dirs(lines:list[list[str]]):
	head = Tree('dir', '/', dict(), None)
	cur = head
	i = 0
	while i < len(lines):
		line = lines[i]
		if line[0] == '$':
			if line[1] == 'cd':
				if line[2] == '/':
					cur = head
				elif line[2] == '..':
					cur = cur.prev
				else:
					cur = cur.connections[line[2]]
				i+=1
			elif line[1] == 'ls':
				i+=1
				line = lines[i]
				while line[0] != '$':
					if line[0] == 'dir':
						cur.connections[line[1]] = Tree('dir', line[1], dict(), cur)
					else:
						cur.connections[line[1]] = Tree('file', int(line[0]), dict(), cur)
					i+=1
					if (i<len(lines)): 
						line = lines[i]
					else:
						break
	return head

def calc_size(dir:Tree)->int:
	res = 0
	for key in dir.connections:
		tree = dir.connections[key]
		if tree.type == 'file':
			res += tree.data
		elif tree.type == 'dir':
			res += calc_size(tree)
		else:
			print(f'Хто? {tree.type=}')
			exit(-1)
		dir.size = res
	return res


def read_input():
  head = form_dirs([line.split(' ') for line in re.split('\r?\n',open(r'.\2022\7\input.txt').read())])
  calc_size(head)
  return head

def createFolderItem(screen:pygame.Surface, itemNum:int, file_str:str, name:str, x:int = ITEM_OFFSET[0],width:int = ITEM_SIZE[0]):
  return FolderItem(screen, x, ITEM_OFFSET[1] + itemNum * (ITEM_SIZE[1] + BW_DISTANCE), width, ITEM_SIZE[1],file_str, FONT, FONT_SIZE,
          bg=BLACK, fg=ORANGE, hover_bg=YELLOW, hover_fg=WHITE_GREYISH,
          click=lambda:name)

def createSpritesForFolder(node:Tree, screen:pygame.Surface, startIndex = 0):
  sprites = pygame.sprite.Group()
  item = 0
  itemNum = 0
  if node.prev != None:
    sprites.add(createFolderItem(screen,0,'..','..'))
    item += 1
  items = list(node.connections.keys())
  while item < MAX_ITEMS and itemNum + startIndex < len(items):
    name = items[itemNum + startIndex]
    cur_item = node.connections[name]
    type = cur_item.type
    size = cur_item.data if cur_item.type == 'file' else cur_item.size
    size_str = '{:.2f} KB'.format(size/1024)
    file_str = f'{type}: {name}    {size_str}'
    sprites.add(createFolderItem(screen,item, file_str,name))
    item += 1
    itemNum += 1
  return sprites, startIndex + itemNum, item, itemNum

def main():
  head = read_input()

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Day 7")
  clock = pygame.time.Clock()
  running = True

  sprites, cur_index, items, itemCount = createSpritesForFolder(head, screen)
  if cur_index - itemCount > 0:
    sprites.add(createFolderItem(screen, items, ' up ', str(max(cur_index-itemCount-MAX_ITEMS+1,0)),width=70))
  if cur_index < len(head.connections) - 1:
    sprites.add(createFolderItem(screen, items, 'down', str(cur_index), x=ITEM_OFFSET[0]+BW_DISTANCE+ITEM_SIZE[0], width=70))

  while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        for sprite in sprites:
          if sprite.rect.collidepoint(pygame.mouse.get_pos()) and type(sprite) == FolderItem:
            item_name = sprite.click()
            if item_name == '..':
              head = head.prev
              sprites, cur_index, items, itemCount = createSpritesForFolder(head, screen, 0)
            elif item_name.isdigit():
              sprites, cur_index, items, itemCount = createSpritesForFolder(head, screen, int(item_name))
            elif head.connections[item_name].type == 'dir':
              head = head.connections[item_name]
              sprites, cur_index, items, itemCount = createSpritesForFolder(head, screen, 0)
            if cur_index - itemCount > 0:
              sprites.add(createFolderItem(screen, items, '  up   ', str(max(cur_index-itemCount-MAX_ITEMS+1,0)),width=70))
            if cur_index < len(head.connections) - 1:
              sprites.add(createFolderItem(screen, items, ' down  ', str(cur_index), x=ITEM_OFFSET[0]+(BW_DISTANCE+ITEM_SIZE[0])//2, width = 70))
    
    screen.fill(BLACK)
    
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
  main()