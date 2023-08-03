import random
import pygame
import time
import pyganim


class Dice:
    def __init__(self, center) -> None:
        self.dice = [1,2,3,4,5,6]
        self.index = random.randint(0,5)
        self.center = center
        self.show = False
        self.playing = False
        
        self.anim = pyganim.PygAnimation

    def load_resources(self):
        
        self.image = pygame.image.load("Resources/Images/dice.png") 
        cara6 = self.image.subsurface(pygame.Rect(0,0,201,200))
        cara5 = self.image.subsurface(pygame.Rect(207,0,201,200))
        cara4 = self.image.subsurface(pygame.Rect(415,0,201,200))
        cara3 = self.image.subsurface(pygame.Rect(0,204,201,200))
        cara2 = self.image.subsurface(pygame.Rect(207,204,201,200))
        cara1 = self.image.subsurface(pygame.Rect(415,204,201,200))
        
        self.anim = pyganim.PygAnimation([(cara1, 100), (cara2, 100), (cara3, 100), (cara4, 100), (cara5, 100), (cara6, 100)])

        self.anim.play()
        self.start_anim = pygame.time.get_ticks()
    def reroll(self):
        random.shuffle(self.faces)
        
    def change_index(self):
        self.index = random.randint(0,5)
        
    def draw_dice(self, screen):
        screen.blit(self.anim[self.current_face], self.rect)