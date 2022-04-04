import sys
import pygame
from star import Star
from random import randint


def check_keydown_events(event):
	if event.key == pygame.K_q:
		sys.exit()


def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event)


def update_screen(ai_settings, screen, stars):
	screen.fill(ai_settings.bg_color)

	stars.draw(screen)

	# Make the most recently drawn screen visible.
	pygame.display.flip()


def get_number_star_x(ai_settings, star_width):
	available_space_x = ai_settings.screen_width - 2 * star_width
	number_star_x = int(available_space_x / (star_width))
	return number_star_x


def get_row_number(ai_settings, star_height):
	available_space_y = ai_settings.screen_height - 2 * star_height
	row_number = int(available_space_y / (star_height))
	return row_number


def add_star(ai_settings, screen, stars, star_number, row_number):
	star = Star(ai_settings, screen)
	#star.x = 2 * star.rect.width * star_number 
	random_num = randint(1,4)
	star.x = random_num * star.rect.width * star_number
	star.rect.x = star.x 

	star.y = random_num * star.rect.height * row_number 
	star.rect.y = star.y 
	stars.add(star)


def create_star(ai_settings, screen, stars):
	star = Star(ai_settings, screen)
	number_star_x = get_number_star_x(ai_settings, star.rect.width)
	number_rows = get_row_number(ai_settings, star.rect.height)
	print(number_rows)

	for row_number in range(number_rows):
		for star_number in range(number_star_x):
			add_star(ai_settings, screen, stars, star_number, row_number)



