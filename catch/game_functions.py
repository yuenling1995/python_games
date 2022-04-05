import sys
import pygame
from ball import Ball 
from random import randint


def check_keydown_events(event, character):
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_RIGHT:
		character.moving_right = True
	elif event.key == pygame.K_LEFT:
		character.moving_left = True


def check_keyup_events(event, character):
	if event.key == pygame.K_RIGHT:
		character.moving_right = False
	elif event.key == pygame.K_LEFT:
		character.moving_left = False


def check_events(character):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, character)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, character)


def update_screen(ai_settings, screen, character, balls):
	screen.fill(ai_settings.bg_color)

	character.blitme()

	balls.draw(screen)

	pygame.display.flip()


def create_balls(ai_settings, screen, balls):
	ball = Ball(ai_settings, screen)
	random_num = randint(1,3)
	available_space_x = ai_settings.screen_width -  2 * ball.rect.width
	number_ball_x = int(available_space_x / (2 * ball.rect.width))

	for ball_number in range(number_ball_x):
		ball = Ball(ai_settings, screen)
		ball.x = ball.rect.width + random_num * ball_number * ball.rect.width
		ball.rect.x = ball.x 
		balls.add(ball)




def update_character(character):
	character.update()


def update_ball(ai_settings, screen, balls, character):
	balls.update()

	if len(balls) == 0:
		create_balls(ai_settings, screen, balls)

	for ball in balls:
		if pygame.sprite.spritecollide(character, balls, True): 
			balls.remove(ball)













