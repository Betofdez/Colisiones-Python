# SELECCIÓN DE FICHAS, FUNCIONA

import pygame
import sys

pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
BLACK = (0, 0, 0)
GRIS = (128,128,128)
AZUL = (59, 131, 189)
ROJO = (255, 105, 97)

ANCHO, ALTO = 800, 600 # Definir el tamaño de la pantalla y crear la pantalla
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hispania in War")

clock = pygame.time.Clock()

class Ficha(pygame.sprite.Sprite):

    def __init__(self, imagen, x, y):
        super().__init__()
        self.image = pygame.image.load(imagen).convert()
        self.image.set_colorkey(BLANCO) #para quitar el color de fondo blanco
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.selected = False
        
    def mover(self, x, y):
        pass

    def seleccionado(self):
        if self.selected:
            pygame.draw.rect(ventana, (255, 0, 0), self.rect, width=2, border_radius=5)


mis_sprites = pygame.sprite.Group()
ficha1 = Ficha("img/caballero3.png",50 ,150)
ficha2 = Ficha("img/caballero3.png",150 ,350)
mis_sprites.add(ficha1)
mis_sprites.add(ficha2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en una ficha
            for ficha in mis_sprites:
                if ficha.rect.collidepoint(event.pos):
                   ficha.selected = not ficha.selected 

                #print (ficha1.selected)
    
    mis_sprites.update()
    ventana.fill(AZUL)  # Limpiar la pantalla
    mis_sprites.draw(ventana)
    for sprites in mis_sprites: # para dibujar los seleccionados
        sprites.seleccionado()
    
    pygame.display.flip() # Dibujar las cosas
    pygame.time.Clock().tick(60)

    