import pygame

class Rocket():

	def __init__(self, ai_settings, screen):
		""" Initialize the rocket and set its starting position."""
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the rocket image and get its rect.
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new rocket at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the rocket's center.
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		""" Update the rocket's position based on the movement flag."""
		# Update the rocket's center value, not the rect. - because rect can't take on decimals
		if self.moving_right and self.rect.right < self.screen_rect.right:
			#used to be: self.rect.center += 1
			self.center += self.ai_settings.rocket_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.rocket_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.bottom -= self.ai_settings.rocket_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.rocket_speed_factor

		# Update rect object from self.center
		self.rect.centerx = self.center
		self.rect.bottom = self.bottom

	def blitme(self):
		""" Draw the rocket at its current location."""
		self.screen.blit(self.image, self.rect)

