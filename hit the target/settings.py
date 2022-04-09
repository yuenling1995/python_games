import pygame

class Settings():

	def __init__(self):

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255,255,255)
		self.caption = "Hit that Target"

		# target settings.
		self.target_width = 100
		self.target_height = 60
		self.target_color = (0, 255, 0)
		self.target_speed_factor = 2
		self.target_moving_direction = 1

		# person settings.
		self.person_width = 150
		self.person_height = 120
		self.person_moving_factor = 2.5
		self.person_limit = 3

		#bullets settings
		self.bullets_width = 17
		self.bullets_height = 3
		self.bullets_color = (60, 60, 60)
		self.bullets_speed_factor = 2
		self.bullets_allowed = 5

		#button settings.
		self.button_width = 200
		self.button_height = 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)