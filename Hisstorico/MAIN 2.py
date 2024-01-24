import pygame
import sys
import os

pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
BLACK = (0, 0, 0)
GRIS = (128,128,128)
AZUL = (59, 131, 189)
ROJO = (255, 105, 97)

# Definir el tamaño de la pantalla y crear la pantalla
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hispania in War")

clock = pygame.time.Clock()

def load_png(name):
    """ Carga la imagen y devuelve el objeto imagen"""
    fullname = os.path.join("img", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

class Ficha:

    def __init__(self, imagen):
        self.selected = False
        self.image, self.rect = load_png(imagen)
        self.rect.centerx = 400
        self.rect.centery = 100

    def draw(self):
        #ventana.blit(image, imagerec)
        pygame.draw.rect(ventana, ROJO, self.rect, width=2, border_radius=5)
        # pygame.draw.circle(ventana,ROJO, (100,100), 40, 1)
        if self.selected:
            pygame.draw.rect(ventana, ROJO, self.rect, width=2, border_radius=5)
        
    def mover(self, x, y):
        self.rect.move_ip(x, y)

# Crear fichas
#fichas = [Ficha(100, 100, "Infanteria", ROJO), Ficha(200, 200, "Infanteria", ROJO), Ficha(300, 300, "Infanteria", ROJO)]
ficha1 = Ficha("caballero2.png")
#ficha1.mover(100,100)
#pygame.draw.rect(ventana, ROJO, (50,50),(50,50), border_radius=5)
pygame.draw.rect(ventana, BLANCO, (100, 100, 50, 50), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en una ficha
            if ficha1.rect.collidepoint(event.pos):
                ficha1.selected = not ficha1.selected 
                ficha1.draw()
                print (ficha1.selected)
    
    ventana.fill(AZUL)  # Limpiar la pantalla
    ventana.blit(ficha1.image, ficha1.rect)
    
    #ficha1.draw()
    pygame.display.flip() # Dibujar las cosas
    pygame.time.Clock().tick(60)

    