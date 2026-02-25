#Ajustes de las entidades del juego
class Ajustes:
    def __init__(self):
        #configuracion de la pantalla y su imagen de fondo
        self.anchura = 1300  
        self.altura = 507 
        self.fondo = 'imagenes/Mapa1.png'
        
        #Enemigos
        self.velocidadEnemigo = 1.75
        self.probabilidadEnviarEnemigo = 2

        #Plasticos
        self.velocidadPlasticos = 1.5
        self.probabilidadEnviarPlastico = 2

        #Puntuacion
        self.plasticosQuePuedenHuir = 10
        self.vidaJugador = 5


