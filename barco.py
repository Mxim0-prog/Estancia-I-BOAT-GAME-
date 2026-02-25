#Archivo para la entidad del barco 
import pygame
from resources import recurso_ruta

class Barco:
    def __init__(self, bt_game):
        self.screen = bt_game.screen
        self.screen_rect = bt_game.screen.get_rect()
        #carga la imagen del barco y lo posiciona al centro y en medio
        self.imagen = pygame.image.load(recurso_ruta('imagenes/Barco1.bmp'))
        self.rect = self.imagen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moviendoIzquierda = False
        self.moviendoDerecha = False


    #dibuja el barco en la posicion
    def blime(self):
        self.screen.blit(self.imagen, self.rect)
    #actualiza la posicion del barco
    def actualizar(self):
        if self.moviendoDerecha:
            self.rect.x += 10
        if self.moviendoIzquierda:
            self.rect.x -= 10

        