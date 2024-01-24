import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
width, height = 800, 600

# Crear la ventana
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego por Turnos")

# Definir colores
white = (255, 255, 255)
blue = (0, 0, 255)

# Definir el jugador actual
current_player = 1

# Definir las coordenadas del jugador 1
player1_x, player1_y = 50, 300
player1_speed = 5

# Definir las coordenadas del jugador 2
player2_x, player2_y = 700, 300
player2_speed = 5

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Actualizar la posición del jugador actual
    if current_player == 1:
        if keys[pygame.K_LEFT] and player1_x > 0:
            player1_x -= player1_speed
        elif keys[pygame.K_RIGHT] and player1_x < width - 50:
            player1_x += player1_speed
        elif keys[pygame.K_UP] and player1_y > 0:
            player1_y -= player1_speed
        elif keys[pygame.K_DOWN] and player1_y < height - 50:
            player1_y += player1_speed
    elif current_player == 2:
        if keys[pygame.K_a] and player2_x > 0:
            player2_x -= player2_speed
        elif keys[pygame.K_d] and player2_x < width - 50:
            player2_x += player2_speed
        elif keys[pygame.K_w] and player2_y > 0:
            player2_y -= player2_speed
        elif keys[pygame.K_s] and player2_y < height - 50:
            player2_y += player2_speed

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar a los jugadores
    pygame.draw.rect(screen, blue, (player1_x, player1_y, 50, 50))
    pygame.draw.rect(screen, blue, (player2_x, player2_y, 50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

    # Cambiar al siguiente jugador en cada iteración del bucle
    current_player = 3 - current_player  # Alternar entre 1 y 2
    print(current_player)