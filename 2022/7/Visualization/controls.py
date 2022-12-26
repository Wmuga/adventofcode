import pygame

class FolderItem(pygame.sprite.Sprite):
  def __init__(self, surface, x = 10, y = 10, width = 60, height = 40, text='Button', font = 'Arial', fontSize = 16, border_size = 2,
  bg = (255,255,255), fg = (0,0,0), hover_bg = (200,200,200), hover_fg = (0,0,0), border_color = (255,255,255), click = None):
    super().__init__()
    self.click = click if click else lambda: None
    # Rectangle
    self.x = x
    self.y = y
    self.width = width
    self.heigth = height
    self.border_size = border_size
    # Colors
    self.bg = bg
    self.fg = fg
    self.hover_bg = hover_bg
    self.hover_fg = hover_fg
    self.border_color = border_color
    # Text
    self.text = text
    self.font = pygame.font.SysFont(font, fontSize)
    self.drawn_text = self.font.render(text, True, self.fg)
    self.surface = surface
    # for superclass
    self.image = pygame.Surface((self.width + self.border_size * 2,self.heigth + self.border_size * 2),pygame.SRCALPHA)
    self.rect = pygame.Rect(self.x,self.y,self.width,self.heigth)
  
  def update(self):
    bg, fg = (self.hover_bg, self.hover_fg) if self.rect.collidepoint(pygame.mouse.get_pos()) else (self.bg, self.fg)
    self.image = pygame.Surface((self.width + self.border_size * 2,self.heigth + self.border_size * 2),pygame.SRCALPHA)
    pygame.draw.rect(self.surface, self.border_color, (self.x, self.y, self.width+self.border_size*2, self.heigth+self.border_size*2))
    self.drawn_text = self.font.render(self.text, True, fg)
    pygame.draw.rect(self.surface, bg, (self.x + self.border_size,self.y + self.border_size,self.width,self.heigth))
    w,h = self.drawn_text.get_width(), self.drawn_text.get_height()
    self.image.blit(self.drawn_text, ((self.width-w - self.border_size) - 2, (self.heigth-h)//2 - self.border_size))
