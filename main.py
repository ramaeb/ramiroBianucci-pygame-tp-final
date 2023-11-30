import pygame as pg
from models.auxiliar import *
from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

color = (0,200,0)
color_1 = (0,0,0)
ventana = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

mueve_dere = False
mueve_izq = False

juego_ejecutandose = True
jugador = Jugador(300,200,5,5)
mueve_dere = False
mueve_izq = False
saltando = False
dispara = False
while juego_ejecutandose:
    #MIENTRAS EL JUGADOR ESTÉ VIVO SE TOMAN TODOS LOS MOVIMIENTOS
    if jugador.jugador_vivo:
        jugador.movimiento_lateral(mueve_dere,mueve_izq)
        jugador.animacion()
        cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara)
        
    #print(delta_ms)
    lista_eventos = pg.event.get()
    
    for event in lista_eventos:
        
        match event.type:
            
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
            
            case pg.KEYDOWN:
                if event.key == pg.K_UP and saltando == False:
                    jugador.salta = True
                    saltando = True
                if event.key == pg.K_RIGHT:
                    mueve_dere = True
                if event.key == pg.K_LEFT:
                    mueve_izq = True
                
                if event.key == pg.K_e:
                    dispara = True
                    print("Ataco")

            case pg.KEYUP:
                if event.key == pg.K_UP:
                    jugador.salta = False
                if event.key == pg.K_RIGHT:
                    mueve_dere = False
                if event.key == pg.K_LEFT:
                    mueve_izq = False
                if event.key == pg.K_e:
                    dispara = False



    ventana.fill(color) #llenamos de color verde la venta
    pg.draw.line(ventana,color_1,(0,300),(ANCHO_VENTANA,200))
    #screen.blit(back_img, back_img.get_rect())
    
    jugador.draw(screen)
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()