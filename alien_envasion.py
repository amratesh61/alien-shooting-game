import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from points import Scoreboard

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(("battleship"))
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings,screen)
    alien =Alien(ai_settings,screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:   
            ship.update()
        
            gf.update_aliens(ai_settings,stats,sb,screen, ship , aliens,bullets)
        
        gf.update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button)
        gf.update_bullets(ai_settings,screen,stats,sb, ship,aliens,bullets)
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pygame.display.flip()

run_game()