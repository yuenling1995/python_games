import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	# draw a ship.
	ship = Ship(ai_settings, screen)
	# make a group to store bullets in.
	bullets = Group()



	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		# update ship position with keypresses
		ship.update()
		# update bullet position with keypresses
		bullets.update()

		# remove old bullets
		gf.remove_old_bullets(ai_settings, bullets)

		gf.update_screen(ai_settings, screen, ship, bullets)



run_game()