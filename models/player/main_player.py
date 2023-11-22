import pygame as pg
from models.constantes import ANCHO_VENTANA, DEBUG,ALTO_VENTANA

class Jugador(pg.sprite.Sprite):

    def __init__(self,x,y,escala,velocidad):
        #HEREDO FUNCIONALIDADES DE LA CLASE SPRITE
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load('assets/img/player/idle/0.png')
        self.image = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.velocidad = velocidad #Cuantos pixeles se mueve el personaje al presionar tecla movimiento.
        self.direccion = True #Verdadero para la derecha y falso flipeo para la izquierda
        self.flip = False
        for i in range(5):
            img = pg.image.load(f'assets/img/player/idle/{i}.png')
            img = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
            self.lista_animacion.append(img) 
        self.index = 0

    def animacion(self):
        COOLDOWN_ANIMACION = 100     

    def movimiento_lateral(self,mueve_dere,mueve_izq):    
        #Coordenadas predecibles para el movimiento.
        dx = 0
        dy = 0

        if mueve_dere: 
            dx = self.velocidad
            self.direccion = True
            self.flip = False
            
        if mueve_izq:
            dx = -self.velocidad
            self.direccion = False
            self.flip = True
        #Seteo de la posicion del jugador
        self.rect.x += dx
        self.rect.y += dy


    def draw(self,screen):
        #Dibuja el personaje en pantalla, tambien dibuja si esta el flipeo de la imagen.
        screen.blit(pg.transform.flip(self.image,self.flip,False),self.rect) 