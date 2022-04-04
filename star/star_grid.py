import pygame
import sys
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from star import Star



def run_game():

	# initiate pygame
	pygame.init()
	ai_settings = Settings()
	#create a screen
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	# create a group of stars
	stars = Group()
	gf.create_star(ai_settings, screen, stars)


	while True:
		gf.check_events()
		gf.update_screen(ai_settings, screen, stars)



run_game()