import pygame as pg
import random
from ..constantes import *
from ..player.bala import *
import os
class Enemigo(pg.sprite.Sprite):

    def __init__(self,x,y,escala,velocidad,mundo,jugador,puntos=0,vidas=3):
        #HEREDO FUNCIONALIDADES DE LA CLASE SPRITE
        pg.sprite.Sprite.__init__(self)
        self.jugador = jugador
        self.mundo = mundo
        self.vidas = vidas
        self.disparando = False
        self.enemigo_vivo = True #VARIABLE PARA SABER SI EL JUGADOR ESTÁ VIVO.
        self.velocidad = velocidad #Cuantos pixeles se mueve el personaje al presionar tecla movimiento.
        self.direccion = 1 #Verdadero para la derecha y falso flipeo para la izquierda
        self.lista_animacion = []
        self.vel_y = 0
        self.flip = False #Variable para girar el sprite izq y der
        self.tiempo_animacion = pg.time.get_ticks()
        self.accion = 0
        self.colisiona = False #Flag para la colision
        self.cayendo = True #Flag para la caida del jugador
        self.index_animacion = 0
        self.salta = False #Activa el salto
        self.cooldown_disparo = 20
        self.mueve_dere = False
        self.mueve_izq = False
        self.contador_movimiento = 0
        self.idling = False
        self.idling_counter = 0
        self.ai_moving_right = False
        self.ai_moving_left = False
        self.vision = pg.Rect(0, 0, 100, 20)
        #IDLE
        #CARGA LAS ANIMACIONES
        tipo_animacion = ['idle','walk','death']
        for animacion in tipo_animacion:
            #LISTA TEMPORAL
            lista_temporal = []
            #AGREGA CADA IMAGEN A LA LISTA E ITERA
            num_frames = len(os.listdir(f'assets/img/enemy/{animacion}'))
            for i in range(num_frames):
                img = pg.image.load(f'assets/img/enemy/{animacion}/{i}.png')
                img = pg.transform.scale(img, ((img.get_width()* escala), (img.get_height()* escala)))
                lista_temporal.append(img)
            self.lista_animacion.append(lista_temporal)

        self.image = self.lista_animacion[self.accion][self.index_animacion]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def animacion(self):
        COOLDOWN_ANIMACION = 100
        #cambio de imagen, segun el frame elegido
        self.image = self.lista_animacion[self.accion][self.index_animacion]
        #empiezo el timer para seguir cambiando los sprites de la animacion
        if pg.time.get_ticks() - self.tiempo_animacion > COOLDOWN_ANIMACION:
            self.tiempo_animacion = pg.time.get_ticks()
            self.index_animacion += 1
        if self.index_animacion >= len(self.lista_animacion[self.accion]):
            if self.accion == 2:
                self.index_animacion = len(self.lista_animacion[self.accion])-1
            else:
                self.index_animacion = 0
    def cambio_accion(self,accion):
        if accion != self.accion:
            self.accion = accion
            self.index_animacion = 0
            self.tiempo_animacion = pg.time.get_ticks()

    def movimiento(self,mueve_dere,mueve_izq):    
        #Coordenadas predecibles para el movimiento, 
        # sirven para parar movimientos o para las mismas colisiones.
        dx = 0
        dy = 0
        if mueve_dere: 
            dx = self.velocidad
            self.direccion = 1
            self.flip = False
        if mueve_izq:
            dx = -self.velocidad
            self.direccion = -1
            self.flip = True
        
        for tile in self.mundo.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                self.direccion *= -1
                self.contador_movimiento = 0
			#CHEQUEA COLISION TILE X Y FLIP SI CHOCA CON TILE
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#CHEQUEA Y SALTANDO //INDIFERENTE EN ENEMIGO
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
				#CHEQUEA SI COLISIONA EN Y //PISO
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.cayendo =  False
                    dy = tile[1].top - self.rect.bottom
                
        
        self.rect.x += dx
        self.rect.y += dy
    def cambio_sprites_movimiento(self,mueve_dere,mueve_izq,enemigo,enemigo_vivo):
        if enemigo_vivo:
            if (mueve_dere or mueve_izq):
                enemigo.cambio_accion(1)
            else:
                enemigo.cambio_accion(0)
        else:
            enemigo.cambio_accion(2)

    def draw(self,screen):
        #Dibuja el personaje en pantalla, tambien dibuja si esta el flipeo de la imagen.
        screen.blit(pg.transform.flip(self.image,self.flip,False),self.rect) 
    def disparo(self):
            if self.cooldown_disparo == 0:
                self.cooldown_disparo = 20
                bala = Bala(self.rect.centerx + (0.8 * self.rect.size[0] * self.direccion) , self.rect.centery, self.direccion)
                bullet_group.add(bala)

    def ia(self):
        if self.enemigo_vivo:
            if self.idling == False and random.randint(1, 200) == 1:
                    self.cambio_accion(0)
                    self.idling = True
                    self.idling_counter = 50
                #SE FIJA SI ESTA CERCA DEL JUGADOR
            if self.vision.colliderect(self.jugador.rect):
				#ATACA
                self.velocidad = 15
                self.disparo()
            else:
                    print(self.idling_counter)
                    if self.idling == False:
                        if self.direccion == 1:
                            self.ai_moving_right = True
                        else:
                            self.ai_moving_right = False
                        
                        ai_moving_left = not self.ai_moving_right
                        self.movimiento(self.ai_moving_right,ai_moving_left)
                        self.cambio_accion(1)#1: run
                        self.contador_movimiento += 1
                        #CENTRA LA VISION DEL ENEMIGO CUANDO SE MUEVE
                        self.vision.center = (self.rect.centerx + 150 * self.direccion, self.rect.centery)

                        if self.contador_movimiento > 10:
                            self.direccion *= -1
                            self.contador_movimiento *= -1
                    else:
                        self.idling_counter -= 1
                        if self.idling_counter <= 0:
                            self.idling = False
        else:
            self.mueve_dere = False
            self.mueve_izq = False
            self.movimiento(self.ai_moving_right,self.ai_moving_left)
            self.animacion()
            self.cambio_sprites_movimiento(self.ai_moving_right,self.ai_moving_left,self,self.enemigo_vivo)
            self.rect.y += 60
            

    def update(self):
        self.ia()
        self.animacion()
        self.cambio_sprites_movimiento(self.ai_moving_right,self.ai_moving_left,self,self.enemigo_vivo)
        if self.disparando:
            print("disparando")
            self.disparo()
        if self.vidas == 0:
            self.enemigo_vivo = False
        if self.cooldown_disparo > 0:
            self.cooldown_disparo -= 1