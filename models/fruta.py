from typing import Any
import pygame as pg
from datos import *
from .constantes import TILE_SIZE


class Item(pg.sprite.Sprite):
    def __init__(self,x,y,fruta_img):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(fruta_img, ((fruta_img.get_width()* 0.1), (fruta_img.get_height()* 0.1)))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 20, y + (TILE_SIZE - self.image.get_height()))
    def update(self,jugador):
        if pg.sprite.collide_rect(self, jugador):
            jugador.puntos += 100
            fruta_fx.play()
            self.kill()
            