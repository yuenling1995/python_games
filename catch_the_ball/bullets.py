import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

	def __init__(self, ai_settings, screen, character):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("./images/bullets.bmp")
		self.image = pygame.transform.scale(self.image, (self.ai_settings.bullet_width, self.ai_settings.bullet_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# set the bullet initial position
		self.rect.centerx = character.rect.centerx
		self.rect.top = character.rect.top

		self.y = float(self.rect.y)


	def blitme(self):
		self.screen.blit(self.image, self.rect)


	def update(self):
		self.y -= self.ai_settings.bullet_speed_factor
		self.rect.y = self.y
