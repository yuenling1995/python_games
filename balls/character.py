import pygame
from pygame.sprite import Sprite


class Character(Sprite):

	def __init__(self, ai_settings, screen):

		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("./images/character.bmp")
		self.image = pygame.transform.scale(self.image, (self.ai_settings.character_width, self.ai_settings.character_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# set the character initial position.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#create flags to move right/left
		self.moving_right = False
		self.moving_left = False

		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.image, self.rect)


	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right: 
			self.x += self.ai_settings.character_speed_factor
		if self.moving_left and self.rect.x > 0:
			self.x -= self.ai_settings.character_speed_factor
		self.rect.x = self.x

	def center_character(self):
		self.rect.centerx = self.screen_rect.centerx 






