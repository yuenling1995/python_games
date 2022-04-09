import pygame
from pygame.sprite import Sprite



class Bullets(Sprite):

	def __init__(self, ai_settings, screen, person):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings


		# create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, self.ai_settings.bullets_width, self.ai_settings.bullets_height)
		self.rect.centery = person.rect.centery
		self.rect.left = person.rect.right 

		# store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

		self.color = self.ai_settings.bullets_color
		self.speed_factor = self.ai_settings.bullets_speed_factor


	def draw_bullets(self):
		pygame.draw.rect(self.screen, self.color, self.rect)


	def update(self):
		self.x += self.speed_factor
		self.rect.x = self.x
