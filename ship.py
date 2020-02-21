import pygame

class Ship():
    def __init__(self, screen):
        """initialize ship and set its starting position"""
        self.screen = screen
        
        #load image and save it as self.image
        self.image = pygame.image.load('images/ship.bmp')
        #set image as a rectangle
        self.rect = self.image.get_rect()
        #set screen as a rectangle, then you can position the image in the rectangle
        self.screen_rect = screen.get_rect()
        
        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen.centerx
        self.rect.bottom = self.screen.bottom
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        


        
        