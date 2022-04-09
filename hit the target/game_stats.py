import pygame


class GameStats():
	""" track statistics for Hit that Target."""

	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False


	def reset_stats(self):
		self.person_left = self.ai_settings.person_limit