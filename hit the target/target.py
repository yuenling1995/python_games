import pygame
from pygame.sprite import Sprite



class Target(Sprite):

	def __init__(self, ai_settings, screen):
		super().__init__()

		self.ai_settings = ai_settings
		self.screen = screen 

		self.rect = pygame.Rect(0, 0, ai_settings.target_width, ai_settings.target_height)
		self.screen_rect = screen.get_rect()

		#set up target's initial position.
		self.rect.right = self.screen_rect.right - 50
		self.rect.centery = self.screen_rect.centery

		# set up target's exact rect for later position updates.
		self.y = float(self.rect.y)

		self.color = ai_settings.target_color
		self.speed_factor = ai_settings.target_speed_factor 


	def draw_target(self):
		pygame.draw.rect(self.screen, self.color, self.rect)


	def update(self):
		self.y -= self.speed_factor * self.ai_settings.target_moving_direction
		if self.y <= self.screen_rect.top:
			self.ai_settings.target_moving_direction = -1
		# or elif self.rect.bottom > self.screen_rect.bottom:
		elif self.y >= int(self.screen_rect.bottom - 60):
			self.ai_settings.target_moving_direction = 1

		self.rect.y = self.y












