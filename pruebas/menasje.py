import pygame
import csv
import sys

BLANCO = (255, 255, 255)

pygame.init()

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

mis_sprites_provincias = pygame.sprite.Group()

with open('pruebas/Fichero_Provincias.csv', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for linea in csv_reader:

        provincia = Provincia(linea["Imagen"],linea["x"],linea["y"],linea["Bando"],linea["Defensa"],linea["Nombre"],linea["Alias"])
        mis_sprites_provincias.add(provincia)
        print(provincia.nombre)
        print(linea)
#provincia = Provincia(linea)
for provincia in mis_sprites_provincias:
    print(provincia.imagen)
    print("hola")

#print (mis_sprites_provincias[1])

while True:
    for event in pygame.event.get():
        for provincia in mis_sprites_provincias:
            print(provincia.imagen)
            print("hola")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        print("hola")