import pygame
import sys
from settings import Settings
import game_functions as gf
from pygame.sprite import Group



def run_game():

	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	raindrops = Group()
	new_raindrops = Group()
	
	gf.create_raindrops(ai_settings, screen, raindrops)



	while True:
		gf.check_events()
		gf.update_raindrops(raindrops)


		gf.update_screen(ai_settings, screen, raindrops)










run_game()