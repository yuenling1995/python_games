import pygame


class Settings():
	""" initialize the game's static settings."""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		self.caption = "Catch the Ball"

		#character settings.
		self.character_width = 120
		self.character_height = 120
		self.character_limit = 3


		#bullet settings.
		self.bullet_width = 40
		self.bullet_height = 40
		self.bullets_allowed = 20

		#ball settings
		self.ball_width = 65
		self.ball_height = 65

		# how quickly the game speeds up
		self.speedup_scale = 1.1
		# how quickly the score adds up
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.character_speed_factor = 4
		self.bullet_speed_factor = 1.5
		self.ball_drop_speed = 1
		self.ball_points = 50


	def increase_speed(self):
		self.character_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.ball_drop_speed *= self.speedup_scale

		self.ball_points = int(self.ball_points * self.score_scale)
























