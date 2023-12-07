import pygame as pg
    
class JugadorSprite():
    pass

#ALTERNA EL MOVIMIENTO DEL IDLE Y DEL WALK EN SPRITES.
def cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara,saltando,muerte):
    
    if (saltando and (mueve_dere or mueve_izq)):
        jugador.cambio_accion(3)
    elif (mueve_dere or mueve_izq):
        jugador.cambio_accion(1)
    elif dispara and (muerte == False):
        jugador.cambio_accion(2)
    elif saltando and (muerte == False):
        jugador.cambio_accion(3)
   # elif muerte:
   #   jugador.cambio_accion(4)
    else:
        jugador.cambio_accion(0)