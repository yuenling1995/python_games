import pygame


class Settings():

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)
		self.caption = "Catch the Ball"

		#character settings.
		self.character_width = 180
		self.character_height = 180
		self.character_speed_factor = 2
		self.character_limit = 3


		#bullet settings.
		self.bullet_width = 40
		self.bullet_height = 40
		self.bullet_speed_factor = 1.5
		self.bullets_allowed = 5

		#ball settings
		self.ball_width = 50
		self.ball_height = 50
		self.ball_drop_speed = 1.5









