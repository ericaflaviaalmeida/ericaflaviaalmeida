import pygame


class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(
			image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		# obtém a posição do mouse
		pos = pygame.mouse.get_pos()
		# verifique as condições de mouseover e cliqu
		if self.rect.collidepoint(pos): #0 = left click
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		# botão de desenho na tela
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action