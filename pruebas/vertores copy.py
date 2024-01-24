import pygame
import sys

ANCHO, ALTO = 400, 400
BLANCO = (255, 255, 255)
contador = 0
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hispania in War")
vectorCaballero = pygame.Vector2(50,50)
vectorDestino = pygame.Vector2(100,100)

caballero = pygame.image.load("img/caballerocrismedieval.png")
move = False
while True:
    for event in pygame.event.get():
        chivato = False       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                while vectorCaballero != vectorDestino:
                    vectorCaballero.move_towards_ip(vectorDestino,1) # segundo argumento es distancia en pixeles


    ventana.fill(BLANCO)  # Limpiar la pantalla
    ventana.blit(caballero, vectorCaballero)
    pygame.display.flip()
    pygame.time.Clock().tick(20)