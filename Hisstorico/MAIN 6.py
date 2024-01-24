# SELECCIÓN DE FICHAS Y DESELECCIONA FICHA AL ELEGIR OTRA, FUNCIONA

import pygame
import sys

pygame.init()

# Definir colores *********************************************************************
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128,128,128)
AZUL = (59, 131, 189)
ROJO = (255, 105, 97)


DatosProvincia1 =""
DatosProvincia2 =""
DatosProvincia3 =""
Destinox = 0
Destinoy = 0


# Definir PANTALLA *********************************************************************
ANCHO, ALTO = 800, 600 # Definir el tamaño de la pantalla y crear la pantalla
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hispania in War")

# Tipos de letra y función para mostrar marcador ********************************************
consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')
font = pygame.font.Font(None, 20)



def muestra_texto(pantalla,fuente,texto,color, dimensiones, x, y):
	tipo_letra = pygame.font.Font(fuente,dimensiones)
	superficie = tipo_letra.render(texto,True, color)
	rectangulo = superficie.get_rect()
	rectangulo.center = (x, y)
	pantalla.blit(superficie,rectangulo)


# Definir clase FICHA *********************************************************************
class Ficha(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y, bando, ataque, defensa, salud):
        super().__init__()
        self.image = pygame.image.load(imagen).convert()
        self.image.set_colorkey(BLANCO) #para quitar el color de fondo blanco
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.selected = False
        self.bando = bando
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        
    def mover(self, x, y):
        pass

    def seleccionado(self):
        if self.selected:
            pygame.draw.rect(ventana, (255, 0, 0), self.rect, width=2, border_radius=5)

class Provincia(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y, bando, defensa, nombre):
        super().__init__()
        self.image = pygame.image.load(imagen).convert()
        self.image.set_colorkey(BLANCO) #para quitar el color de fondo blanco
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.selected = False
        self.bloqueado = True
        self.bando = bando
        self.defensa = defensa
        self.nombre = nombre

    def seleccionado(self):
        if self.selected:
            pygame.draw.rect(ventana, (255, 0, 0), self.rect, width=2, border_radius=5)

# INICIALIZACIÓN DE LAS FICHAS *********************************************************************
mis_sprites_fichas = pygame.sprite.Group()
mis_sprites_provincias = pygame.sprite.Group()
ficha1 = Ficha("img/caballero3.png",250 ,200, "Cristiano",20, 8, 45)
ficha2 = Ficha("img/caballeria2.png",325 ,375, "Musulmán",15,12,50)
andalucia = Provincia("img/andaluciasola.png", 350, 400, "cristiano", 50, "Andalucía")
extremadura = Provincia("img/extramadurasola.png", 250, 200, "cristiano", 60, "Extremadura") 
castillamancha = Provincia("img/castillamanchasola.png", 470, 170, "cristiano", 70, "Castilla la Mancha")
mis_sprites_provincias.add(andalucia)
mis_sprites_provincias.add(extremadura)
mis_sprites_provincias.add(castillamancha)
mis_sprites_fichas.add(ficha1)
mis_sprites_fichas.add(ficha2)

fichaSeleccionada = ficha1

jugador_actual = 1

# BUCLE DEL JUEGO *********************************************************************
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1): #el uno respresenta botón iqzdo, el 3 es el dcho
            # Verificar si se hizo clic en una ficha
            for ficha in mis_sprites_fichas: # Quitar la selección de cualquier otra ficha
                if ficha.selected: # Si hay ficha seleccionada la deselecciono
                    ficha.selected = not ficha.selected
                
                if ficha.rect.collidepoint(event.pos): # Selecciono o deselecciono si el evento del ratón colisiona
                   ficha.selected = True 
                   fichaSeleccionada = ficha

            """for provincia in mis_sprites_provincias:
                if provincia.selected:
                    provincia.selected = not provincia.selected

                if provincia.rect.collidepoint(event.pos):
                    provincia.selected = not provincia.selected
                     # Cargar variables para Mostrar datos de la provincia *******************************
                    DatosProvincia1 = f'{provincia.bando}'
                    DatosProvincia2 = f'{provincia.defensa}'
                    DatosProvincia3 = f'{provincia.nombre}'
            """


        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 3):
            
            for provincia in mis_sprites_provincias:
                if (provincia.rect.collidepoint(event.pos)) and (fichaSeleccionada.selected == True):
                #provincia.selected = not provincia.selected
                    fichaSeleccionada.rect.centerx = provincia.rect.centerx
                    fichaSeleccionada.rect.centery = provincia.rect.centery
                    fichaSeleccionada.selected = False  
                    print(provincia.nombre)  

    
    mis_sprites_fichas.update()
    mis_sprites_provincias.update()
    ventana.fill(NEGRO)  # Limpiar la pantalla
    
    
    #mapaEspana = pygame.image.load("img/Espana.png") # Dibujar mapa de fondo
    #ventana.blit(mapaEspana, (-150, 0))

    #pygame.draw.circle(ventana, NEGRO, (400, 375), 5) # Dibujar las capitales
    mis_sprites_provincias.draw(ventana)
    for sprites in mis_sprites_provincias: # para dibujar los seleccionados
        sprites.seleccionado()

    mis_sprites_fichas.draw(ventana)
    for sprites in mis_sprites_fichas: # para dibujar los seleccionados
        sprites.seleccionado()

    
    # Dibujar marcador ***************************************************************************************
    datosFichas = [
        "Bando: " + fichaSeleccionada.bando,
        "Ataque: " + str(fichaSeleccionada.ataque),
        "Defensa: " + str(fichaSeleccionada.defensa),
        "salud: " + str(fichaSeleccionada.salud)
    ]

    datosProvincias = [
        "Provincia: " + DatosProvincia3,
        "Bando: " + DatosProvincia1,
        "Defencas: " + DatosProvincia2
    ]

    text_surfaces = [font.render(line, True, BLANCO) for line in datosFichas]
    text_surfaces2 = [font.render(line, True, BLANCO) for line in datosProvincias]

    line_height = 20
    for i, text_surface in enumerate(text_surfaces):
        # Dibujar cada línea en la pantalla
        ventana.blit(text_surface, (30, (i+1) * line_height))

    line_height = 20
    for i, text_surface in enumerate(text_surfaces2):
        # Dibujar cada línea en la pantalla
        ventana.blit(text_surface, (30, (i+10) * line_height))
       
    # Pintar las cosas ********************************************************************************

    pygame.display.flip() # Dibujar las cosas
    pygame.time.Clock().tick(20)
    jugador_actual = 3 - jugador_actual
    #print(jugador_actual)
    