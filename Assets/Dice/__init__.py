import random
import pygame
import time


class Dice:
    def __init__(self, center) -> None:
        self.dice = [1,2,3,4,5,6]
        self.index = random.randint(0,5)
        self.center = center
        self.show = False
        self.playing = False
        
    def load_resources(self):
        
        self.image = pygame.image.load("Resources/Images/dice.png") 
        cara6 = self.image.subsurface(pygame.Rect(0,0,201,200))
        cara5 = self.image.subsurface(pygame.Rect(207,0,201,200))
        cara4 = self.image.subsurface(pygame.Rect(415,0,201,200))
        cara3 = self.image.subsurface(pygame.Rect(0,204,201,200))
        cara2 = self.image.subsurface(pygame.Rect(207,204,201,200))
        cara1 = self.image.subsurface(pygame.Rect(415,204,201,200))
        
        self.faces = [cara1,cara2, cara3, cara4, cara5, cara6]
        self.anim = self.faces + self.faces
        self.rect = cara5.get_rect()
        
        self.rect.center = self.center
    def reroll(self):
        random.shuffle(self.faces)
        
    def change_index(self):
        self.index = random.randint(0,5)
        
    def draw_dice(self, screen):
        screen.blit(self.anim[self.current_face], self.rect)
    
    def draw_dice_anim(self):   
        random.shuffle(self.anim)
        self.playing = True
        for face in range(0,len(self.anim)):
            self.current_face = face
            time.sleep(0.3)
            
        time.sleep(5)
        self.playing = False