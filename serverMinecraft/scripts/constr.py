from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

posUser = mc.player.getTilePos()

def fill_vacio(x1: int ,y1 : int ,z1 : int,x2 : int,y2 : int,z2 : int,idblock : int , sub : int =0 ):
    mc.setBlocks(x1,y1,z1,x2,y2,z2, idblock, sub)
    if(y1>y2):
        y1-=1
        y2+=1
    else:
        y1+=1
        y2-=1
    
    if(x1>x2):
        x1-=1
        x2+=1
    else:
        x1+=1
        x2-=1

    if(z1>z2):
        z1-=1
        z2+=1
    else:
        z1+=1
        z2-=1

    mc.setBlocks(x1,y1,z1,x2,y2,z2, 0)


#altura
altura=5
radio=8

x=posUser.x
y=posUser.y
z=posUser.z

#base
fill_vacio(x+radio, y-1, z+radio, x-radio, y+altura, z-radio, 98)
mc.setBlock(x,y+altura-1,z,89)
mc.postToChat("base lista")

