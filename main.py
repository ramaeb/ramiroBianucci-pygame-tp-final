import pygame as pg
from models.auxiliar import *
from models.enemy.main_enemy import *
from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()
color = (0,200,0)
color_1 = (0,0,0)
back_img = pg.image.load('./assets/img/background/3.png')
back_img = pg.transform.scale(back_img, (ANCHO_VENTANA, ALTO_VENTANA))


pg.display.flip()
ventana = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
mueve_dere = False
mueve_izq = False

juego_ejecutandose = True
jugador = Jugador(300,200,5,5)
dispara = False
jugador.cayendo = True

while juego_ejecutandose:
    #MIENTRAS EL JUGADOR ESTÉ VIVO SE TOMAN TODOS LOS MOVIMIENTOS
    if jugador.jugador_vivo:
        jugador.movimiento_lateral(mueve_dere,mueve_izq)
        jugador.animacion()
        cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara,jugador.cayendo,jugador.jugador_vivo)
    else:
        mueve_dere = False
        mueve_izq = False
        jugador.movimiento_lateral(mueve_dere,mueve_izq)
        
        jugador.animacion()
        cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara,jugador.cayendo,jugador.jugador_vivo)
        
    cuadrado = pg.draw.rect(ventana,color_1,pg.Rect(100,200,60,60))
    enemies = pg.sprite.Group()
    enemy = Enemigo()
    enemies.add(enemy)
    colision = pg.sprite.spritecollide(jugador, enemies, False)

    if colision:
        print("COLISION!")
        jugador.jugador_vivo = False
#ventana = pg.image.load(R"assets\img\background\background.png")
    lista_eventos = pg.event.get()
    
    for event in lista_eventos:
        match event.type:
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
            #SETEO DE TECLAS
            case pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    mueve_dere = True
                if event.key == pg.K_LEFT:
                    mueve_izq = True
                if event.key == pg.K_e:
                    dispara = True
                    print("Ataco")
                if event.key == pg.K_o:
                    jugador.jugador_vivo = False
                    print("Ataco")
                if (event.key == pg.K_UP) and (not jugador.cayendo):
                    jugador.salta = True
                    jugador.cayendo = True
    
            case pg.KEYUP:
                if (event.key == pg.K_UP):
                    jugador.cayendo = True
                if event.key == pg.K_RIGHT:
                    mueve_dere = False
                if event.key == pg.K_LEFT:
                    mueve_izq = False
                if event.key == pg.K_e:
                    dispara = False



    screen.blit(back_img, back_img.get_rect())
    pg.draw.line(ventana,color_1,(0,300),(ANCHO_VENTANA,300))
    pg.draw.line(ventana,color_1,(0,200),(ANCHO_VENTANA,200))
    #screen.blit(back_img, back_img.get_rect())
    enemies.update()
    enemies.draw(screen)
    jugador.draw(screen)
    
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()