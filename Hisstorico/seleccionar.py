import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir el tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir el tamaño y el color de las fichas
CHIP_SIZE = 50
CHIP_COLOR = (0, 128, 255)

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Selección de Fichas")

clock = pygame.time.Clock()

class Chip:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CHIP_SIZE, CHIP_SIZE)
        self.selected = False

    def draw(self):
        pygame.draw.rect(screen, CHIP_COLOR, self.rect, border_radius=5)
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), self.rect, width=2, border_radius=5)

# Crear fichas
chips = [Chip(100, 100), Chip(200, 100), Chip(300, 100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en una ficha
            for chip in chips:
                if chip.rect.collidepoint(event.pos):
                    chip.selected = not chip.selected

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar fichas
    for chip in chips:
        chip.draw()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)
