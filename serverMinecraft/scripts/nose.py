from mcpi.minecraft import Minecraft

mc = Minecraft.create()

posUser = mc.player.getTilePos()

#altura
altura=100
radio=5

#base
mc.setBlocks(posUser.x+radio, posUser.y, posUser.z+radio, posUser.x-radio, posUser.y, posUser.z-radio, 35, 14)
mc.postToChat("base lista")

mc.setBlocks(posUser.x+1+radio, posUser.y, posUser.z+radio, posUser.x+radio+1, posUser.y+altura, posUser.z-radio, 35, 14)

mc.setBlocks(posUser.x-radio-1, posUser.y, posUser.z+radio, posUser.x-radio-1, posUser.y+altura, posUser.z-radio, 35, 14)

mc.setBlocks(posUser.x+radio, posUser.y, posUser.z+radio+1, posUser.x-radio, posUser.y+altura, posUser.z+radio+1, 35, 14)

mc.setBlocks(posUser.x+radio, posUser.y, posUser.z-radio-1, posUser.x-radio, posUser.y+altura, posUser.z-radio-1, 35, 14)

mc.postToChat("paredes listas")

yesca= posUser.y
z_pos = posUser.z-radio+1
x_pos= posUser.x

ipri= yesca+1

for x in range(x_pos, x_pos+radio-1):
    mc.setBlock(x,ipri,z_pos, 35, 10)
    mc.setBlock(x,ipri,z_pos-1, 35, 10)
    ipri=ipri+1
opt=0
x_pos=x_pos+radio-1
i=ipri
while( i <= (yesca+altura)):

    if(opt==0):
        #base
        mc.setBlocks(x_pos, i,z_pos, x_pos+1, i, z_pos-1, 35, 10)
        fin = z_pos+((radio*2)-2)
        while(z_pos<=fin):
            mc.setBlock(x_pos, i, z_pos, 35, 10)
            mc.setBlock(x_pos+1, i, z_pos, 35, 10)
            z_pos=z_pos+1
            i=i+1
        i=i-1
        z_pos=z_pos-1
        opt=1
    elif(opt==1):
        #base
        mc.setBlocks(x_pos, i,z_pos, x_pos+1, i, z_pos+1, 35, 10)
        fin = x_pos-((radio*2)-2)
        while(x_pos>=fin):
            mc.setBlock(x_pos, i, z_pos, 35, 10)
            mc.setBlock(x_pos, i, z_pos+1, 35, 10)
            x_pos=x_pos-1
            i=i+1
        i=i-1;
        x_pos=x_pos+1
        opt=2
    elif(opt==2):
        #base
        mc.setBlocks(x_pos, i,z_pos, x_pos-1, i, z_pos+1, 35, 10)
        fin = z_pos-((radio*2)-2)
        while(z_pos>=fin):
            mc.setBlock(x_pos, i, z_pos, 35, 10)
            mc.setBlock(x_pos-1, i, z_pos, 35, 10)
            z_pos=z_pos-1
            i=i+1
        i=i-1
        z_pos=z_pos+1
        opt=3
    else:
        #base
        mc.setBlocks(x_pos, i,z_pos, x_pos-1, i, z_pos-1, 35, 10)
        fin = x_pos+((radio*2)-2)
        while(x_pos<=fin):
            mc.setBlock(x_pos, i, z_pos, 35, 10)
            mc.setBlock(x_pos, i, z_pos-1, 35, 10)
            x_pos=x_pos+1
            i=i+1
        i=i-1
        x_pos=x_pos-1
        opt=0