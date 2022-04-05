import pygame



class Settings():

	def __init__(self):

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (250, 250, 250)
		self.caption = "Raindrop Grid"

		# raindrop settings.
		self.raindrop_width = 80
		self.raindrop_height = 80
		self.raindrop_speed_factor = 1
		self.raindrop_drop_speed = 1