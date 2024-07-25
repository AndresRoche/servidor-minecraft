import cv2
import sys
from mcpi.minecraft import Minecraft
from pathlib import Path
from time import sleep
import math

timer= .2
mc = Minecraft.create()


class Colores:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

colores_block_minecraft = {
    "White":0,
    "Orange":1,
    "Magenta":2,
    "Light_Blue":3,
    "Yellow":4,
    "Lime":5,
    "Pink":6,
    "Grey":7,
    "Light_Grey":8,
    "Cyan":9,
    "Purple":10,
    "Blue":11,
    "Brown":12,
    "Green":13,
    "Red":14,
    "Black":15
}

colores_dict = {
    "White" : Colores(255, 255, 255),
    "Orange" : Colores(255, 165, 0),
    "Magenta" : Colores(255, 0, 255),
    "Light_Blue" : Colores(135, 206, 250),
    "Yellow" : Colores(255, 255, 0),
    "Lime" : Colores(0, 255, 0),
    "Pink" : Colores(255, 192, 203),
    "Grey" : Colores(128, 128, 128),
    "Light_Grey" : Colores(211, 211, 211),
    "Cyan" : Colores(0, 255, 255),
    "Purple" : Colores(128, 0, 128),
    "Blue" : Colores(0, 0, 255),
    "Brown" : Colores(165, 42, 42),
    "Green" : Colores(0, 128, 0),
    "Red" : Colores(255, 0, 0),
    "Black" : Colores(0, 0, 0)
}

print(sys.argv[1])

imagen = cv2.imread(str(sys.argv[1]))

def getdistancia(r,g,b, colores_class):
  puntox= math.pow(int(r)-int(colores_class.r),2)
  puntoy= math.pow(int(g)-int(colores_class.g),2)
  puntoz= math.pow(int(b)-int(colores_class.b),2)
  return math.sqrt(puntox+puntoy+puntoz)



def colorBlockWool(r,g,b):
    distanciaColor = {
        "White" : getdistancia(r,g,b,colores_dict["White"]),
        "Orange" : getdistancia(r,g,b,colores_dict["Orange"]),
        "Magenta" : getdistancia(r,g,b,colores_dict["Magenta"]),
        "Light_Blue" : getdistancia(r,g,b,colores_dict["Light_Blue"]),
        "Yellow" : getdistancia(r,g,b,colores_dict["Yellow"]),
        "Lime" : getdistancia(r,g,b,colores_dict["Lime"]),
        "Pink" : getdistancia(r,g,b,colores_dict["Pink"]),
        "Grey" : getdistancia(r,g,b,colores_dict["Grey"]),
        "Light_Grey" : getdistancia(r,g,b,colores_dict["Light_Grey"]),
        "Cyan" : getdistancia(r,g,b,colores_dict["Cyan"]),
        "Purple" : getdistancia(r,g,b,colores_dict["Purple"]),
        "Blue" : getdistancia(r,g,b,colores_dict["Blue"]),
        "Brown" : getdistancia(r,g,b,colores_dict["Brown"]),
        "Green" : getdistancia(r,g,b,colores_dict["Green"]),
        "Red" : getdistancia(r,g,b,colores_dict["Red"]),
        "Black" : getdistancia(r,g,b,colores_dict["Black"])
    }

    menor= sys.maxsize
    clave=""
    for dist in distanciaColor:
       #print(dist ,distanciaColor.get(dist))
       if(menor>distanciaColor.get(dist)):
          menor=distanciaColor.get(dist)
          clave=dist
    
    return str(clave)
       



if(imagen.shape[0]>100 or imagen.shape[1]>100):
    print("Imagen demasiado grande")
    exit()


posUser = mc.player.getTilePos()

x=posUser.x+(imagen.shape[1]//2)
y=posUser.y+imagen.shape[0]
z=posUser.z+15

for fila in range(imagen.shape[0]):
    for columna in range(imagen.shape[1]):
        # Obtener el valor del píxel actual
        pixel = imagen[fila, columna]

        # Separar los valores RGB
        azul, verde, rojo = pixel

        hola = colorBlockWool(rojo, verde, azul)

        # Imprimir el color del píxel
        
        print(hola)

        mc.setBlock(x,y,z,35, colores_block_minecraft[hola])
        x-=1

    y-=1
    x=posUser.x+(imagen.shape[1]//2)

