#Importing and Initializing pygame library
import pygame
import random
import os
pygame.init()

#Setting some global variables
width = 800
height = 600
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#Initializing display and screen#########################################################################
screen = pygame.display.set_mode(size=(width, height))
Background = pygame.image.load(os.path.join("grass_background.png"))

#Define Player Class###############################################################################
class Player(pygame.sprite.Sprite):
    def __init__(self ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("chicken.png"))
        self.rect = self.image.get_rect()
        self.speed = 5
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            
#Define Laser Class####################################################################################           
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
        
        if keys[pygame.K_SPACE]:
            self.rect.y = Player.rect.y
            self.rect.x = Player.rect.x

        self.rect.y -= self.speed

   
            
#Declaring variables for enemy#############################################################
enemy_w = 30
enemy_h = 30
enemy_left = random.randint(0, (width - enemy_w))
enemy_top = random.randint(0, (height - enemy_h))
Enemy = pygame.Rect(enemy_left, enemy_top, enemy_w, enemy_h)

#Variables for platforms##################################################################################
platform1_w = 200
platform1_h = 30
platform1_left = 400
platform1_top = 300

platform_1 = pygame.Rect(platform1_left, platform1_top, platform1_w, platform1_h)
    
platform2_w = 200
platform2_h = 30
platform2_left = 200
platform2_top = 200

platform_2 = pygame.Rect(platform2_left, platform2_top, platform2_w, platform2_h)

#Sprites##############################################################################################
all_sprites = pygame.sprite.Group()

Player = Player()
all_sprites.add(Player)

laser_been_placed = False
Laser = Laser(red, 10, 30)
all_sprites.add(Laser)


#Main Game Loop########################################################################################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
        
    screen.blit(Background, (0,0))

    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
