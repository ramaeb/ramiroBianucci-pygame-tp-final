import pygame as pg
from pygame import mixer
from models.constantes import *
#cargar sonidos
pg.mixer.pre_init(44100,-16,2,512)
mixer.init()
pg.init()
hit_fx = pg.mixer.Sound('assets/img/sounds/hit.wav')
hit_fx.set_volume(0.3)
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
vida_img = pg.image.load('assets/img/vidas/vida.png')
vida_img = pg.transform.scale(vida_img, ((vida_img.get_width()* 0.1), (vida_img.get_height()* 0.1)))

#NIVEL 1
world_data_1 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
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
world_data_2 = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,2,2,2,2,0,0,0,0,0,0,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[2,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[2,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
]
