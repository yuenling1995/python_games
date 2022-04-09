import pygame
import sys
from settings import Settings
import game_functions as gf
from target import Target
from person import Person
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():

	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	# create a play button.
	play_button = Button(ai_settings, screen, "Play")

	# create a game stats instance
	stats = GameStats(ai_settings)

	# create a target.
	target = Target(ai_settings, screen)

	#create a person
	person = Person(ai_settings, screen)

	#create a group of bullets.
	bullets = Group()


	while True:

		gf.check_events(ai_settings, screen, person, bullets, stats, play_button)
		if stats.game_active:
			gf.update_target(target)
			gf.update_person(person)
			gf.update_bullets(ai_settings, bullets, target, stats)


		gf.update_screen(ai_settings, screen, target, person, bullets, play_button)




run_game()