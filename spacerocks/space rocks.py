# this one looks much difficult than last py games!!
import pygame
from methods import GameObject, SpaceShip
from utils import load_sprite


class Spacerocks:
    def __init__(self):
        self.init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        # controls game speed
        self.spaceship = SpaceShip((400, 300))
        self.astroid = GameObject((400, 300), load_sprite("asteroid"), (1, 0))

    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption("THE space war")

    def handle_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE)):
                quit()

    def process_game_logic(self):
        self.spaceship.move()
        self.astroid.move()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        # the screen u want to draw // the point u want to draw it
        self.spaceship.draw(self.screen)
        self.astroid.draw(self.screen)
        pygame.display.flip()  # updates content of the screen
        self.clock.tick(60)


if __name__ == "__main__":
    space_rocks = Spacerocks()
    space_rocks.main_loop()
