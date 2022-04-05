import pygame


class Settings():

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.caption = "Catch the Ball"
		self.bg_color = (255, 255, 255)


		# character settings
		self.character_width = 180
		self.character_height = 180
		self.character_speed_factor = 3

		#ball settings
		self.ball_width = 80
		self.ball_height = 80
		self.ball_drop_speed = 1