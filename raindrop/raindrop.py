import pygame
from pygame.sprite import Sprite



class Raindrop(Sprite):

	def __init__(self, ai_settings, screen):
		super().__init__()

		self.screen = screen
		self.ai_settings = ai_settings


		self.image = pygame.image.load("./images/raindrop.bmp")
		self.image = pygame.transform.scale(self.image, (self.ai_settings.raindrop_width, self.ai_settings.raindrop_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# set the raindrop's initial position.
		self.rect.x = self.rect.width 
		self.rect.y = self.rect.height
		
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.image, self.rect)


	def update(self):
		self.y += self.ai_settings.raindrop_speed_factor

		# redraw the row of raindrops when it hit the bottom of screen
		if self.y >= self.screen_rect.height:
			self.y = 0
		self.rect.y = self.y


	def check_edges(self):
		""" return true if the raindrop hits the bottom of screen."""
		if self.rect.bottom >= self.screen_rect.bottom:
			return True



