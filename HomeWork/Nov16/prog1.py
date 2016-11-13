import pygame

class config_class(object):
    def __init__(self, config_dict):
        for attribute, value in config_dict.items():
            setattr(self, attribute, value)

class fighter(pygame.Surface):
    def __init__(self, config):
        self.config = config
        self.left, self.top, self.width, self.height = self.config.coordinates
        self.__create__()

    def __create__(self):
        self.__create_main__()
        self.__create_health__()

    def __create_main__(self):
        #main_surface
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.config.color)

    def __create_health__(self):
        #health
        self.health_surface   = pygame.font.Font(None,15).render(str(self.config.health), True, (0,0,0))
        self.health_x_y       = (self.width - self.health_surface.get_width())/2,10

    def __draw__(self):
        self.config.screen.blit(self.surface, (self.left, self.top))

        if self.config.bools["health_changed"]:
            self.config.health += self.config.data["health_delta"]
            if self.config.health <0:
                self.__destroy__()
            else:
                self.config.bools["health_changed"] = False
                self.__create_main__()
                self.__create_health__()
        self.surface.blit(self.health_surface, self.health_x_y)
    
    def __destroy__(self):
        print "i am done"

   
