import pygame as pg
    
class JugadorSprite():
    pass

#ALTERNA EL MOVIMIENTO DEL IDLE Y DEL WALK EN SPRITES.
def cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara,saltando,colision_piso):
    
    if (saltando and (mueve_dere or mueve_izq)):
        jugador.cambio_accion(3)
    elif (mueve_dere or mueve_izq):
        jugador.cambio_accion(1)
    elif dispara:
        jugador.cambio_accion(2)
    elif saltando:
        jugador.cambio_accion(3)
    else:
        jugador.cambio_accion(0)