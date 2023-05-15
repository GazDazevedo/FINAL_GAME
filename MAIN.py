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

    def load_data(self):
        self.ranged_img = pg.image.load(path.join(img_folder, "bellar_man_single_frm.png")).convert()
        self.leader_img = pg.image.load(path.join(img_folder, "bellar_man_single_frm.png")).convert()
        self.savage_img = pg.image.load(path.join(img_folder, "bellar_man_single_frm.png")).convert()
        self.builder_img = pg.image.load(path.join(img_folder, "bellar_man_single_frm.png")).convert()
        self.resource = pg.image.load(path.join(img_folder, "bellar_man_single_frm.png")).convert()

    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.ranged = pg.sprite.Group()
        self.leader = pg.sprite.Group()
        self.savage = pg.sprite.Group()
        self.building = pg.sprite.Group()
        self.builder = pg.sprite.Group()
        self.resource = pg.sprite.Group()
        self.head = pg.sprite.Group()
       
        self.run()

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
        self.all_sprites.update()
            
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            
    
    

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()