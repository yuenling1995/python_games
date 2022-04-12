import pygame
import sys
from settings import Settings
import game_functions as gf
from character import Character
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():

	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)


	# make the play button.
	play_button = Button(ai_settings, screen, "Play")

	# make a character.
	character = Character(ai_settings, screen)
	#make bullets group.
	bullets = Group()

	#make balls group.
	balls = Group()
	#create a row of balls.
	gf.create_balls(ai_settings, screen, balls)

	#create an instance to store game statistics.
	stats = GameStats(ai_settings)

	# make a scoreboard 
	sb = Scoreboard(ai_settings, screen, stats)


	while True:
		gf.check_events(ai_settings, screen, stats, play_button, character, bullets, balls, sb)

		if stats.game_active:
			gf.update_balls(ai_settings, stats, screen, character, balls, bullets, sb)
			gf.update_bullets(ai_settings, screen, bullets, balls, stats, sb)

		gf.update_screen(ai_settings, screen, stats, character, bullets, balls, play_button, sb)




run_game()



