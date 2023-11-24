import pygame as pg
from models.constantes import ANCHO_VENTANA, DEBUG,ALTO_VENTANA

GRAVEDAD = 0.8
class Jugador(pg.sprite.Sprite):

    def __init__(self,x,y,escala,velocidad):
        #HEREDO FUNCIONALIDADES DE LA CLASE SPRITE
        pg.sprite.Sprite.__init__(self)
        self.jugador_vivo = True #VARIABLE PARA SABER SI EL JUGADOR ESTÁ VIVO.
        self.velocidad = velocidad #Cuantos pixeles se mueve el personaje al presionar tecla movimiento.
        self.direccion = True #Verdadero para la derecha y falso flipeo para la izquierda
        self.lista_animacion = []
        self.flip = False #Variable para girar el sprite izq y der
        self.tiempo_animacion = pg.time.get_ticks()
        self.accion = 0
        self.index_animacion = 0
        self.salta = False #Variable para saber si está saltando o no.
        #IDLE
        lista_temporal = []
        for i in range(5):
            img = pg.image.load(f'assets/img/player/idle/{i}.png')
            img = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
            lista_temporal.append(img)
        self.lista_animacion.append(lista_temporal)
        
        lista_temporal = []
        for i in range(7):
            img = pg.image.load(f'assets/img/player/walk/{i}.png')
            img = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
            lista_temporal.append(img)
        self.lista_animacion.append(lista_temporal)

        lista_temporal = []
        for i in range(7):
            img = pg.image.load(f'assets/img/player/shoot/{i}.png')
            img = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
            lista_temporal.append(img)

        self.lista_animacion.append(lista_temporal)

        lista_temporal = []
        for i in range(3):
            img = pg.image.load(f'assets/img/player/jump/{i}.png')
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

        if self.salta:
            pass


    def disparo(self,dispara):
        if dispara:
            pass

    def draw(self,screen):
        #Dibuja el personaje en pantalla, tambien dibuja si esta el flipeo de la imagen.
        screen.blit(pg.transform.flip(self.image,self.flip,False),self.rect) 