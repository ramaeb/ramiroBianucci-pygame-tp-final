import pygame as pg
from pygame import mixer
from models.constantes import *
#cargar sonidos
pg.mixer.pre_init(44100,-16,2,512)
mixer.init()
pg.init()
fruta_fx = pg.mixer.Sound('assets/img/sounds/fruta_colect.wav')
fruta_fx.set_volume(0.3)
salto_fx = pg.mixer.Sound('assets/img/sounds/salto.wav')
salto_fx.set_volume(0.3)
cancion_fx = pg.mixer.Sound('assets/img/sounds/cancion.mp3')
cancion_fx.set_volume(0.1) 

#IMAGES
back_img = pg.image.load('./assets/img/background/3.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))
fruta_img = pg.image.load('assets/img/fruta/fruta.png')

#NIVEL 1
world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

