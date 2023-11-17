# hier komt de code voor de sprites
import pygame
from settings import *

class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        bg_image = pygame.image.load("graphics/environment/background.png").convert()

        full_height = bg_image.get_height() * scale_factor
        full_width = bg_image.get_width() * scale_factor
        full_sized_image = pygame.transform.scale(bg_image,(int(full_width),int(full_height))) # scale de image naar de juiste grootte
      
        self.image = pygame.Surface((full_width * 2,full_height)) 
        self.image.blit(full_sized_image,(0,0))
        self.image.blit(full_sized_image,(full_width,0))
      
        self.rect = self.image.get_rect(topleft=(0,0)) # topleft is een x en y waarde in 1 variabele
        self.pos = pygame.math.Vector2(self.rect.topleft) # vector2 is een x en y waarde in 1 variabele

    def update(self, dt):
        self.pos.x -= 300 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)