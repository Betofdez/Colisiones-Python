# TODAS LAS PROVINCIAS Y COMBATE COMPLETO

import pygame
import sys
import ctypes
import csv

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
Chivato = False

# Definir PANTALLA *********************************************************************
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ANCHO, ALTO = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 75
#ANCHO, ALTO = 1000, 640 # Definir el tamaño de la pantalla y crear la pantalla
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

def batalla(atacante, defensor):
    while atacante.salud>0 and defensor.salud>0:
        ataque = atacante.unidades * atacante.ataque * (atacante.salud/100)
        defensa = defensor.unidades * defensor.defensa * (defensor.salud/100)

        atacante.salud = atacante.salud - defensa
        defensor.salud = defensor.salud - ataque

    if atacante.salud < 0:
        atacante.salud = 0
    else:   
        defensor.salud = 0
    
    return atacante.salud , defensor.salud # devuelve tupla [a,b]

# Definir clase FICHA *********************************************************************
class Ficha(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y, bando, ataque, defensa, salud, unidades, nombre):
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
        self.unidades = unidades
        self.nombre = nombre
        
    def moverFicha(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
    
    def seleccionado(self):
        if self.selected:
            pygame.draw.rect(ventana, (255, 0, 0), self.rect, width=2, border_radius=5)

    def mostrarPuntuacion(self):
        pygame.draw.rect(ventana, (255, 0, 0), pygame.Rect(self.rect.centerx, self.rect.centery + 20, 20, 20), width=1, border_radius=5)
        
    def combateAcumula(self):
        pass


class Provincia(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y, bando, defensa, nombre, id):
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
        self.id = id
        self.dibujo = imagen

    def seleccionado(self):
        if self.selected:
            pygame.draw.rect(ventana, (255, 0, 0), self.rect, width=2, border_radius=5)

    def cambiarBando(self, img):
        self.image = pygame.image.load("img/IMG2/" + img + ".png").convert()  
        self.image.set_colorkey(BLANCO) #para quitar el color de fondo blanco    
        #self.rect = self.image.get_rect()  

# INICIALIZACIÓN DE LAS FICHAS *********************************************************************
mis_sprites_fichas = pygame.sprite.Group()
mis_sprites_provincias = pygame.sprite.Group()

with open('pruebas/Fichero_Provincias.csv', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for linea in csv_reader:

        provincia = Provincia(linea["Imagen"],float(linea["x"]),float(linea["y"]),linea["Bando"],float(linea["Defensa"]),linea["Nombre"],linea["Alias"])
        mis_sprites_provincias.add(provincia)

"""
andalucia = Provincia("img/IMG2/andaluciamora.png", 350, 525, "Musulmán", 50, "Andalucía","andalucia")
extremadura = Provincia("img/IMG2/extremaduramora.png", 263, 378, "Musulmán", 60, "Extremadura","extremadura") 
castillamancha = Provincia("img/IMG2/castillamanchamora.png", 432, 346, "Musulmán", 70, "Castilla la Mancha","castillamancha")
murcia = Provincia("img/IMG2/murciamora.png", 529, 468, "Musulmán", 70, "Murcia","murcia")
valencia = Provincia("img/IMG2/valenciamora.png", 577, 375, "Musulmán", 70, "Valencia","valencia")
castillaleon = Provincia("img/IMG2/castillaleonCris.png", 360, 192, "Cristiano", 70, "Castilla y León","castillaleon")
aragon = Provincia("img/IMG2/aragonCris.png", 563, 214, "Cristiano", 70, "Aragón","aragon")
cataluna = Provincia("img/IMG2/catalunaCris.png", 701, 191, "Cristiano", 70, "Cataluña","cataluna")
madrid = Provincia("img/IMG2/madridmora.png", 393, 281, "Musulmán", 70, "Madrid","madrid")
navarra = Provincia("img/IMG2/navarraCris.png", 514, 123, "Cristiano", 70, "Navarra","navarra")
rioja = Provincia("img/IMG2/riojaCris.png", 470, 149, "Cristiano", 70, "La Rioja","rioja")
galicia = Provincia("img/IMG2/galiciaCris.png", 175, 95, "Cristiano", 70, "Galicia","galicia")
asturias = Provincia("img/IMG2/asturiasCris.png", 300, 65, "Cristiano", 70, "Asturias","asturias")
cantabria = Provincia("img/IMG2/cantabriaCris.png", 385, 83, "Cristiano", 70, "Cantabria","cantabria")
paisvasco = Provincia("img/IMG2/vascongadasCris.png", 463, 96, "Cristiano", 70, "Vascongadas","vascongadas")

"""
aragon=mis_sprites_provincias.sprites()[6]
andalucia=mis_sprites_provincias.sprites()[0]
castillaleon=mis_sprites_provincias.sprites()[5]
extremadura=mis_sprites_provincias.sprites()[1]

ficha1 = Ficha("img/caballeria2.png",aragon.rect.centerx, aragon.rect.centery, "Cristiano",20, 8, 100, 3, "Conde") # imagen, x, y, bando, ataque, defensa, salud, unidades, nombreUnidad
ficha2 = Ficha("img/caballeria2MORO.png",andalucia.rect.centerx, andalucia.rect.centery, "Musulmán",15,12,100, 3, "General")
ficha3 = Ficha("img/caballeria2.png",castillaleon.rect.centerx, castillaleon.rect.centery, "Cristiano",15,12,100, 1, "Duque")
ficha4 = Ficha("img/caballeria2MORO.png",extremadura.rect.centerx, extremadura.rect.centery, "Musulmán",15,12,100, 1, "Jefe")

"""
mis_sprites_provincias.add(andalucia)
mis_sprites_provincias.add(extremadura)
mis_sprites_provincias.add(castillamancha)
mis_sprites_provincias.add(murcia)
mis_sprites_provincias.add(valencia)
mis_sprites_provincias.add(castillaleon)
mis_sprites_provincias.add(aragon)
mis_sprites_provincias.add(cataluna)
mis_sprites_provincias.add(madrid)
mis_sprites_provincias.add(navarra)
mis_sprites_provincias.add(rioja)
mis_sprites_provincias.add(galicia)
mis_sprites_provincias.add(asturias)
mis_sprites_provincias.add(cantabria)
mis_sprites_provincias.add(paisvasco)
"""

mis_sprites_fichas.add(ficha1)
mis_sprites_fichas.add(ficha2)
#mis_sprites_fichas.add(ficha3)
#mis_sprites_fichas.add(ficha4)

fichaSeleccionada = ficha1 # Necesito tener algo en la variable, por si luego se utiliza, sino da error el probrama
provinciaSeleccionada = provincia#andalucia # Necesito tener algo en la variable, por si luego se utiliza, sino da error el probrama

jugador_actual = 1

# BUCLE DEL JUEGO *********************************************************************
while True:
    for event in pygame.event.get():
        chivato = False
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

            for provincia in mis_sprites_provincias:
                if provincia.selected:
                    provincia.selected = not provincia.selected
                if provincia.rect.collidepoint(event.pos):
                    if fichaSeleccionada.selected == True:
                        provincia.selected = False
                    elif fichaSeleccionada.selected == False:
                        provincia.selected = True
                        provinciaSeleccionada = provincia

        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 3):
            
            for provincia in mis_sprites_provincias:
                if (provincia.rect.collidepoint(event.pos)) and (fichaSeleccionada.selected == True):
                    #Movimiento de la ficha
                    fichaSeleccionada.moverFicha(provincia.rect.centerx, provincia.rect.centery)
                    fichaSeleccionada.selected = False 
                    # FUNCION PARA SUMAR CIFRAS O COMBATE
                    for ficha in mis_sprites_fichas:
                        if (ficha != fichaSeleccionada) and (ficha.rect.centerx == fichaSeleccionada.rect.centerx) and (ficha.rect.centery == fichaSeleccionada.rect.centery):
                            chivato=True
                            if (ficha.bando == fichaSeleccionada.bando): # suma fichas y elimina ficha
                                fichaSeleccionada.unidades = ficha.unidades + fichaSeleccionada.unidades
                                mis_sprites_fichas.remove(ficha) # Elimino la ficha, para dejar una sola con todas las unidades    
                            else: # batalla
                                print("Entro en batalla")
                                resultado = batalla(fichaSeleccionada,ficha)
                                fichaSeleccionada.salud = resultado[0] #atacante
                                ficha.salud = resultado[1]  #defensor
                                if ficha.salud <=0: 
                                    mis_sprites_fichas.remove(ficha)
                                    if provincia.bando == "Musulmán":
                                        provincia.bando = "Cristiano"
                                        provincia.cambiarBando(provincia.id +"Cris")          
                                    else:
                                        provincia.bando = "Musulmán"
                                        provincia.cambiarBando(provincia.id +"mora") 
                                if fichaSeleccionada.salud <=0:
                                    mis_sprites_fichas.remove(fichaSeleccionada)
                                    if provincia.bando == "Musulmán":
                                        provincia.bando = "Cristiano"
                                        provincia.cambiarBando(provincia.id +"Cris")
                                    else:
                                        provincia.bando = "Musulmán"
                                        provincia.cambiarBando(provincia.id +"mora")                       
                            break

                    if chivato == False:
                        print(provincia.bando)
                        print(fichaSeleccionada.bando)
                        print(chivato)
                        if (provincia.bando == "Musulmán") and (fichaSeleccionada.bando == "Cristiano"):
                            provincia.bando="Cristiano"
                            provincia.cambiarBando(provincia.id +"Cris")
                        elif (provincia.bando == "Cristiano") and (fichaSeleccionada.bando == "Musulmán"):
                            provincia.bando="Musulmán"
                            provincia.cambiarBando(provincia.id +"mora")
                        break        

                    
    
    mis_sprites_fichas.update()
    mis_sprites_provincias.update()
    ventana.fill(BLANCO)  # Limpiar la pantalla
    
    
    #mapaEspana = pygame.image.load("img/Espana.png") # Dibujar mapa de fondo
    #ventana.blit(mapaEspana, (-150, 0))

    #pygame.draw.circle(ventana, NEGRO, (400, 375), 5) # Dibujar las capitales
    mis_sprites_provincias.draw(ventana)
    for sprites in mis_sprites_provincias: # para dibujar los seleccionados
        sprites.seleccionado()

    mis_sprites_fichas.draw(ventana)
    for sprites in mis_sprites_fichas: # para dibujar los seleccionados
        sprites.seleccionado()
        sprites.mostrarPuntuacion()
        # Mostrar datos de las unidades de la ficha seleccionada, junto a la ficha
        puntuacion = font.render(str(sprites.unidades), True, NEGRO)
        puntuacion_rect = puntuacion.get_rect(center=(sprites.rect.centerx + 9, sprites.rect.centery + 29))
        ventana.blit(puntuacion, puntuacion_rect)  

    
    # Dibujar MARCADOR ***************************************************************************************
    datosFichas = [
        "Bando: " + fichaSeleccionada.bando,
        "Ataque: " + str(fichaSeleccionada.ataque),
        "Defensa: " + str(fichaSeleccionada.defensa),
        "Salud: " + str(round(fichaSeleccionada.salud)),
        "Unidades " + str(fichaSeleccionada.unidades)
    ]

    datosProvincias = [
        "Provincia: " + provinciaSeleccionada.nombre,
        "Bando: " + provinciaSeleccionada.bando,
        "Defensas: " + str(provinciaSeleccionada.defensa)
    ]

    text_surfaces = [font.render(line, True, AZUL) for line in datosFichas]
    text_surfaces2 = [font.render(line, True, AZUL) for line in datosProvincias]

    line_height = 20
    for i, text_surface in enumerate(text_surfaces): # fichas
        # Dibujar cada línea en la pantalla
        ventana.blit(text_surface, (730, 550 + i * line_height))

    line_height = 20
    for i, text_surface in enumerate(text_surfaces2): # provincias
        # Dibujar cada línea en la pantalla
        ventana.blit(text_surface, (700, 350 + i * line_height))
    # Dibujar eb el marcador la figura junto a los datos *********************************************
    if fichaSeleccionada.bando == "Cristiano":
        imagen = pygame.image.load('img/caballerocrismedieval.png')
    else:
        imagen = pygame.image.load('img/caballeromoro.png')

    rect_imagen = imagen.get_rect()
    rect_imagen.topleft = (550, 550)
    ventana.blit(imagen, rect_imagen)
    pygame.draw.rect(ventana, NEGRO, rect_imagen, width=2, border_radius=5)

    imagenprov = pygame.image.load(provinciaSeleccionada.dibujo)
    rect_imagenprov = imagenprov.get_rect()
    rect_imagenprov.topleft = (850,300)
    ventana.blit(imagenprov, rect_imagenprov)
    pygame.draw.rect(ventana, NEGRO, rect_imagenprov, width=2, border_radius=5)



    # Pintar las cosas ********************************************************************************

    pygame.display.flip() # Dibujar las cosas
    pygame.time.Clock().tick(20)
    jugador_actual = 3 - jugador_actual
    #print(jugador_actual)
    