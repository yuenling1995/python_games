import sys
import pygame
from raindrop import Raindrop



def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()


def update_screen(ai_settings, screen, raindrops):
	screen.fill(ai_settings.bg_color)

	raindrops.draw(screen)

	pygame.display.flip()


def get_number_raindrop_x(ai_settings, raindrop_width):
	available_space_x = ai_settings.screen_width - 2 * raindrop_width
	number_raindrop_x = int(available_space_x / (2 * raindrop_width))
	return number_raindrop_x


def get_row_number(ai_settings, raindrop_height):
	available_space_y = ai_settings.screen_height - 2 * raindrop_height
	row_number = int(available_space_y / (2 * raindrop_height))
	return row_number 


def raindrop_position(ai_settings, screen, raindrops, raindrop_number, row_number):
	raindrop = Raindrop(ai_settings, screen)
	raindrop.x = raindrop.rect.width + 2 * raindrop_number * raindrop.rect.width
	raindrop.rect.x = raindrop.x 

	raindrop.y = raindrop.rect.height + 2 * row_number * raindrop.rect.height
	raindrop.rect.y = raindrop.y 
	raindrops.add(raindrop)	


def create_raindrops(ai_settings, screen, raindrops):
	raindrop = Raindrop(ai_settings, screen)
	number_raindrop_x = get_number_raindrop_x(ai_settings, raindrop.rect.width)
	number_rows = get_row_number(ai_settings, raindrop.rect.height)


	for row_number in range(number_rows):
		for raindrop_number in range(number_raindrop_x):
			raindrop_position(ai_settings, screen, raindrops, raindrop_number, row_number)


def update_raindrops(raindrops):
	""" update the positions of all raindrops."""
	raindrops.update()















