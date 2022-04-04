import pygame
from pygame.sprite import Sprite




class Star(Sprite):

	def __init__(self, ai_settings, screen):
		super().__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("./images/star.bmp")
		self.image = pygame.transform.scale(self.image, (ai_settings.star_width, ai_settings.star_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# x,y position of star will be same as screen
		self.rect.x = self.screen_rect.x
		self.rect.y = self.screen_rect.y

		self.x = float(self.rect.x)


	def blitme(self):
		""" draw the star at its current position."""
		self.screen.blit(self.image, self.rect)
