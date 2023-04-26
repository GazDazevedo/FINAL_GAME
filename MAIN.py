#Created by Daniel Azevedo

import pygame as pg
import os

from SETTING import *
from sprites import *

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)

    def new(self):
        # starting a new game
        self.all_sprites = pg.sprite.Group()
        self.wall = pg.sprite.Group()
        self.bad = pg.sprite.Group()
        self.good = pg.sprite.Group()
        self.workers = pg.sprite.Group()
        self.building = pg.sprite.Group()
        self.knights = pg.sprite.Group()
        self.calvary = pg.sprite.Group()
        self.spearmen = pg.sprite.Group()
        self.gunmen = pg.sprite.Group()
        self.turrent = pg.sprite.Group()
        self.mud = pg.sprite.Group()
        self.tank = pg.sprite.Group()

    def draw(self):
         self.screen.fill(BLUE)
         self.all_sprites.draw(self.screen)
            # is this a method or a function?
         pg.display.flip()  

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def update(self):
        print()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False


            
    
    

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()