import pygame
import sys
from pygame.locals import *

def main():
	aq = (127, 255, 212)
	pygame.init()

	#creating main screen surface
	screen_width  = 320
	screen_height = 480
	size_tuple = (screen_width, screen_height)
	screen = pygame.display.set_mode(size_tuple)


	#setting game name in title bar
	pygame.display.set_caption("mono2")


	#creating background surface
	background = pygame.Surface(size_tuple)
	background.fill(aq)

	font = pygame.font.Font("ubuntu.ttf", 28)
	text_surface = font.render("Monopoly2", True, (0,0,255))

	
	screen.blit(background, (0,0))
	screen.blit(text_surface, (100,100))
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
		pygame.display.update()


if __name__ == "__main__":
	main()
