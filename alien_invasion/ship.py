import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		"""Initialzie the ship and set its starting position."""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("./images/ship.bmp")
		self.image = pygame.transform.scale(self.image, (ai_settings.ship_width, ai_settings.ship_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_right = False
		self.moving_left = False

		self.center = float(self.rect.centerx)


	def update(self):
		""" Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def blitme(self):
		""" Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)


	def center_ship(self):
		""" center the ship on the screen."""
		self.rect.centerx = self.screen_rect.centerx







