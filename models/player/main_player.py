import pygame as pg
import os
from ..constantes import *
from models.constantes import ANCHO_VENTANA, DEBUG,ALTO_VENTANA

class Jugador(pg.sprite.Sprite):

    def __init__(self,x,y,escala,velocidad):
        #HEREDO FUNCIONALIDADES DE LA CLASE SPRITE
        pg.sprite.Sprite.__init__(self)
        self.jugador_vivo = True #VARIABLE PARA SABER SI EL JUGADOR ESTÁ VIVO.
        self.velocidad = velocidad #Cuantos pixeles se mueve el personaje al presionar tecla movimiento.
        self.direccion = True #Verdadero para la derecha y falso flipeo para la izquierda
        self.lista_animacion = []
        self.vel_y = 0
        self.flip = False #Variable para girar el sprite izq y der
        self.tiempo_animacion = pg.time.get_ticks()
        self.accion = 0
        self.colisiona = False #Flag para la colision
        self.cayendo = False #Flag para la caida del jugador
        self.index_animacion = 0
        self.salta = False #Activa el salto
        #IDLE
        #CARGA LAS ANIMACIONES
        tipo_animacion = ['idle','walk','jump','shoot','death']
        for animacion in tipo_animacion:
            #LISTA TEMPORAL
            lista_temporal = []
            #AGREGA CADA IMAGEN A LA LISTA E ITERA
            num_frames = len(os.listdir(f'assets/img/player/{animacion}'))
            for i in range(num_frames):
                img = pg.image.load(f'assets/img/player/{animacion}/{i}.png')
                img = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
                lista_temporal.append(img)
            self.lista_animacion.append(lista_temporal)

        self.image = self.lista_animacion[self.accion][self.index_animacion]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        

    def animacion(self):
        COOLDOWN_ANIMACION = 100
        #cambio de imagen, segun el frame elegido
        self.image = self.lista_animacion[self.accion][self.index_animacion]
        #empiezo el timer para seguir cambiando los sprites de la animacion
        
        if pg.time.get_ticks() - self.tiempo_animacion > COOLDOWN_ANIMACION:
            self.tiempo_animacion = pg.time.get_ticks()
            self.index_animacion += 1
        if self.index_animacion >= len(self.lista_animacion[self.accion]):
            self.index_animacion = 0
        
    def cambio_accion(self,accion):
        if accion != self.accion:
            self.accion = accion
            self.index_animacion = 0
            self.tiempo_animacion = pg.time.get_ticks()


    def movimiento_lateral(self,mueve_dere,mueve_izq):    
        #Coordenadas predecibles para el movimiento, 
        # sirven para parar movimientos o para las mismas colisiones.
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
        if self.cayendo == True:
            if self.salta:
                self.vel_y = -11
                self.salta = False
            else:
                self.vel_y += GRAVEDAD
                dy += self.vel_y
        
        #COLISION PISO INVENTADO
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.colisiona = True
            self.cayendo = False
        if self.rect.left <= 0:
            self.rect.left = 0
            print("MURO IZ")
        if self.rect.right + dx > ANCHO_VENTANA:
            dx = ANCHO_VENTANA - self.rect.right
            print("MURO")
        
        self.rect.x += dx
        self.rect.y += dy

        


    def disparo(self,dispara):
        if dispara:
            pass

    def draw(self,screen):
        #Dibuja el personaje en pantalla, tambien dibuja si esta el flipeo de la imagen.
        screen.blit(pg.transform.flip(self.image,self.flip,False),self.rect) 

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y,velocidad):  
        pg.sprite.Sprite.__init__(self)