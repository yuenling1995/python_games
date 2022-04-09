import pygame
from pygame.sprite import Sprite



class Person(Sprite):

	def __init__(self, ai_settings, screen):

		self.ai_settings = ai_settings
		self.screen = screen 

		self.image = pygame.image.load("./images/person.bmp")
		self.image = pygame.transform.scale(self.image, (self.ai_settings.person_width, self.ai_settings.person_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# set the person initial position.
		self.rect.centery = self.screen_rect.centery 
		self.rect.left = self.screen_rect.left + 20

		# set the person's exact rect for later position updates
		self.y = float(self.rect.y)


		# set the flag for moving.
		self.moving_up = False
		self.moving_down = False
		self.speed_factor = self.ai_settings.person_moving_factor


	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_up and self.y > 0:
			self.y -= self.speed_factor
		if self.moving_down and self.y <= int(self.screen_rect.bottom - 120):
			self.y += self.speed_factor

		self.rect.y = self.y






