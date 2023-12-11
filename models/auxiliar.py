import pygame as pg
    
class JugadorSprite():
    pass

#ALTERNA EL MOVIMIENTO DEL IDLE Y DEL WALK EN SPRITES.
'''
def cambio_sprites_movimiento(mueve_dere,mueve_izq,jugador,dispara,saltando,vivo):
    if vivo:
        if (saltando and (mueve_dere or mueve_izq)):
            jugador.cambio_accion(2)
        elif (mueve_dere or mueve_izq):
            jugador.cambio_accion(1)
        elif dispara:
            jugador.cambio_accion(3)
        elif saltando:
            jugador.cambio_accion(2)
    # elif muerte:
    #   jugador.cambio_accion(4)
        else:
            jugador.cambio_accion(0)
    else:
        jugador.cambio_accion(4)

'''