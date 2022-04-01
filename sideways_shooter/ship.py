import pygame


class Ship():


	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("./images/ship.bmp")
		self.image = pygame.transform.scale(self.image, (ai_settings.ship_width, ai_settings.ship_height))

		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()


		#place the ship at on the left side of screen
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left

		# flag for continuous movements.
		self.moving_up = False
		self.moving_down = False


	def blitme(self):
		""" draw the ship onto the screen."""
		self.screen.blit(self.image, self.rect)


	def update(self):
		""" Update the ship's position."""
		if self.moving_up and self.rect.y > 0:
			self.rect.y -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.ai_settings.ship_speed_factor









