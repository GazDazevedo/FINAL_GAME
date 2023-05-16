#File created by Daniel Azevedo

# import libs
from random import *
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
        self.money = 0
        self.nocourt = False
        self.chance = 0
        self.moneychance = 0
        self.Outcome = 0
        self.Victory = False
        self.Failure = False
        self.hasvalue = False
        self.run()
        
    def comp_choice(self):
        #Returns random value between 0 and 2
        return (randint(1,10))
    
    def milchance(self):
        self.anti = (randint(1,10))
        if self.anti > (2 + self.military):
            self.Outcome = 1
            print(self.anti)
        if self.anti < (2 + self.military):
            self.Outcome = 2
            print(self.anti)
        
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
            self.draw_text("Stability: " + str(self.stability), 40, BLACK, 1200, 500)
            if self.nocourt == False:
                self.draw_text("Court: " + str(self.courtopinion), 40, BLACK, 1200, 600)
            self.draw_text("Gold: " + str(self.gold), 40, BLACK, 1200, 700)
            
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
            if self.Turn == 6:
                self.draw_text("Choose your right hand", 30, BLACK, 800, 200)
                self.draw_text("Queen: No cost, corrupt, good with money", 30, BLACK, 650, 450)
                self.draw_text("The Marshall: Hight cost, good military, iron fist", 30, BLACK, 650, 600)
                self.draw_text("Jeff: Everyone loves jeff the jeff", 30, BLACK, 650, 800)
            if self.Turn >= 7 and self.Turn < 13:
                if self.hasvalue == False:
                    self.chance = self.comp_choice()
                    self.hasvalue = True
                if self.chance == 1:
                        self.draw_text("The Harvest has failed this month my Lord!", 30, BLACK, 800, 200)
                        self.draw_text("Send relief to the peasants!", 30, BLACK, 650, 450)
                        self.draw_text("Who cares as long as the taxes are paid!", 30, BLACK, 650, 600)
                        self.draw_text("Tell the nobles to handle it!", 30, BLACK, 650, 800) 

                if self.chance == 2:
                        self.draw_text("Bandits from the north my Lord", 30, BLACK, 800, 200)
                        self.draw_text("Send the legions, I want their heads!", 30, BLACK, 650, 450)
                        self.draw_text("They're only raiding Gilbert, I don't like him anyway!", 30, BLACK, 650, 600)
                        self.draw_text("Bandits only want gold, negotiate will you!", 30, BLACK, 650, 800) 
                        
                if self.chance == 3:
                        self.draw_text("Our Southern ally is under attack!", 30, BLACK, 800, 200)
                        self.draw_text("Send the Legion out, it'll be a short war", 30, BLACK, 650, 450)
                        self.draw_text("Send some money, everyone can use some money!", 30, BLACK, 650, 600)
                        self.draw_text("They're weak, why not invade them ourselves?", 30, BLACK, 650, 800) 
                     
                if self.chance == 4:
                        self.draw_text("Jeff has run out of entertainment my King!", 30, BLACK, 800, 200)
                        self.draw_text("That's terrible, send the military band", 30, BLACK, 650, 450)
                        self.draw_text("I'll throw him a feast!", 30, BLACK, 650, 600)
                        self.draw_text("Why do I care?", 30, BLACK, 650, 800) 
                     
                if self.chance == 5:
                        self.draw_text("The nobles are fighting again my King!", 30, BLACK, 800, 200)
                        self.draw_text("Let them, the strong eat the weak!", 30, BLACK, 650, 450)
                        self.draw_text("I think they just want some gold!", 30, BLACK, 650, 600)
                        self.draw_text("It's time for some good federal intervention!", 30, BLACK, 650, 800) 
                       
                if self.chance == 6:
                        self.draw_text("A witch has been sighted in the Village of Scon", 30, BLACK, 800, 200)
                        self.draw_text("Witches, no such thing! Now where is the Dragon?", 30, BLACK, 650, 450)
                        self.draw_text("Great, go buy me some potions would you?", 30, BLACK, 650, 600)
                        self.draw_text("Fire is always a good solution!", 30, BLACK, 650, 800) 
                    
                if self.chance == 7:
                        self.draw_text("A new war horse is avabile my King", 30, BLACK, 800, 200)
                        self.draw_text("Buy it, I love horses", 30, BLACK, 650, 450)
                        self.draw_text("Buy it, Jeff loves horses", 30, BLACK, 650, 600)
                        self.draw_text("Horses smell, I need a Dragon", 30, BLACK, 650, 800) 
              
                if self.chance == 8:
                        self.draw_text("The Kingdom of Alac wants an alliance!", 30, BLACK, 800, 200)
                        self.draw_text("New friend? Of course!", 30, BLACK, 650, 450)
                        self.draw_text("Only for defense, nothing more!", 30, BLACK, 650, 600)
                        self.draw_text("The Kingdom of Ala-what?", 30, BLACK, 650, 800)
            
                if self.chance == 9:
                        self.draw_text("A man claims to be your brother!", 30, BLACK, 800, 200)
                        self.draw_text("Find him a place in court!", 30, BLACK, 650, 450)
                        self.draw_text("Put him in-charge of the treasury", 30, BLACK, 650, 600)
                        self.draw_text("How did John find me again? Send him to Siberia!", 30, BLACK, 650, 800) 
         
                if self.chance == 10:
                        self.draw_text("A fire in the castle has broken out my Lord!", 30, BLACK, 800, 200)
                        self.draw_text("Call upon the royal firefighters!", 30, BLACK, 650, 450)
                        self.draw_text("Throw gold at it, gold fixes everything!", 30, BLACK, 650, 600)
                        self.draw_text("This is fine", 30, BLACK, 650, 800)
             
                if self.chance == 2 and self.Failure == True:
                        self.draw_text("Our legions have failed to kill the Bandits", 30, BLACK, 800, 200)
                        self.draw_text("They are useless", 30, BLACK, 650, 450)
                   
                if self.chance == 2 and self.Victory == True:
                        self.draw_text("Our legions have driven the Bandits out ", 30, BLACK, 800, 200)
                        self.draw_text("I'm a great general", 30, BLACK, 650, 450)
                      
                if self.chance == 4 and self.Failure == True:
                        self.draw_text("The band played Jeff's least favorite song", 30, BLACK, 800, 200)
                        self.draw_text("How could they?", 30, BLACK, 650, 450)
                      
                if self.chance == 4 and self.Victory == True:
                        self.draw_text("Jeff loved the parade", 30, BLACK, 800, 200)
                        self.draw_text("He is so great", 30, BLACK, 650, 450)
                     
                if self.chance == 5 and self.Victory == True:
                        self.draw_text("Our forces end the fighting", 30, BLACK, 800, 200)
                        self.draw_text("Suprise Dictatorship", 30, BLACK, 650, 450)
                   
                if self.chance == 5 and self.Failure == True:
                        self.draw_text("The intervention didn't go so well", 30, BLACK, 800, 200)
                        self.draw_text("Why?", 30, BLACK, 650, 450)
    
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
                        self.hasvalue = False
                        self.Turn = 2
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.hasvalue = False
                        self.mouse_coords = 0,0
                        self.Turn = 3
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.hasvalue = False
                        self.mouse_coords = 0,0
                        self.Turn = 4
                if self.Turn == 2:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.hasvalue = False
                        self.mouse_coords = 0,0
                        self.Turn = 4
                if self.Turn == 3:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 4
                if self.Turn == 4:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 10
                        self.courtopinion = self.courtopinion + 5
                        self.military = 3
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 5
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.courtopinion = self.courtopinion - 10
                        self.military = 1
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 5
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.stability = self.stability - 10
                        self.military = 2
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 5
                if self.Turn == 5:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.courtopinion = self.courtopinion + 20
                        self.stability = self.stability - 25
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 6
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 20
                        self.stability = self.stability + 20
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 6
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 50
                        self.nocourt = True
                        self.courtopinion = 1000
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 6
                if self.Turn == 6:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.money = 2
                        self.courtopinion = self.courtopinion - 10
                        self.stability = self.stability -5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 7
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 20
                        self.stability = self.stability + 20
                        self.military = self.military + 2
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = 7
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 50
                        self.mouse_coords = 0,0
                        self.Turn = 7
                if self.chance == 1:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 10
                        self.stability = self.stability + 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold + 5
                        self.stability = self.stability - 15
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 10
                        self.courtopinion = self.courtopinion - 15
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 2:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.milchance()
                        if self.Outcome == 1:
                            self.Failure = True
                        if self.Outcome == 2:
                            self.Victory = True
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 15
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 10
                        self.gold = self.gold - 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 2 and self.Failure == True:
                    self.numchoices = 3
                    self.stability = self.stability - 10
                    self.courtopinion = self.courtopinion - 15
                    self.Failure = False
                    self.hasvalue = False
                    self.Turn = self.Turn + 1
                if self.chance == 2 and self.Victory == True:
                    self.numchoices = 3
                    self.stability = self.stability + 10
                    self.courtopinion = self.courtopinion + 5
                    self.Victory = False
                    self.hasvalue = False
                    self.Turn = self.Turn + 1
                if self.chance == 3:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.courtopinion = self.courtopinion + 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 15
                        self.courtopinion = self.courtopinion - 15
                        self.gold = self.gold + 20
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 4:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.milchance()
                        if self.Outcome == 1:
                            self.Failure = True
                        if self.Outcome == 2:
                            self.Victory = True
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.stability = self.stability + 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 4 and self.Failure == True:
                    self.numchoices = 3
                    self.stability = self.stability - 10
                    self.courtopinion = self.courtopinion - 5
                    self.Failure = False
                    self.hasvalue = False
                    self.Turn = self.Turn + 1
                if self.chance == 4 and self.Victory == True:
                    self.numchoices = 3
                    self.stability = self.stability + 10
                    self.courtopinion = self.courtopinion + 10
                    self.Victory = False
                    self.hasvalue = False
                    self.Turn = self.Turn + 1
                if self.chance == 5:
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 1
                        self.milchance()
                        if self.Outcome == 1:
                            self.Failure = True
                        if self.Outcome == 2:
                            self.Victory = True
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 10
                        self.stability = self.stability + 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 15
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 5 and self.Failure == True:
                    self.numchoices = 3
                    self.stability = self.stability - 20
                    self.courtopinion = self.courtopinion - 5
                    self.Failure = False
                    self.hasvalue = False
                    self.Turn = self.Turn + 1
                if self.chance == 5 and self.Victory == True:
                    self.numchoices = 3
                    self.stability = self.stability + 10
                    self.courtopinion = self.courtopinion + 10
                    self.Victory = False
                    self.hasvalue = False
                    self.Turn = self.Turn + 1
                if self.chance == 6:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.stability = self.stability - 10
                        self.potions = True
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 10
                        self.courtopinion = self.courtopinion - 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 7:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 10
                        self.courtopinion = self.courtopinion + 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.stability = self.stability + 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 8:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.courtopinion = self.courtopinion + 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.courtopinion = self.courtopinion - 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 9:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.courtopinion = self.courtopinion + 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.money = self.money + 1
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.courtopinion = self.courtopinion - 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                if self.chance == 10:
                    if (Choices_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability + 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices2_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.gold = self.gold - 5
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
                    if (Choices3_image_rect.collidepoint(self.mouse_coords) == True):
                        self.numchoices = 3
                        self.stability = self.stability - 10
                        self.mouse_coords = 0,0
                        self.hasvalue = False
                        self.Turn = self.Turn + 1
    def update(self):
        self.draw()


# instantiate the game class...
g = Game()
g.new()
# kick off the game loop


pg.quit()