import pygame
from controls import events
import time

class Snake():
    def __init__(self, screen, length, list, image):
        self.screen = screen
        self.length = length
        self.list = list
        self.image = image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.y = self.rect.centery
        self.x = self.rect.centerx
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
            time.sleep(0.002)
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
            time.sleep(0.002)
        if self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
            time.sleep(0.002)
        if self.mup and self.rect.top > 0:
            self.rect.centery -= 1
            time.sleep(0.002)





