#teletrasportar al punto de origen

import random

#inicializacion
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#con esta funcion se cambia la posicion del jugardor en x y z
# X y Z son 0
#Y es 110 para no quedar atorado en el suelo
mc.player.setTilePos(0,-40,0)

#postToChat lanza un mensaje en el chat
mc.postToChat('Mensaje mamate un guavo diego')

#setblock lanza un bloque en una cordanadas
mc.setBlock(0, -60, 0, 57)

#funciona como un fill
mc.setBlocks(5,-55,5, -5, -55, -5,20,4)