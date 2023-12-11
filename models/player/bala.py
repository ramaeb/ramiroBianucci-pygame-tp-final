import pygame as pg
from models.constantes import *
bullet_group = pg.sprite.Group()
class Bala(pg.sprite.Sprite):
    def __init__(self,x,y,direccion):
        # self.grupo = bullet_group
        pg.sprite.Sprite.__init__(self)
        self.velocidad = 15
        self.image =  pg.image.load('assets/img/bullet/5.png').convert_alpha()
        self.image = pg.transform.scale(self.image, ((self.image.get_width()*0.17), (self.image.get_height() * 0.2)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direccion = direccion
    def update(self):
        #movimiento bala
        self.rect.x = self.rect.x + (self.velocidad*self.direccion)
        #elimina balas del escenario
        if (self.rect.right < 0)or (self.rect.left > ANCHO_VENTANA):
            self.kill()

