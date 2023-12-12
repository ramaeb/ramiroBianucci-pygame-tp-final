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

#MUNDO

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
jugador.cayendo = True

def dibujo_grid():

    tile_size = 70
    for line in range(0,30):
        pg.draw.line(screen, (255, 255, 255), (0, line * tile_size), (ANCHO_VENTANA, line * tile_size))
        pg.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, ALTO_VENTANA))

while juego_ejecutandose:
    #MIENTRAS EL JUGADOR ESTÉ VIVO SE TOMAN TODOS LOS MOVIMIENTOS
    

    #test ---
    cuadrado = pg.draw.rect(ventana,color_1,pg.Rect(100,200,60,60))
    enemies = pg.sprite.Group()
    enemy = Enemigo()
    enemies.add(enemy)
    colision = pg.sprite.spritecollide(jugador, enemies, False)
    #COLSION---
    if colision:
        print("COLISION!")
        jugador.jugador_vivo = False
    #COLSION---

    lista_eventos = pg.event.get()
    '''
    USAR FORMS PARA LOS NIVELES Y LOS UPDATES HACERLOS DENTRO DEL NIVEL. CORTA
    form_activo = Form.get_active()
    form_activo.draw()
    form_activo.upd    
    '''
    for event in lista_eventos:

        match event.type:
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
            
            #SETEO DE TECLAS
            case pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    jugador.mueve_dere = True
                if event.key == pg.K_LEFT:
                    jugador.mueve_izq = True
                if (event.key == pg.K_e):
                    jugador.disparando = True
                    print("Ataco")
                #test muerte
                if event.key == pg.K_o:
                    jugador.jugador_vivo = False
                    print("MUERTO")
                if (event.key == pg.K_UP) and (not jugador.cayendo):
                    jugador.salta = True
                    jugador.cayendo = True
    
            case pg.KEYUP:
                if (event.key == pg.K_UP):
                    jugador.cayendo = True
                if event.key == pg.K_RIGHT:
                    jugador.mueve_dere = False
                if event.key == pg.K_LEFT:
                    jugador.mueve_izq = False
                if event.key == pg.K_e:
                    jugador.disparando = False



    screen.blit(back_img, back_img.get_rect())
    pg.draw.line(ventana,color_1,(0,300),(ANCHO_VENTANA,300))
    #screen.blit(back_img, back_img.get_rect())
    enemies.update()
    enemies.draw(screen)
    #centralizar en nivel(class) con metodo draw
    jugador.draw(screen)
    jugador.update()
    bullet_group.draw(screen)
    bullet_group.update()
    dibujo_grid()
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()