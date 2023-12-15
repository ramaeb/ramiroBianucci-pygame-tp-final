import pygame as pg
from nivel import *
from datos import *
from models.auxiliar import *
from models.player.bala import *
from models.enemy.main_enemy import *
from models.fruta import *
from creador_mundo import *
from creador_mundo import *
from models.enemy.main_enemy import Enemigo
from game_manager import Tiempo
from models.constantes import (
    ALTO_VENTANA, ANCHO_VENTANA, FPS
)
from models.player.main_player import Jugador

screen = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

clock = pg.time.Clock()
fuente = pg.font.SysFont("Arial",30)

#SETEO FRUTAS
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
mundo = Mundo(world_data_1)
jugador = Jugador(300,200,3,5)
enemigo = Enemigo(random.randrange(10, 300),600,3,5,mundo,jugador)

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
    '''
    USAR FORMS PARA LOS NIVELES Y LOS UPDATES HACERLOS DENTRO DEL NIVEL. CORTA
    form_activo = Form.get_active()
    form_activo.draw()
    form_activo.upd     
    '''
    
    screen.blit(back_img, back_img.get_rect())
    mundo.draw(screen)

    #screen.blit(back_img, back_img.get_rect())
    #centralizar en nivel(class) con metodo draw

    if jugador.jugador_vivo == False:
            mensaje_muerte = fuente.render("GAME OVER",True,(0,0,0))
            screen.blit(mensaje_muerte,(300,400))
            jugador.draw(screen)
            jugador.update(mundo)
            nivel.update()
            cancion_fx.fadeout(2)
    #win por puntos
    elif jugador.puntos == 500:
            mensaje_muerte = fuente.render("WIN",True,(0,0,0))
            screen.blit(mensaje_muerte,(350,300))
            cancion_fx.fadeout(2)
    else:
        tiempo = pg.time.get_ticks()//1000
        contador = Tiempo.update_tiempo(tiempo)
        Tiempo.update_puntos(jugador.puntos)
        if jugador.puntos != None:
            muestra_puntos =  Tiempo.update_puntos(jugador.puntos)

        #BLITEO Y DRAW
        enemigo.draw(screen)
        enemigo.update()
        jugador.draw(screen)
        jugador.update(mundo)
        bullet_group.draw(screen)
        bullet_group.update(jugador,enemigo)
        fruta_grupo.draw(screen)
        fruta_grupo.update(jugador)

        if tiempo > 30:
                mensaje_perdida = fuente.render("TIEMPO ACABADO",True,(0,0,0))
                screen.blit(mensaje_perdida,(450,300))
                screen.blit(muestra_puntos,(350,300))
                pg.quit()

        nivel.update(screen,tiempo)
        screen.blit(muestra_puntos,(500,20))
        screen.blit(Tiempo.update_tiempo(tiempo),(300,20))
    #MANEJO DE VIDAS !!
    
    delta_ms = clock.tick(FPS)
    pg.display.update()

pg.quit()