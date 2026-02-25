#Archivo para la entidad de los enemigos
import pygame
from pygame.sprite import Sprite
import random

class Enemigo(Sprite):
    def __init__(self,bt_game):
        #carga al enemigo, establece su imagen y su posicion de inicio
        super().__init__()
        self.bt_game = bt_game
        self.screen = bt_game.screen

        self.image = pygame.image.load('imagenes/Enemigo1.bmp')
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height-150
        self.rect.x = random.randint(10, self.rect.width)*10
        self.ajustes = bt_game.ajustes

    #actualiza la posicion del enemigo decendiendo segun la velocidad en los ajustes
    def update(self):
        self.rect.y += self.ajustes.velocidadEnemigo
