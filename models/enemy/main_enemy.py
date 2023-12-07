import pygame as pg
from ..constantes import *
from models.constantes import ANCHO_VENTANA, DEBUG,ALTO_VENTANA

class Enemigo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((100, 100))  # Tamaño del enemigo
        self.image.fill((0,0,0))  # Color del enemigo
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)  # Posición inicial del enemigo