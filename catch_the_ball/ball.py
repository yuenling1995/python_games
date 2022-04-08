import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load("./images/ball.bmp")
		self.image = pygame.transform.scale(self.image, (self.ai_settings.ball_width, self.ai_settings.ball_height))
		self.rect = self.image.get_rect()
		self.screen_rect = self.image.get_rect()

		# set the ball initial position.
		self.rect.x = self.rect.width 
		self.rect.y = self.rect.height 

		self.y = float(self.rect.y) 


	def blitme(self):
		self.screen.blit(self.image, self.rect)


	def update(self):
		self.y += self.ai_settings.ball_drop_speed

		if self.y > self.ai_settings.screen_height: 
			self.y = 0
			
		self.rect.y = self.y



