import pygame

class Goblin:
	def __init__(self):
		self.name = "Goblin"
		self.health = 30
		self.max_health = 30
		self.exp = 10
		self.dead = False
		self.image = pygame.image.load("goblin.png")