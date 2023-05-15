#File created by Daniel Azevedo

# import libs
import pygame as pg
import os
# import settings 
from SETTING import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
# create game class in order to pass properties to the sprites file
'''
Goals:

Multiple Choices

Images for events

Multiple outcomes

Mini game

Different events

'''


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
        King_image = pg.image.load(os.path.join(game_folder, 'king.jpg')).convert()
        King_image_rect = King_image.get_rect()
        King_image_rect.x = 330
        King_image_rect.y = 100
        self.screen.blit(King_image, King_image_rect)

    def new(self):
        # starting a new game
        self.score = 0
        self.dead = False
        self.numchoices = 3
        self.Turn = 1
        self.stability = 100
        self.courtopinion = 100
        self.gold = 100
        self.badomens = 0
        self.military = 0
        self.run()
        
        
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
        


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
                            
    def draw(self):
        if self.dead == False:
            self.screen.fill(DARKGREEN)
            King_image = pg.image.load(os.path.join(game_folder, 'king.jpg')).convert()
            King_image_rect = King_image.get_rect()
            King_image_rect.x = 50
            King_image_rect.y = 100
            Textbox_image = pg.image.load(os.path.join(game_folder, 'Textbox.jpg')).convert()
            Textbox_image_rect = Textbox_image.get_rect()
            Textbox_image_rect.x = 350
            Textbox_image_rect.y = 50
            Stats_image = pg.image.load(os.path.join(game_folder, 'Statsandeffects.jpg')).convert()
            Stats_image_rect = Stats_image.get_rect()
            Stats_image_rect.x = 55
            Stats_image_rect.y = 390
            self.screen.blit(King_image, King_image_rect)
            self.screen.blit(Textbox_image, Textbox_image_rect)
            self.screen.blit(Stats_image, Stats_image_rect)
            self.draw_text("Stability: ", 40, BLACK, 1200, 500)
            self.draw_text("Court: ", 40, BLACK, 1200, 600)
            self.draw_text("Gold: ", 40, BLACK, 1200, 700)
            
            if self.numchoices >= 1:
                Choices_image = pg.image.load(os.path.join(game_folder, 'Choices.jpg')).convert()
                Choices_image_rect = Choices_image.get_rect()
                Choices_image_rect.x = 400
                Choices_image_rect.y = 420
                self.screen.blit(Choices_image, Choices_image_rect)
                if self.numchoices >= 2:
                    Choices2_image = pg.image.load(os.path.join(game_folder, 'Choices.jpg')).convert()
                    Choices2_image_rect = Choices2_image.get_rect()
                    Choices2_image_rect.x = 400
                    Choices2_image_rect.y = 575
                    self.screen.blit(Choices2_image, Choices2_image_rect)
                    if self.numchoices >= 3: 
                        Choices3_image = pg.image.load(os.path.join(game_folder, 'Choices.jpg')).convert()
                        Choices3_image_rect = Choices2_image.get_rect()
                        Choices3_image_rect.x = 400
                        Choices3_image_rect.y = 730
                        self.screen.blit(Choices3_image, Choices3_image_rect)
            if self.Turn == 1:
                self.draw_text("You are the ruler of the Great Kingdom of Bellarmine", 40, BLACK, 800, 200)
                self.draw_text("Great! Tell me about it would you?", 30, BLACK, 650, 450)
                self.draw_text("What am I doing?", 30, BLACK, 650, 600)
                self.draw_text("I already know", 30, BLACK, 650, 800)
            if self.Turn == 2:
                self.draw_text("I'm no historian", 40, BLACK, 800, 200)
                self.draw_text("You're fired", 30, BLACK, 650, 450)
            if self.Turn == 3:
                self.draw_text("Keep the kingdom alive, if a value is 0, you lose", 30, BLACK, 800, 200)
                self.draw_text("You're not very helpful", 30, BLACK, 650, 450)
            if self.Turn == 4: 
                self.draw_text("Now it is time to make your military", 30, BLACK, 800, 200)
                self.draw_text("Knights: High cost, great ability, good court", 30, BLACK, 650, 450)
                self.draw_text("Peasants: No cost, not the best, bad court opinion", 30, BLACK, 650, 600)
                self.draw_text("Mercenaries: Medium cost, decent, untrustorthy", 30, BLACK, 650, 800)
            if self.Turn == 5:
                self.draw_text("Now it is time to make your court", 30, BLACK, 800, 200)
                self.draw_text("Jesters: Low cost, insane, easy to please", 30, BLACK, 650, 450)
                self.draw_text("Nobles: Hight cost, competent, content", 30, BLACK, 650, 600)
                self.draw_text("Democracy? Not in my kingdom", 30, BLACK, 650, 800)

                        
        else:
            self.screen.fill(BLUE)
            # is this a method or a function?
        pg.display.flip()  

    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_r:
                    self.dead = False
                    g = Game()
                    g.new()
            if event.type == pg.MOUSEBUTTONUP:
                pg.mouse.get_pos
                self.mouse_coords = pg.mouse.get_pos()
                if self.Turn == 1:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.mouse_coords = 0,0
                        self.Turn = 2
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.mouse_coords = 0,0
                        self.Turn = 3
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.mouse_coords = 0,0
                        self.Turn = 4
                if self.Turn == 2:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.mouse_coords = 0,0
                        self.Turn = 4
                if self.Turn == 3:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.mouse_coords = 0,0
                        self.Turn = 4
                if self.Turn == 4:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 10
                        self.courtopinion = self.courtopinion + 5
                        self.military = 3
                        self.mouse_coords = 0,0
                        self.Turn = 5
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.courtopinion = self.courtopinion - 10
                        self.military = 1
                        self.mouse_coords = 0,0
                        self.Turn = 5
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.stability = self.stability - 10
                        self.military = 2
                        self.mouse_coords = 0,0
                        self.Turn = 5
                if self.Turn == 5:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.courtopinion = self.courtopinion + 20
                        self.stability = self.stability - 25
                        self.mouse_coords = 0,0
                        self.Turn = 6
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 20
                        self.stability = self.stability + 20
                        self.mouse_coords = 0,0
                        self.Turn = 6
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 50
                        self.courtopinion = 1000
                        self.mouse_coords = 0,0
                        self.Turn = 6
    def update(self):
        self.draw()


# instantiate the game class...
g = Game()
g.new()
# kick off the game loop


pg.quit()