import sys
import pygame
from bullets import Bullets
from time import sleep



def check_keydown_events(event, ai_settings, screen, person, bullets):
	if event.key == pygame.K_UP:
		person.moving_up = True
	elif event.key == pygame.K_DOWN:
		person.moving_down = True
	elif event.key == pygame.K_SPACE:
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullets(ai_settings, screen, person)
			bullets.add(new_bullet)
	elif event.key == pygame.K_q:
		sys.exit()


def check_keyup_events(event, person):
	if event.key == pygame.K_UP:
		person.moving_up = False
	elif event.key == pygame.K_DOWN:
		person.moving_down = False


def check_events(ai_settings, screen, person, bullets, stats, play_button):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, person, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, person)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(bullets, stats, play_button, mouse_x, mouse_y)


def check_play_button(bullets, stats, play_button, mouse_x, mouse_y):
	# check if mouse position collide with the button.
	button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_click:
		pygame.mouse.set_visible(False)
		stats.game_active = True

		# empty the bullets
		bullets.empty()


def update_screen(ai_settings, screen, target, person, bullets, play_button):
	screen.fill(ai_settings.bg_color)

	play_button.draw_button()

	target.draw_target()
	person.blitme()

	# have to use this instead of bullets.draw(screen)
	#because it's a rect instead of an image
	for bullet in bullets.sprites():
		bullet.draw_bullets()

	pygame.display.flip()


def update_target(target):
	target.update()


def update_person(person):
	person.update()


def update_bullets(ai_settings, bullets, target, stats):
	bullets.update()
	remove_old_bullets(ai_settings, bullets)

	if pygame.sprite.spritecollideany(target, bullets):
		sleep(2)
		stats.game_active = False
		pygame.mouse.set_visible(True)


def remove_old_bullets(ai_settings, bullets):
	for bullet in bullets.copy():
		if bullet.rect.x > ai_settings.screen_width:
			bullets.remove(bullet)







