import pygame
import sys
from ajustes import Ajustes
from barco import Barco
from enemigo import Enemigo
from plasticos import Botella
from plasticos import Bolsa
import random

class Bote:
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.anchura, self.ajustes.altura))
        self.fondo = pygame.image.load(self.ajustes.fondo)
        pygame.display.set_caption("Boat game")
        self.barco = Barco(self)
        self.enemigos = pygame.sprite.Group()
        self.plasticos = pygame.sprite.Group()
        self.puntuacionJugador = 0
        self.salud = self.ajustes.vidaJugador
        self.plasticoHuir = self.ajustes.plasticosQuePuedenHuir
        self.gameover = False


    def enviarEnemigos(self):
        if len(self.enemigos)<0:
            pez = Enemigo(self)
            self.enemigos.add(pez)
        elif len(self.enemigos)<5 and random.randint(1,100) <= self.ajustes.probabilidadEnviarEnemigo:
            pez = Enemigo(self)
            self.enemigos.add(pez)
            
    def enviarPlasticos(self):
        if len(self.plasticos)<0:
            bottle = Botella(self)
            bag = Bolsa(self)
            self.plasticos.add(bottle)
            self.plasticos.add(bag)
        elif len(self.plasticos)<3 and random.randint(1,100) <= self.ajustes.probabilidadEnviarPlastico:
            bottle = Botella(self)
            bag = Bolsa(self)
            self.plasticos.add(bottle)
            self.plasticoHuir -= 1
            self.plasticos.add(bag)            

    def elimiarEnemigos(self):
        for enemigo in self.enemigos.copy():
            if enemigo.rect.bottom >= self.ajustes.altura:
                self.enemigos.remove(enemigo)
                self.enviarEnemigos()
                self.muerto()

    def elimiarPlasticos(self):
        for plastico in self.plasticos.copy():
            if plastico.rect.bottom >= self.ajustes.altura:
                self.plasticos.remove(plastico)
                self.enviarPlasticos()
        
    def colisionJugador(self):
        colisionPez = pygame.sprite.spritecollide(self.barco, self.enemigos,True)
        colisionBotella = pygame.sprite.spritecollide(self.barco, self.plasticos,True)
        if len(colisionBotella) != 0:
            self.puntuacionJugador += 10
            self.plasticoHuir += 1
        if len(colisionPez) != 0:
            self.salud -= 1
            self.muerto()

    def muerto(self):
        if self.salud<=0 or self.plasticoHuir<=0:
            self.gameover = True
            
            #sys.exit()


    def actualizarEnemigos(self):
        self.enemigos.update()

    def actualizarPlasticos(self):
        self.plasticos.update()

    def actualizarPantalla(self):
        self.screen.blit(self.fondo,(0,0))
        self.barco.blime()
        self.enemigos.draw(self.screen)
        self.plasticos.draw(self.screen)
        self.puntiacion()
        self.txtPlasticoHuido()
        self.txtSalud()
        self.Gmover()
        pygame.display.flip()
    
    def bordes(self):
        izquierda = 100
        derecha = 700
        arriba = 100
        abajo = 500
        rectangulo = pygame.Rect(izquierda, arriba,6)
         


    def compronbarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif self.gameover == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.barco.moviendoDerecha = True
                        self.barco.rect.x +=2
                    elif event.key == pygame.K_LEFT:
                        self.barco.moviendoIzquierda = True
                        self.barco.rect.x -=2

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.barco.moviendoDerecha = False
                    elif event.key == pygame.K_LEFT:
                        self.barco.moviendoIzquierda = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.gameover:
                        self.__init__()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit()
                
    def Gmover(self):
        if self.gameover == True:
            fuente = pygame.font.SysFont("Consolas", 25)
            superficieTXT = fuente.render(f""" Perdiste :c Presiona "espacio" para continuar o presiona click para salir """, True, (255,255,255),(255,0,0))
            rectTXT = superficieTXT.get_rect()
            rectTXT.midtop = (600,200)
            self.screen.blit(superficieTXT, rectTXT)
    def puntiacion(self):
        fuente = pygame.font.SysFont("Consolas", 50)
        superficieTXT = fuente.render(str(self.puntuacionJugador),True, (255,255,255))
        rectTXT = superficieTXT.get_rect()
        rectTXT.midtop = (620,20)
        self.screen.blit(superficieTXT, rectTXT)
    def txtSalud(self):
        fuente = pygame.font.SysFont("Consolas", 25)
        superficieTXT = fuente.render(f"Vidas = {str(self.salud)}",True, (0,0,0),(255,0,0))
        rectTXT = superficieTXT.get_rect()
        rectTXT.midtop = (75,0)
        self.screen.blit(superficieTXT, rectTXT)
    def txtPlasticoHuido(self):
        fuente = pygame.font.SysFont("Consolas", 25)
        superficieTXT = fuente.render(f" No dejes que escapen! {str(self.plasticoHuir)}",True, (0,0,0),(255,0,0))
        rectTXT = superficieTXT.get_rect()
        rectTXT.midtop = (1100,0)
        self.screen.blit(superficieTXT, rectTXT)

    def run_game(self):
        while True:
            self.compronbarEventos()
            self.barco.actualizar()
            self.colisionJugador()
            self.enviarEnemigos()
            self.enviarPlasticos()
            self.actualizarEnemigos()
            self.actualizarPlasticos()
            self.elimiarEnemigos()
            self.elimiarPlasticos()

            

            self.actualizarPantalla()
 

if __name__ == '__main__':
    bt = Bote()
    bt.run_game()