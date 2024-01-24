import pygame
pygame.init()
ventana = pygame.display.set_mode((1500,900))
pygame.display.set_caption("Hispania")


# Crea el objeto caballero y mapa
caballero = pygame.image.load("img/caballero2.png")
mapa = pygame.image.load("img/mapahist.png")
# Obtengo el rectángulo del objeto anterior
caballerorect = caballero.get_rect()
maparect = mapa.get_rect()
posicion = 0
"""  dfsdfgfd cv

"""
# Pongo el muñeco en el origen de coordenadas
caballerorect.move_ip(271,398)
maparect.move_ip(0,0)

# se define la letra por defecto
fuente = pygame.font.Font(None, 20)


jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
            pos = pygame.mouse.get_pos()
            columna = pos[0] # (LARGO + MARGEN)
            fila = pos[1] # (ALTO + MARGEN)
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
            if event.button == 3:
                mensajerr = "Botón 3"
            if event.button == 1:
                mensajerr = "Botón 1"   


# Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        caballerorect = caballerorect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        caballerorect = caballerorect.move(3,0)
    if keys[pygame.K_UP]:
        caballerorect = caballerorect.move(0,-3)
    if keys[pygame.K_DOWN]:
        caballerorect = caballerorect.move(0,3)

    puntoy = caballerorect.y
    puntox = caballerorect.x
    
    pos = pygame.mouse.get_pos()
    columna = pos[0] # (LARGO + MARGEN)
    fila = pos[1] # (LARGO + MARGEN)
    posicion =  "Posición: %d y eje y: %d. Ha pulsado: %d" % (columna,fila,mensajerr)
    posicioncaballero = "Posición: %d y eje y: %d" % (puntox,puntoy)
   
    # Se crea una variable que contendra el mensaje y el color, en este caso negro (0,0,0)
    #mensaje = fuente.render(posicion, 1, (0, 0, 0))
    #mensaje2 = fuente.render(posicioncaballero, 1, (0, 0, 0))

    ventana.fill((252, 243, 207))
    
    # Dibujo el muñeco y el mapa
    ventana.blit(mapa, maparect)
    ventana.blit(caballero, caballerorect)
    # Muestro las coordenadas del muñeco
    
    ventana.blit(mensaje, (850, 10))
    ventana.blit(mensaje2, (850, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()