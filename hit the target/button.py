import pygame.font 


class Button():

	def __init__(self, ai_settings, screen, msg):
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = screen.get_rect()

		self.font = pygame.font.SysFont(None, 48)

		# build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.ai_settings.button_width, self.ai_settings.button_height)
		self.rect.center = self.screen_rect.center

		# the button message needs to be prepped only once
		self.prep_msg(msg)


	def prep_msg(self, msg):
		# render the text display as an image
		self.msg_image = self.font.render(msg, True, self.ai_settings.text_color, self.ai_settings.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		self.screen.fill(self.ai_settings.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


# some Notes here:
# steps to display text on the screen - 
# 1 - create a font object: pygame.font.SysFont()
# 2 - render the text display as an image 
# 3 - blit the text image

# here we wanna create a button with text (msg) in it, so we also create a rect object fill with green color.
# we draw the green rectangle first, and then blit the text image at the same position as the green rectangle.





