# Importing and Initializing pygame library
import pygame
import random

pygame.init()

# Setting some global variables
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Initializing display and screen
width, height = 800, 600
screen = pygame.display.set_mode(size=(width, height))

# Define Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, player_width, player_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([player_width, player_height])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < width - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < height - self.rect.height:
            self.rect.y += self.speed

# Define Laser Class
class Laser(pygame.sprite.Sprite):
    def __init__(self, color, laser_width, laser_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([laser_width, laser_height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.speed = 1
        self.timer = 2000
        self.fired_time = 0
        self.laser_been_placed = False

    def update(self):
        keys = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE] and not self.laser_been_placed:
            self.rect.y = player.rect.y
            self.rect.x = player.rect.x
            self.laser_been_placed = True
            self.fired_time = current_time

        if self.laser_been_placed:
            self.rect.y -= self.speed

            if current_time - self.fired_time >= self.timer:
                self.kill()
                self.laser_been_placed = False

# Declaring variables for enemy
enemy_w = 30
enemy_h = 30
enemy_left = random.randint(0, (width - enemy_w))
enemy_top = random.randint(0, (height - enemy_h))
enemy_rect = pygame.Rect(enemy_left, enemy_top, enemy_w, enemy_h)

# Variables for platforms
platform1_w = 200
platform1_h = 30
platform1_left = 400
platform1_top = 300

platform2_w = 200
platform2_h = 30
platform2_left = 200
platform2_top = 200

all_sprites = pygame.sprite.Group()
player = Player(blue, 30, 30)
laser = Laser(red, 10, 30)

all_sprites.add(player)
all_sprites.add(laser)

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(black)

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
