import pygame
import sys
from pygame.locals import *

def main():
	color=(0, 35, 102)
	pygame.init()
	
	screen = pygame.display.set_mode((800,600), pygame.RESIZABLE )
	
	bg=pygame.Surface(screen.get_size())
	bg.fill(color)

	text_surface=font.render("KNACK!!!!!!!",True , (0,0,255))

	screen.blit(bg,(0,0))
	screen.blit(text_suface, (100,100))
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			pygame.display.update()
