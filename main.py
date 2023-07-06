import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.inGame = False
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.size = (self.screen.get_width(), self.screen.get_height())
        pygame.display.set_caption("The binding of isaac Four Souls")
        info = pygame.display.Info()
        self.bg = pygame.image.load("Resources/Images/table.png")
        self.bg = pygame.transform.scale(self.bg, self.size)

    def run(self):
        self.inGame = True
        while self.inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inGame = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.inGame = False

            pygame.display.flip()
            self.screen.blit(self.bg, (0,0))


if __name__ == "__main__":
    game = Game()
    game.run()
