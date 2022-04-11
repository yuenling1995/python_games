import pygame



class Settings():

	def __init__(self):
		""" Initialize the game's static settings."""
		# screen settings.
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		self.caption = "Alien Invasion"

		# ship settings.
		self.ship_width = 50
		self.ship_height = 40
		self.ship_limit = 3


		# Bullet settings.
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5

		# alien settings.
		self.alien_width = 70
		self.alien_height = 70
		self.fleet_drop_speed = 10

		# how quickly the game speeds up
		self.speedup_scale = 1.1
		# how quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()



	def initialize_dynamic_settings(self):
		""" Initialize settings that change throughout the game."""
		self.ship_speed_factor = 2
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction of 1 represent right; -1 represents left.
		self.fleet_direction = 1

		# scoring
		self.alien_points = 50


	def increase_speed(self):
		""" Increase speed settings and alien point values."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

























