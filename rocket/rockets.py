import pygame
from rocket_settings import Settings
from rocket import Rocket
import rocket_gf as gf



def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.caption)

	# Make a rocket.
	rocket = Rocket(ai_settings, screen)

	# Start the main loop for the game.
	while True:

		# Watch for keyboard and mouse events.
		gf.check_events(rocket)
		rocket.update()
		gf.update_screen(ai_settings, screen, rocket)


run_game()