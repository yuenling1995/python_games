import sys
import pygame


class Settings():

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (250, 250, 250)
		self.caption = "Sideways Shooter"

		#ship settings.
		self.ship_speed_factor = 2
		self.ship_width = 220
		self.ship_height = 150

		# bullet settings.
		self.bullet_width = 80
		self.bullet_height = 60
		self.bullet_color = 60, 60, 60
		self.bullet_speed_factor = 1
		self.bullets_allowed = 3