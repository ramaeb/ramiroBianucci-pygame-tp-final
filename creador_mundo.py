import pygame as pg
from models.constantes import TILE_SIZE,ANCHO_VENTANA,ALTO_VENTANA
class Mundo():
    def __init__(self,data):
        self.tile_list = []
        #cargar foreground
        piedra_img = pg.image.load('assets/img/foreground/piedra.png')
        pasto_img = pg.image.load('assets/img/foreground/piedra_pasto.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pg.transform.scale(piedra_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pg.transform.scale(pasto_img,(TILE_SIZE,TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * TILE_SIZE
                    img_rect.y = row_count * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    def draw(self,screen):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])

def dibujo_grid(screen):
    for line in range(0,30):
        pg.draw.line(screen, (255, 255, 255), (0, line * TILE_SIZE), (ANCHO_VENTANA, line * TILE_SIZE))
        pg.draw.line(screen, (255, 255, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, ALTO_VENTANA))
