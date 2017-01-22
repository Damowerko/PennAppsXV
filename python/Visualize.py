import pygame
import numpy as np

class Visualize(object):
    def __init__(self):
        pygame.init()
        self.display_size = 1600
        self.screen = pygame.display.set_mode((self.display_size, self.display_size))

    def draw(self, theta):
        self.screen.fill((255,255,255))
        center = np.array([[self.display_size/2], [self.display_size/2]])

        vector = np.array([[self.display_size/4],[0]])

        theta = -theta

        rotMatrix = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        position = rotMatrix*vector

        pygame.draw.circle(self.screen, (100,100,255), center-position, 20, 0)
        pygame.display.update()




