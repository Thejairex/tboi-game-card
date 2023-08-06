import random
import pygame
import pyganim


class Dice:
    def __init__(self, center) -> None:
        self.dice = [1, 2, 3, 4, 5, 6]
        self.index = random.randint(0, 5)
        self.center = center
        self.show = False

        self.anim_duration = 0
        self.anim_current = 0
        self.anim_playing = False
        
        self.result_duration = 0
        self.result_current = 0
        self.result_showing = False

    def load_resources(self):

        self.image = pygame.image.load("Resources/Images/dice.png")
        cara6 = self.image.subsurface(pygame.Rect(0, 0, 201, 200))
        cara5 = self.image.subsurface(pygame.Rect(207, 0, 201, 200))
        cara4 = self.image.subsurface(pygame.Rect(415, 0, 201, 200))
        cara3 = self.image.subsurface(pygame.Rect(0, 204, 201, 200))
        cara2 = self.image.subsurface(pygame.Rect(207, 204, 201, 200))
        cara1 = self.image.subsurface(pygame.Rect(415, 204, 201, 200))

        self.faces = [(cara1, 1), (cara2 ,2), (cara3, 3), (cara4, 4), (cara5, 5), (cara6, 6)]
        self.reroll()
        self.change_index()

        self.anim = pyganim.PygAnimation(
            [(cara1, 100), (cara2, 100), (cara3, 100), (cara4, 100), (cara5, 100), (cara6, 100)])
        rect = cara1.get_rect()
        self.center = self.center[0] - rect.width / \
            2, self.center[1] - rect.height/2

    def animation(self):
        if not self.anim_playing and not self.result_showing:
            self.reroll()
            self.change_index()
            self.anim_duration = (pygame.time.get_ticks() + 1500) // 1000
            self.anim_playing = True
            self.anim.play()
            
        self.anim_current = pygame.time.get_ticks() // 1000
        
        if self.anim_current == self.anim_duration:
            # self.show = False
            self.anim_playing = False
            self.anim.stop()

    def result(self, screen: pygame.Surface):
        if not self.anim_playing and not self.result_showing:
            self.result_duration = (pygame.time.get_ticks() + 1000) // 1000
            self.result_showing = True
            
        self.result_current = pygame.time.get_ticks() // 1000
        
        if self.result_current == self.result_duration:
            self.result_showing = False
            self.show = False
            print("Resultado del dado: ", self.faces[self.index][1])
            
        else:
            screen.blit(self.faces[self.index][0], self.center)
            

    def reroll(self):
        random.shuffle(self.faces)

    def change_index(self):
        self.index = random.randint(0, 5)

    def draw_dice(self, screen: pygame.Surface):
        self.animation()

        self.anim.blit(screen, self.center)
