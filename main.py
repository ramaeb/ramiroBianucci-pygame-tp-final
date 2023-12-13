import pygame as pg
from nivel import *
from pygame import mixer
from models.auxiliar import *
from models.player.bala import *
from models.enemy.main_enemy import *
from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

#sonidos y musica
pg.mixer.pre_init(44100,-16,2,512)
mixer.init()
pg.init()

#cargar sonidos
salto_fx = pg.mixer.Sound('assets/img/sounds/salto.wav')
salto_fx.set_volume(0.3)
#cancion_fx = pg.mixer.Sound('assets/img/sounds/cancion.mp3')
#cancion_fx.set_volume(0.1) 


clock = pg.time.Clock()
color = (0,200,0)
color_1 = (0,0,0)
back_img = pg.image.load('./assets/img/background/3.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))


pg.display.flip()
#SETEO VARIABLES
ventana = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
juego_ejecutandose = True
jugador = Jugador(300,200,3,5)
tile_size = 50
def dibujo_grid():

    tile_size = 50
'''
    for line in range(0,30):
        pg.draw.line(screen, (255, 255, 255), (0, line * tile_size), (ANCHO_VENTANA, line * tile_size))
        pg.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, ALTO_VENTANA))
'''
class Mundo():
    def __init__(self,data):
        self.tile_list = []
        #cargar foreground
        piedra_img = pg.image.load('assets/img/foreground/piedra.png')
        pasto_img = pg.image.load('assets/img/foreground/piedra_pasto.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pg.transform.scale(piedra_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pg.transform.scale(pasto_img,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
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
mundo = Mundo(world_data)

#cancion_fx.play()
while juego_ejecutandose:
    #MIENTRAS EL JUGADOR ESTÉ VIVO SE TOMAN TODOS LOS MOVIMIENTOS
    
    #test ---
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        if event.type == pg.QUIT:
                        print('Estoy CERRANDO el JUEGO')
                        juego_ejecutandose = False
    nivel = Nivel(lista_eventos,jugador)
    '''
    USAR FORMS PARA LOS NIVELES Y LOS UPDATES HACERLOS DENTRO DEL NIVEL. CORTA
    form_activo = Form.get_active()
    form_activo.draw()
    form_activo.upd     
    '''
    nivel.update()
    screen.blit(back_img, back_img.get_rect())
    mundo.draw()
    pg.draw.line(ventana,color_1,(0,300),(ANCHO_VENTANA,300))
    #screen.blit(back_img, back_img.get_rect())
    #centralizar en nivel(class) con metodo draw
    jugador.draw(screen)
    jugador.update(mundo)
    bullet_group.draw(screen)
    bullet_group.update()
    dibujo_grid()
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()