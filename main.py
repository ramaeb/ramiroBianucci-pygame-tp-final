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

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

clock = pg.time.Clock()
enemigo = Enemigo(600,200,3,5)

fruta_grupo = pg.sprite.Group()
fruta = Item(100,600,fruta_img)
fruta_grupo.add(fruta)
fruta = Item(100,300,fruta_img)
fruta_grupo.add(fruta)
fruta = Item(600,300,fruta_img)
fruta_grupo.add(fruta)
fruta = Item(600,600,fruta_img)
fruta_grupo.add(fruta)
fruta = Item(350,450,fruta_img)
fruta_grupo.add(fruta)


pg.display.flip()

#SETEO VARIABLES
ventana = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
juego_ejecutandose = True
jugador = Jugador(300,200,3,5)

mundo = Mundo(world_data_1)
cancion_fx.play()
while juego_ejecutandose:
    #MIENTRAS EL JUGADOR ESTÉ VIVO SE TOMAN TODOS LOS MOVIMIENTOS
    print(jugador.puntos)
    #test ---
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        if event.type == pg.QUIT:
                        print('Estoy CERRANDO el JUEGO')
                        juego_ejecutandose = False
    nivel = Juego(lista_eventos,jugador,screen,enemigo)
    '''o
    USAR FORMS PARA LOS NIVELES Y LOS UPDATES HACERLOS DENTRO DEL NIVEL. CORTA
    form_activo = Form.get_active()
    form_activo.draw()
    form_activo.upd     
    '''
    
    screen.blit(back_img, back_img.get_rect())
    mundo.draw(screen)

    #screen.blit(back_img, back_img.get_rect())
    #centralizar en nivel(class) con metodo draw
    jugador.draw(screen)
    enemigo.draw(screen)
    enemigo.update(mundo)
    jugador.update(mundo)
    bullet_group.draw(screen)
    bullet_group.update()
    fruta_grupo.draw(screen)
    fruta_grupo.update(jugador)
    dibujo_grid(screen)
    nivel.update()

    #MANEJO DE VIDAS !!
    
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()