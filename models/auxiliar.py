import pygame as pg
    
class JugadorSprite():
    pass

#ALTERNA EL MOVIMIENTO DEL IDLE Y DEL WALK EN SPRITES.
def cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara):
    
    if (mueve_dere or mueve_izq):
        jugador.cambio_accion(1)
    elif dispara:
        jugador.cambio_accion(2)
    else:
        jugador.cambio_accion(0)