import pygame
from pygame.sprite import Sprite




class Bullet(Sprite):
	""" A class to manage bullets fired from the ship."""

	def __init__(self, ai_settings, screen, ship):
		""" create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = screen

		#create a bullet rect at (0,0) and then set correct position.
		self.bullet = pygame.image.load("./images/monkey_bullet.bmp")
		self.bullet = pygame.transform.scale(self.bullet, (ai_settings.bullet_width, ai_settings.bullet_height))

		self.rect = self.bullet.get_rect()
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right

		# store bullet's y position as float
		self.x = float(self.rect.x)

		self.speed_factor = ai_settings.bullet_speed_factor


	def update(self):
		""" move the bullet up the screen."""
		# update the decimal position of the bullet.
		self.x += self.speed_factor
		# update the rect position.
		self.rect.x = self.x


	def draw_bullet(self):
		self.screen.blit(self.bullet, self.rect)
