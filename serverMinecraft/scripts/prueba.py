from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

def numero_aleatorios(inicio, final): 
    return random.randrange(inicio, final)

#bloqueID = mc.getBlock(11, -60, 1)
i = 0

while(i <= 30):
    x = numero_aleatorios(-100, 100)
    y = numero_aleatorios(1, 64)
    z = numero_aleatorios(-100, 100)
   #subBlock = numero_aleatorios(0, 15)

    #idblock = mc.getBlock(x,y,z)
    
   
    mc.setBlock(x,y,z,4) 

    i = i + 1


print('listo')
mc.postToChat('listo')
#mc.postToChat(num_ran)