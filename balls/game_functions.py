import sys
import pygame
from bullets import Bullet
from ball import Ball
from time import sleep


def check_keydown_events(event, ai_settings, screen, stats, character, bullets, balls):
	if event.key == pygame.K_LEFT:
		character.moving_left = True
	elif event.key == pygame.K_RIGHT:
		character.moving_right = True
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		after_button_click(ai_settings, screen, stats, character, bullets, balls)
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, character, bullets)


def fire_bullet(ai_settings, screen, character, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, character)
		bullets.add(new_bullet)


def check_keyup_events(event, character):
	if event.key == pygame.K_LEFT:
		character.moving_left = False
	elif event.key == pygame.K_RIGHT:
		character.moving_right = False



def check_events(ai_settings, screen, stats, play_button, character, bullets, balls, sb):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, play_button, character, bullets, balls, mouse_x, mouse_y, sb)

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, stats, character, bullets, balls)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, character)


def check_play_button(ai_settings, screen, stats, play_button, character, bullets, balls, mouse_x, mouse_y, sb):
	button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_click and not stats.game_active:
		after_button_click(ai_settings, screen, stats, character, bullets, balls, sb)


def after_button_click(ai_settings, screen, stats, character, bullets, balls, sb):
	pygame.mouse.set_visible(False)

	#reset the game stats
	stats.reset_stats()
	ai_settings.initialize_dynamic_settings()
	stats.game_active = True 

	# reset the scoreboard images.
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()


	# empty the group of bullets and balls.
	bullets.empty()
	balls.empty()

	# create a new rows of balls and center the character
	create_balls(ai_settings, screen, balls)
	character.center_character()


def update_screen(ai_settings, screen, stats, character, bullets, balls, play_button, sb):
	screen.fill(ai_settings.bg_color)

	character.blitme()
	update_character(character)


	# draw the whole group of bullets onto the screen.
	bullets.draw(screen)


	#draw the group of balls onto the screen
	balls.draw(screen)

	# show the scoreboard
	sb.show_score()

	if not stats.game_active:
		play_button.draw_button()

	pygame.display.flip()


def update_character(character):
	character.update()


def update_bullets(ai_settings, screen, bullets, balls, stats, sb):
	bullets.update()

	remove_old_bullets(bullets)
	check_bullet_ball_collisions(ai_settings, screen, bullets, balls, stats, sb)


def check_bullet_ball_collisions(ai_settings, screen, bullets, balls, stats, sb):
	# check for any bullets that have hit aliens.
	# if so, get rid of the bullet and the alien.
	collisions = pygame.sprite.groupcollide(bullets, balls, False, True)

	if collisions:
		for balls in collisions.values():
			stats.score += ai_settings.ball_points * len(balls)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(balls) == 0:
		bullets.empty()

		#increase the game speed
		ai_settings.increase_speed()

		#increase game level
		stats.level += 1
		sb.prep_level()

		create_balls(ai_settings, screen, balls)


def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score 
		sb.prep_high_score()


def remove_old_bullets(bullets):
	#remove bullets that are off the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def create_balls(ai_settings, screen, balls):
	available_space_x = ai_settings.screen_width - 3 * ai_settings.ball_width
	number_balls_x = int(available_space_x / (3 * ai_settings.ball_width))

	for ball_number in range(number_balls_x):
		ball = Ball(ai_settings, screen)
		ball.x = 3 * ball.rect.width + 3 * ball.rect.width * ball_number
		ball.rect.x = ball.x
		balls.add(ball)




def update_balls(ai_settings, stats, screen, character, balls, bullets, sb):
	balls.update()

	if pygame.sprite.spritecollideany(character, balls):
		character_hit(ai_settings, stats, screen, character, balls, bullets, sb)

	check_balls_bottom(ai_settings, stats, screen, character, balls, bullets, sb)


def character_hit(ai_settings, stats, screen, character, balls, bullets, sb):
	""" respond to character being hit by balls."""
	#decrement characters left.
	if stats.character_left > 0:
		stats.character_left -= 1

		# update scoreboard
		sb.prep_people()

		# empty the lsit of balls and bullets.
		bullets.empty()
		balls.empty()

		# create a new row of balls and center the character.
		create_balls(ai_settings, screen, balls)
		character.center_character()

		# pause.
		sleep(0.5)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_balls_bottom(ai_settings, stats, screen, character, balls, bullets, sb):
	""" check if any balls have reached the bottom of screen."""
	screen_rect = screen.get_rect()

	for ball in balls.sprites():
		if ball.rect.bottom >= screen_rect.bottom:
			# treat this the same as if the character got hit.
			character_hit(ai_settings, stats, screen, character, balls, bullets, sb)
			break








