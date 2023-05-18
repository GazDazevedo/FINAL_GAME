#By Daniel Azevedo
import pygame as pg
import os
# import settings 

# from pg.sprite import Sprite

# set up assets folders
pg.init()


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
WIDTH = 1440
HEIGHT = 900
BLUE = 100,100,100
BLACK = 200,10,200
DARKGREEN = 84, 183, 92
FPS = 30
screen = pg.display.set_mode((WIDTH, HEIGHT))
Choices_image = pg.image.load(os.path.join(game_folder, 'Choices.jpg')).convert()
Choices_image_rect = Choices_image.get_rect()
Choices_image_rect.x = 400
Choices_image_rect.y = 420
Choices2_image = pg.image.load(os.path.join(game_folder, 'Choices.jpg')).convert()
Choices2_image_rect = Choices2_image.get_rect()
Choices2_image_rect.x = 400
Choices2_image_rect.y = 575
Choices3_image = pg.image.load(os.path.join(game_folder, 'Choices.jpg')).convert()
Choices3_image_rect = Choices2_image.get_rect()
Choices3_image_rect.x = 400
Choices3_image_rect.y = 730