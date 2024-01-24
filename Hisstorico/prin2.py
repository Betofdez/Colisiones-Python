import pygame
pygame.init()
ventana = pygame.display.set_mode((640,480))

pygame.display.set_caption("Hispania")

def update(self):
     if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(self.game.mpos):
                    
                    self.image.load("img/caballero.png")


def seleccion(self,fil,col):
     self.selected
     self.seleccion(fil,col)


# Crea el objeto pelota
caballero = pygame.image.load("img/caballero2.png").convert()
mapa = pygame.image.load("img/mapa.png")
# Obtengo el rectángulo del objeto anterior
caballerorec = caballero.get_rect()
maparec = mapa.get_rect()
# Inicializo los valores con los que se van a mover la pelota

# Pongo la pelota en el origen de coordenadas
caballerorec.move_ip(100,100)
maparec.move_ip(100,100)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    
    # Muevo el caballero
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        caballerorec = caballerorec.move(-3,0)
    if keys[pygame.K_RIGHT]:
        caballerorec = caballerorec.move(3,0)
    if keys[pygame.K_UP]:
        caballerorec = caballerorec.move(0,-3)
    if keys[pygame.K_DOWN]:
        caballerorec = caballerorec.move(0,3)
  
  
    
    ventana.fill((252, 243, 207))
    # Dibujo las cosas
    ventana.blit(mapa, maparec)
    ventana.blit(caballero, caballerorec)
   
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()