# PANELES DE INFORMACIÓN FUNCIONANDO CORRECTAMENTE Y COLOCADOS

import pygame
import sys
import ctypes # para conocer la pantalla que tiene el usuario
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

ventanaEmergente=False
# Tipos de letra y función para mostrar marcador ********************************************

#consolas = pygame.font.match_font('consolas')
#times = pygame.font.match_font('times')
#arial = pygame.font.match_font('arial')
#courier = pygame.font.match_font('courier')
font = pygame.font.Font(None, 30)

def ventanaEmergenteDef(resultado, pantalla):
        ventana_emergente = pygame.Surface((400, 200))
        ventana_emergente.fill(BLANCO)
        rect_ventana_emergente = ventana_emergente.get_rect(center=(ANCHO - 300, 150)) #center=(400 // 2, 200 // 2)
 
        # Dibujar la ventana emergente en la pantalla principal
        ventana.blit(ventana_emergente, rect_ventana_emergente)
        for i, nDatos in enumerate(resultado):
            textoEmergente = font.render("Salud Atacante: " + str(round(nDatos[0])), True, NEGRO) # fichaAtacante.ataque
            textoEmergente2 = font.render("Salud Defensora: " + str(round(nDatos[1])), True, NEGRO) # fichaDefensora
        
            pantalla.blit(textoEmergente, (rect_ventana_emergente.x + 30, rect_ventana_emergente.y  + 50 + i * 50))
            pantalla.blit(textoEmergente2, (rect_ventana_emergente.x + 30, rect_ventana_emergente.y  + 70 + i * 50))
        
        pygame.draw.rect(ventana, NEGRO, pygame.Rect(rect_ventana_emergente.x, rect_ventana_emergente.y, 400, rect_ventana_emergente.y  + 100 + i * 50), width=1, border_radius=5)



def batalla(atacante, defensor):
    datosCombate=[]
    while atacante.salud>0 and defensor.salud>0:
        ataque = atacante.unidades * atacante.ataque * (atacante.salud/100)
        defensa = defensor.unidades * defensor.defensa * (defensor.salud/100)

        atacante.salud = atacante.salud - defensa
        defensor.salud = defensor.salud - ataque
        datosCombate.append([atacante.salud, defensor.salud])

    if atacante.salud < 0:
        atacante.salud = 0
    else:   
        defensor.salud = 0
    
    print(datosCombate)
    return datosCombate #atacante.salud , defensor.salud # devuelve tupla [a,b]

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

# INICIALIZACIÓN DE LAS FICHAS Y PROVINCIAS *********************************************************************
mis_sprites_fichas = pygame.sprite.Group()
mis_sprites_provincias = pygame.sprite.Group()

with open('data/Fichero_Provincias.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=';') # Dictreader es para crear diccionario y poder buscar por cabecera
    for linea in csv_reader:

        provincia = Provincia(linea["Imagen"],float(linea["x"]),float(linea["y"]),linea["Bando"],float(linea["Defensa"]),linea["Nombre"],linea["Alias"])
        mis_sprites_provincias.add(provincia)

with open('data/Fichero_Fichas.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=';') # Dictreader es para crear diccionario y poder buscar por cabecera
    for linea in csv_reader:

        ficha = Ficha(linea["Imagen"], float(linea["x"]), float(linea["y"]), linea["Bando"], float(linea["Ataque"]), float(linea["Defensa"]), float(linea["Salud"]), float(linea["Unidades"]), linea["Nombre"])
        mis_sprites_fichas.add(ficha)


fichaSeleccionada = mis_sprites_fichas.sprites()[1] # Necesito tener algo en la variable, por si luego se utiliza, sino da error el probrama
provinciaSeleccionada = mis_sprites_provincias.sprites()[1]  # Necesito tener algo en la variable, por si luego se utiliza, sino da error el probrama

jugador_actual = 1

# BUCLE DEL JUEGO *********************************************************************
while True:
    for event in pygame.event.get():
        chivato = False       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()                
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1): #el uno respresenta botón iqzdo, el 3 es el dcho
            ventanaEmergente=False #para quitar ventana emergente si está activa porque hubo combate
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
                            else: # BATALLA ******** BATALLA ************* BATALLA ******************
                                resultado = batalla(fichaSeleccionada,ficha)
                                ultimoResultado = resultado [-1]
                                fichaSeleccionada.salud = ultimoResultado[0] #atacante
                                ficha.salud = ultimoResultado[1]  #defensor
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
                                ventanaEmergente = True                       
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
    
    

    mis_sprites_provincias.draw(ventana)
    for sprites in mis_sprites_provincias: # para dibujar los seleccionados
        sprites.seleccionado()

    mis_sprites_fichas.draw(ventana)
    for sprites in mis_sprites_fichas: # para dibujar los seleccionados
        sprites.seleccionado()
        sprites.mostrarPuntuacion()
        # Mostrar datos de las unidades de la ficha seleccionada, junto a la ficha
        puntuacion = font.render(str(round(sprites.unidades)), True, NEGRO)
        puntuacion_rect = puntuacion.get_rect(center=(sprites.rect.centerx + 9, sprites.rect.centery + 29))
        ventana.blit(puntuacion, puntuacion_rect)  

    
    # Dibujar MARCADOR ***************************************************************************************
    datosFichas = [
        "Bando: " + fichaSeleccionada.bando,
        "Ataque: " + str(fichaSeleccionada.ataque),
        "Defensa: " + str(fichaSeleccionada.defensa),
        "Salud: " + str(round(fichaSeleccionada.salud)),
        "Unidades " + str(round(fichaSeleccionada.unidades))
    ]

    datosProvincias = [
        "Provincia: " + provinciaSeleccionada.nombre,
        "Bando: " + provinciaSeleccionada.bando,
        "Defensas: " + str(provinciaSeleccionada.defensa)
    ]

    text_surfaces = [font.render(line, True, AZUL) for line in datosFichas]
    text_surfaces2 = [font.render(line, True, AZUL) for line in datosProvincias]

    line_height = 25
    for i, text_surface in enumerate(text_surfaces): # fichas
        # Dibujar cada línea en la pantalla
        ventana.blit(text_surface, (ANCHO - 350, ALTO - 575 + i * line_height)) #730,550

    line_height = 25
    for i, text_surface in enumerate(text_surfaces2): # provincias
        # Dibujar cada línea en la pantalla
        ventana.blit(text_surface, (ANCHO - 350, ALTO - 400 + i * line_height)) #730,550
    # Dibujar eb el marcador la figura junto a los datos *********************************************
    if fichaSeleccionada.bando == "Cristiano":
        imagen = pygame.image.load('img/caballerocrismedieval.png')
    else:
        imagen = pygame.image.load('img/caballeromoro.png')

    imagenescala = pygame. transform.scale(imagen,(175,175)) # para ajustar la imagen a un tamaño determinado
    rect_imagen = imagenescala.get_rect() # FICHA
    rect_imagen.topleft = (ANCHO - 550, ALTO - 600) #650,300
    ventana.blit(imagenescala, rect_imagen)
    pygame.draw.rect(ventana, NEGRO, rect_imagen, width=2, border_radius=5)

    imagenprov = pygame.image.load(provinciaSeleccionada.dibujo) # PROVINCIA
    imagenprovescala = pygame. transform.scale(imagenprov,(175,175))  # para ajustar la imagen a un tamaño determinado
    rect_imagenprov = imagenprovescala.get_rect()
    rect_imagenprov.topleft = (ANCHO - 550,ALTO - 400) #550,550
    ventana.blit(imagenprovescala, rect_imagenprov)
    pygame.draw.rect(ventana, NEGRO, rect_imagenprov, width=2, border_radius=5)

    
    # Ventana Emergente ********************************************************************
    if ventanaEmergente == True:
        ventanaEmergenteDef(resultado, ventana)

    # *************************************************************************************
    
    # Pintar las cosas ********************************************************************************

    pygame.display.flip() # Dibujar las cosas
    pygame.time.Clock().tick(20)
    jugador_actual = 3 - jugador_actual
    #print(jugador_actual)
    