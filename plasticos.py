#Archivo para la entidad de los recolectables
import pygame
from pygame.sprite import Sprite
import random

class Bolsa(Sprite):
    #Carga los recolectables tipo bolsa, su imagen y los posiciona aleatoriamente en la parte superior
    def __init__(self,bt_game):
        super().__init__()
        self.bt_game = bt_game
        self.screen = bt_game.screen

        self.image = pygame.image.load('imagenes/Bolsa.bmp')
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height-150
        self.rect.x = random.randint(10, self.rect.width)*10
        self.ajustes = bt_game.ajustes

    #actualiza la bolsa moviendola hacia abajo
    def update(self):
        self.rect.y += self.ajustes.velocidadPlasticos

class Botella(Sprite):
    #Carga los recolectables tipo botella, su imagen y los posiciona aleatoriamente en la parte superior
    def __init__(self,bt_game):
        super().__init__()
        self.bt_game = bt_game
        self.screen = bt_game.screen

        self.image = pygame.image.load('imagenes/Botella.bmp')
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height-150
        self.rect.x = random.randint(10, self.rect.width)*10
        self.ajustes = bt_game.ajustes

    #actualiza la botella moviendola hacia abajo
    def update(self):
        self.rect.y += self.ajustes.velocidadPlasticos
