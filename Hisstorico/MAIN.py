import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRIS = (128,128,128)
AZUL = (59, 131, 189)
ROJO = (255, 105, 97)
INFANTERIA = pygame.transform.scale(pygame.image.load("img/caballero.png"), (45,45))
#INFANTERIA.set.colorkey(WHITE)

# Definir el tamaño de la pantalla
ANCHO, ALTO = 800, 600
FILAS, COLUMNAS = 6 , 6
TAMANO_CUADRADO = ANCHO // COLUMNAS

# Definir el tamaño y el color de las fichas
FICHA_SIZE = 50
FICHA_COLOR = (0, 128, 255)

# Crear la pantalla
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hispania in War")

clock = pygame.time.Clock()

class Ficha:
    RELLENO = 15
    BORDE = 2
    
    def __init__(self, x, y, tipo, color):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.color = color
        self.selected = False
        self.rect = pygame.Rect(x, y, TAMANO_CUADRADO//2, TAMANO_CUADRADO//2)
       

    def draw(self, win):
        radio = TAMANO_CUADRADO//2 - self.RELLENO
        pygame.draw.circle(win, BLACK, (self.x, self.y), radio + self.BORDE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radio) # Agraga círculo de color para resaltar
        
        if self.selected:
            pygame.draw.circle(win, AZUL, (self.x, self.y), radio + self.BORDE)
        win.blit(INFANTERIA, (self.x - INFANTERIA.get_width()//2, self.y - INFANTERIA.get_height()//2)) # Pone una imagen en la pantlla

    def move(self, x, y):
        self.x = x
        self.y = y

    #def draw(self):
        
        #ventana.blit(self, self.rect)
        # pygame.draw.rect(ventana, FICHA_COLOR, self.rect, border_radius=5)
    #    if self.selected:
    #        pygame.draw.rect(ventana, (255, 0, 0), self.rect, width=2, border_radius=5)

# Crear fichas
fichas = [Ficha(100, 100, "Infanteria", ROJO), Ficha(200, 200, "Infanteria", ROJO), Ficha(300, 300, "Infanteria", ROJO)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en una ficha
            for ficha in fichas:
                if ficha.rect.collidepoint(event.pos):
                    ficha.selected = not ficha.selected
                    print ("entro")

    # Limpiar la pantalla
    ventana.fill(WHITE)

    # Dibujar fichas
    for ficha in fichas:
        ficha.draw(ventana)
        #ventana.blit(ficha, ficha.rect)
        

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)
