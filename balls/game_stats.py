import pygame


class GameStats():
	""" track statistics for Catch the Ball."""

	def __init__(self, ai_settings):
		""" initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0


	def reset_stats(self):
		""" initialzie statistics that can change during the game"""
		self.character_left = self.ai_settings.character_limit
		self.score = 0
		self.level = 1