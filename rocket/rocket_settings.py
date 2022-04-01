class Settings():
	"""A class to store all settings for Rockets."""

	def __init__(self):
		""" Initialize the game's settings."""
		# Screen settings.
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (250, 250, 250)
		self.caption = "Rocket"

		# ship settings
		self.rocket_speed_factor = 1.5