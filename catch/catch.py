import sys
import pygame
from settings import Settings
import game_functions as gf
from character import Character
from pygame.sprite import Group



def run_game():

	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	#create a character, ball
	character = Character(ai_settings, screen)
	balls = Group()

	gf.create_balls(ai_settings, screen, balls)


	while True:
		gf.check_events(character)
		gf.update_character(character)
		gf.update_ball(ai_settings, screen, balls, character)


		gf.update_screen(ai_settings, screen, character, balls)




run_game()
