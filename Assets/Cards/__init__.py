import pygame

class Card:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple) -> None:
        self.x = x
        self.y = y
        self.x_temp = x
        self.y_temp = y
        self.width = width
        self.height = height
        self.space = (76, 104)
        self.list_card = []
        self.color = color
        
    def draw(self, screen):
        for rect in self.list_card:
            pygame.draw.rect(screen, self.color, rect)
        
class PlayerCard(Card):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, negative: bool) -> None:
        super().__init__(x, y, width, height, color )
        self.negative = negative
        
    def add_player_card(self):
        if len(self.list_card) < 12:
            self.list_card.append(pygame.Rect(self.x_temp, self.y_temp, self.width, self.height))
            if self.negative:
                self.x_temp -= self.space[0]
            else:
                self.x_temp += self.space[0]
            
            if len(self.list_card) == 7:
                if self.negative:
                    self.y_temp -= self.space[1]
                    self.x_temp = self.x
                    self.x_temp -= self.space[0] * 2
                else:
                    self.y_temp += self.space[1]
                    self.x_temp = self.x
                    self.x_temp += self.space[0] * 2