import pygame as pg
class Nivel():
    def __init__(self,lista_eventos,jugador):
        self.lista_eventos = lista_eventos
        self.jugador = jugador
    def update(self):
        for event in self.lista_eventos:

            match event.type:
                
                #SETEO DE TECLAS
                case pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.jugador.mueve_dere = True
                    if event.key == pg.K_LEFT:
                        self.jugador.mueve_izq = True
                    if (event.key == pg.K_e):
                        self.jugador.disparando = True
                        print("Ataco")
                    #test muerte
                    if event.key == pg.K_o:
                        self.jugador.jugador_vivo = False
                        print("MUERTO")
                    if (event.key == pg.K_UP) and (not self.jugador.cayendo):
                        #salto_fx.play()
                        self.jugador.salta = True
                        self.jugador.cayendo = True
        
                case pg.KEYUP:
                    if (event.key == pg.K_UP):
                        self.jugador.cayendo = True
                    if event.key == pg.K_RIGHT:
                        self.jugador.mueve_dere = False
                    if event.key == pg.K_LEFT:
                        self.jugador.mueve_izq = False
                    if event.key == pg.K_e:
                        self.jugador.disparando = False


