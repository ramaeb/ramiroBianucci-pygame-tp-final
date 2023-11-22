import pygame as pg

from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
clock = pg.time.Clock()

color = (0,200,0)
ventana = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

mueve_dere = False
mueve_izq = False

juego_ejecutandose = True
jugador = Jugador(300,200,5,5)
mueve_dere = False
mueve_izq = False
while juego_ejecutandose:
    jugador.movimiento_lateral(mueve_dere,mueve_izq)
    #print(delta_ms)
    lista_eventos = pg.event.get()
    for event in lista_eventos:
        match event.type:
        
            case pg.QUIT:
                print('Estoy CERRANDO el JUEGO')
                juego_ejecutandose = False
                break
    
            case pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    mueve_dere = True
                if event.key == pg.K_LEFT:
                    mueve_izq = True
    
            case pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    mueve_dere = False
                if event.key == pg.K_LEFT:
                    mueve_izq = False


    ventana.fill(color) #llenamos de color verde la venta
    #screen.blit(back_img, back_img.get_rect())
    
    jugador.draw(screen)
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()