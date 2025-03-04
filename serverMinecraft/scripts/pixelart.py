# Ejercicio 014 usando setBlock() Crear pixel art bloque por bloque
# El diagrama a seguir esta en: https://i.redd.it/80b6n18ejn241.jpg

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Necesitamos importar time
import time

# IDs de los materiales para usar
# Black Wool = 35,15
# Gray Wool = 35,7
# Light Gray Wooll = 35,8
# White wool = 35
# Brown Wool = 35,12
# Orange Wool = 35,1

# Vamos a crear una espada como pixel art cerca del origen
# bloque por bloque con la funcion mc.setBlock()" 

#Mover al jugador cerca del origen
mc.player.setTilePos(0, 5, 6)


#Vamos a construir la espada sobre Z = 0
# Z siempre sera 0 porque es un dibujo en 2D


# Linea linea 1 del pixel art
mc.setBlock(1, 4, 0, 35,15)
mc.setBlock(2, 4, 0, 35,15)
mc.setBlock(3, 4, 0, 35,15)

# Linea linea 2 del pixel art
mc.setBlock(1, 5, 0, 35,15)
mc.setBlock(2, 5, 0, 35,7)
mc.setBlock(3, 5, 0, 35,15)

# Linea linea 3 del pixel art
mc.setBlock(1, 6, 0, 35,15)
mc.setBlock(2, 6, 0, 35,15)
mc.setBlock(3, 6, 0, 35,1)
mc.setBlock(4, 6, 0, 35,12)
mc.setBlock(9, 6, 0, 35,15)
mc.setBlock(10, 6, 0, 35,15)

# Linea linea 4 del pixel art
mc.setBlock(3, 7, 0, 35,12)
mc.setBlock(4, 7, 0, 35,1)
mc.setBlock(5, 7, 0, 35,12)
mc.setBlock(7, 7, 0, 35,15)
mc.setBlock(8, 7, 0, 35,15)
mc.setBlock(9, 7, 0, 35,7)
mc.setBlock(10, 7, 0, 35,15)

# Linea linea 5 del pixel art
mc.setBlock(4, 8, 0, 35,12)
mc.setBlock(5, 8, 0, 35,1)
mc.setBlock(6, 8, 0, 35,15)
mc.setBlock(7, 8, 0, 35,7)
mc.setBlock(8, 8, 0, 35,7)
mc.setBlock(9, 8, 0, 35,15)

# Linea linea 6 del pixel art
mc.setBlock(5, 9, 0, 35,15)
mc.setBlock(6, 9, 0, 35,7)
mc.setBlock(7, 9, 0, 35,15)
mc.setBlock(8, 9, 0, 35,15)

# Linea linea 7 del pixel art
mc.setBlock(4, 10, 0, 35,15)
mc.setBlock(5, 10, 0, 35,7)
mc.setBlock(6, 10, 0, 35,15)
mc.setBlock(7, 10, 0, 35,8)
mc.setBlock(8, 10, 0, 35)
mc.setBlock(9, 10, 0, 35,15)

# Linea linea 8 del pixel art
mc.setBlock(4, 11, 0, 35,15)
mc.setBlock(5, 11, 0, 35,7)
mc.setBlock(6, 11, 0, 35,15)
mc.setBlock(7, 11, 0, 35)
mc.setBlock(8, 11, 0, 35,8)
mc.setBlock(9, 11, 0, 35)
mc.setBlock(10, 11, 0, 35,15)

# Linea linea 9 del pixel art
mc.setBlock(3, 12, 0, 35,15)
mc.setBlock(4, 12, 0, 35,7)
mc.setBlock(5, 12, 0, 35,15)
mc.setBlock(7, 12, 0, 35,15)
mc.setBlock(8, 12, 0, 35)
mc.setBlock(9, 12, 0, 35,8)
mc.setBlock(10, 12, 0, 35)
mc.setBlock(11, 12, 0, 35,15)

# Linea linea 10 del pixel art
mc.setBlock(3, 13, 0, 35,15)
mc.setBlock(4, 13, 0, 35,15)
mc.setBlock(8, 13, 0, 35,15)
mc.setBlock(9, 13, 0, 35)
mc.setBlock(10, 13, 0, 35,8)
mc.setBlock(11, 13, 0, 35)
mc.setBlock(12, 13, 0, 35,15)

# Linea linea 11 del pixel art
mc.setBlock(9, 14, 0, 35,15)
mc.setBlock(10, 14, 0, 35)
mc.setBlock(11, 14, 0, 35,8)
mc.setBlock(12, 14, 0, 35)
mc.setBlock(13, 14, 0, 35,15)

# Linea linea 12 del pixel art
mc.setBlock(10, 15, 0, 35,15)
mc.setBlock(11, 15, 0, 35)
mc.setBlock(12, 15, 0, 35,8)
mc.setBlock(13, 15, 0, 35)
mc.setBlock(14, 15, 0, 35,15)

# Linea linea 13 del pixel art
mc.setBlock(11, 16, 0, 35,15)
mc.setBlock(12, 16, 0, 35)
mc.setBlock(13, 16, 0, 35,8)
mc.setBlock(14, 16, 0, 35)
mc.setBlock(15, 16, 0, 35,15)

# Linea linea 14 del pixel art
mc.setBlock(12, 17, 0, 35,15)
mc.setBlock(13, 17, 0, 35)
mc.setBlock(14, 17, 0, 35,8)
mc.setBlock(15, 17, 0, 35)
mc.setBlock(16, 17, 0, 35,15)

# Linea linea 15 del pixel art
mc.setBlock(13, 18, 0, 35,15)
mc.setBlock(14, 18, 0, 35)
mc.setBlock(15, 18, 0, 35,8)
mc.setBlock(16, 18, 0, 35,15)

# Linea linea 16 del pixel art
mc.setBlock(14, 19, 0, 35,15)
mc.setBlock(15, 19, 0, 35,15)
mc.setBlock(16, 19, 0, 35,15)
