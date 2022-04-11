import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep



def check_keydown_events(event, ai_settings, screen, stats, ship, bullets, aliens):
	""" Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		after_button_click(ai_settings, screen, stats, ship, bullets, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
	""" Fire a bullet if limit not reached yet."""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):
	""" Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
	""" Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, stats, ship, bullets, aliens)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	""" start a new game when the play clicks play."""
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		after_button_click(ai_settings, screen, stats, ship, bullets, aliens, sb)


def after_button_click(ai_settings, screen, stats, ship, bullets, aliens, sb):
	# hide the mouse cursor
	pygame.mouse.set_visible(False)

	# reset the game settings.
	ai_settings.initialize_dynamic_settings()
	stats.reset_stats()
	stats.game_active = True

	# reset the scoreboard images.
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()

	# empty the list of aliens and bullets.
	aliens.empty()
	bullets.empty()

	# create a new fleet of aliens and center the ship.
	create_fleet(ai_settings, screen, ship, aliens)
	ship.center_ship()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	""" update position of bullets and get rid of old bullets."""
	bullets.update()
	remove_old_bullets(bullets)

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def remove_old_bullets(bullets):
	""" Update position of bullets and get rid of old bullets."""

	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	""" respond to bullet-alien collisions."""
	# remove any bullets and aliens that have collided.

	# check for any bullets that have hit aliens.
	# if so, get rid of the bullet and the alien.
	# the first False creates a super bullet, bullet still exists after it hits the alien
	collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

	if collisions:
		# collisions is a dictionary
		# aliens is a list of aliens being hit by bullet
		# this makes sure each hit alien is counted
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(aliens) == 0:
		# if the entire fleet is destroyed, start a new level.
		# destroy existing bullets and create a new fleet.
		bullets.empty()

		# increase the moving speed
		ai_settings.increase_speed()

		# increase level
		stats.level += 1
		sb.prep_level()

		create_fleet(ai_settings, screen, ship, aliens)


def check_high_score(stats, sb):
	""" check to see if there's a new high score."""
	if stats.score > stats.high_score:
		stats.high_score = stats.score 
		sb.prep_high_score()



def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	""" Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.

	screen.fill(ai_settings.bg_color)

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)

	# draw the score & ships information.
	sb.show_score()

	# draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()


	# Make the most recently drawn screen visible.
	pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
	""" determine the number of aliens that fit in a row."""
	available_space_x = ai_settings.screen_width - 3 * alien_width 
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
	""" determine the number of rows of aliens that fit on the screen."""
	available_space_y = ai_settings.screen_height - ship_height -  2 * alien_height
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	""" create an alien and place it in the row."""
	alien = Alien(ai_settings, screen)
	alien.x = alien.rect.width + 2 * alien.rect.width * alien_number 
	alien.rect.x = alien.x 

	alien.y = 2 * alien.rect.height + 2 * alien.rect.height * row_number
	alien.rect.y = alien.y
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
	""" create a full fleet of aliens."""
	# create an alien and find the number of aliens in a row.
	# spacing between each alien is equal to one alien width.
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	# create the fleet of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			# create an alien and place it in the row.
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
	""" respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)


def change_fleet_direction(ai_settings, aliens):
	""" drop the alien and change direction when it hits the edge of screen."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
	"""
	check if the fleet is at an edge,
	and then update the positions of all aliens in the fleet.
	"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# look for alien-ship collisions.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

	# look for aliens hitting the bottom of the screen.
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
	""" respond to ship being hit by alien."""
	if stats.ship_left > 0:
		# decrement ship_left
		stats.ship_left -= 1

		# update ships scoreboard
		sb.prep_ships()

		# empty the lsit of aliens and bullets.
		aliens.empty()
		bullets.empty()

		# create a new fleet and center the ship.
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		# pause 
		sleep(0.5)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)



def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
	""" check if any aliens have reached the bottom of the screen."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# treat this the same as if the ship got hit.
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)










