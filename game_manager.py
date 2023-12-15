import pygame as pg
from nivel import *
from datos import *
from models.auxiliar import *
from models.player.bala import *
from models.enemy.main_enemy import *
from models.fruta import *
from creador_mundo import *
from models.enemy.main_enemy import Enemigo
from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

class Game():
    def __init__(self):
        self.jugador = Jugador(300,200,3,5)
        self.enemigo = Enemigo()
        self.item = Item()
        self.juego_ejecutandose = True
    def juego_corriendo(self):
        while self.juego_ejecutandose:
            print(self.jugador.puntos)

class Tiempo():
    def __init__(self,tiempo,puntos):
        self.tiempo = tiempo
        self.puntos = puntos
    def update_tiempo(tiempo):
        fuente = pg.font.SysFont("Arial",30)
        contador = fuente.render(f"TIEMPO: {tiempo}",False,(0,0,0))
        return contador
    def update_puntos(puntos):
        fuente = pg.font.SysFont("Arial",30)
        puntos = fuente.render(f"PUNTOS: {puntos}",False,(0,0,0))
        return puntos

