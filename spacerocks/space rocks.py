# this one looks much difficult than last py games!!
import pygame
from methods import SpaceShip, Astroid
from utils import load_sprite, get_random_pos, print_text


def init_pygame():
    pygame.init()
    pygame.display.set_caption("THE SPACE WAR")


class Spacerocks:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):

        init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""

        self.bullets = []
        self.spaceship = SpaceShip((400, 300), self.bullets.append)
        self.astroid = []

        for _ in range(6):
            while True:
                position = get_random_pos(self.screen)
                if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
                    break

            self.astroid.append(Astroid(position, self.astroid.append))

    def main_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def handle_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                quit()
            elif self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.spaceship.shoot()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def get_game_obj(self):
        game_obj = [*self.astroid, *self.bullets]
        if self.spaceship:
            game_obj.append(self.spaceship)
        return game_obj

    def process_game_logic(self):
        for game_object in self.get_game_obj():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.astroid:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.message = "You lost!"
                    break

        for bullet in self.bullets[:]:
            for astroid in self.astroid[:]:
                if astroid.collides_with(bullet):
                    self.astroid.remove(astroid)
                    self.bullets.remove(bullet)
                    astroid.split()
                    break

        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        if not self.astroid and self.spaceship:
            self.message = "You Won!"

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        # the screen u want to draw // the point u want to draw it
        for game_object in self.get_game_obj():
            game_object.draw(self.screen)

        if self.message:
            print_text(self.screen, self.message, self.font)

        pygame.display.flip()  # updates content of the screen
        self.clock.tick(60)


if __name__ == "__main__":
    space_rocks = Spacerocks()
    space_rocks.main_loop()
