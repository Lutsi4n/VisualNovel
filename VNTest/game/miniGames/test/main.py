import pygame
import random
import os
from os import path

# Define the screen size
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

img_pl1 = path.join(path.dirname(__file__), 'player1.png')
img_pl2 = path.join(path.dirname(__file__), 'player2.png')

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the game window caption
pygame.display.set_caption("Fighting Game")

# Define the colors used in the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.speed = 5

    def death(self, folder):
        folder.remove(self)

    def update(self):
        pass

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def attack(self, other_player):
        damage = random.randint(5, 20)
        other_player.health -= damage
        print(f"{self} attacked {other_player} for {damage} damage!" + f"Жизни у врага -  {other_player.health}")

    def __str__(self):
        return f"Player ({self.rect.x}, {self.rect.y})"

# Create the player sprites
player1 = Player(50, SCREEN_HEIGHT/2, img_pl1)
player2 = Player(SCREEN_WIDTH - 100, SCREEN_HEIGHT/2, img_pl2)

# Add the player sprites to a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2)


def run_game():
    # Main game loop
    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle player 1 movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1.move_left()
        if keys[pygame.K_RIGHT]:
            player1.move_right()
        if keys[pygame.K_UP]:
            player1.move_up()
        if keys[pygame.K_DOWN]:
            player1.move_down()

        # Handle player 2 movement
        if keys[pygame.K_a]:
            player2.move_left()
        if keys[pygame.K_d]:
            player2.move_right()
        if keys[pygame.K_w]:
            player2.move_up()
        if keys[pygame.K_s]:
            player2.move_down()

        # Handle player attacks
        if keys[pygame.K_SPACE]:
            player1.attack(player2)
        if keys[pygame.K_RETURN]:
            player2.attack(player1)
        if  player2.health <= 0:
            player2.death(all_sprites)
        if player1.health <= 0:
            player1.death(all_sprites)

        if player1.health <= 0 or player2.health <= 0:
            running = False
            return

        # Draw the screen
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.update()

    # Quit Pygame
    pygame.quit()

run_game()
