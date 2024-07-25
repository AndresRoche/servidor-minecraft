from mcpi.minecraft import Minecraft
import random
from time import sleep
mc = Minecraft.create()

timer= .2

def numero_aleatorios(inicio, final): 
    return random.randrange(inicio, final)

def visualArray(array_int, x_pos, y_pos, z_pos, opt : str):
    leng = len(array_int)
    if(opt=='x'):
        mc.setBlocks(x_pos, y_pos,z_pos, x_pos+leng, y_pos+50,z_pos, 0)
    else:
        mc.setBlocks(x_pos, y_pos,z_pos, x_pos, y_pos+50,z_pos+leng, 0)

    for x in array_int:
        mc.setBlocks(x_pos, y_pos+x,z_pos, x_pos, y_pos,z_pos, 57)
        if(opt=='x'):
            x_pos=x_pos+1
        else:
            z_pos=z_pos+1


def insertion_sort(arr, x, y, z, opt:str):

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        while (i >= 0 and arr[i] > key):
            arr[i + 1] = arr[i]
            i -= 1
            sleep(timer)
            visualArray(arr,x,y,z,opt)

        arr[i + 1] = key
        sleep(timer)
        visualArray(arr,x,y,z,opt)

    return arr



def bubble_sort(arr, x, y, z, opt:str):
  n = len(arr)

  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        sleep(timer)
        visualArray(arr,x,y,z,opt)

  return arr


def quick_sort(arr, low, high, x, y, z, opt:str):

  if low < high:
    pi = partition(arr, low, high,x,y,z,opt)

    quick_sort(arr, low, pi - 1,x,y,z,opt)
    quick_sort(arr, pi + 1, high,x,y,z,opt)

def partition(arr, low, high, x, y, z, opt:str):

  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
      sleep(timer)
      visualArray(arr,x,y,z,opt)

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  sleep(timer)
  visualArray(arr,x,y,z,opt)
  return i + 1


numeros=[]

for x in range(0, 20):
    numeros.append(numero_aleatorios(0,20))

posUser = mc.player.getTilePos()

x__a= posUser.x-(len(numeros)//2)

visualArray(array_int=numeros, x_pos=x__a, y_pos=posUser.y, z_pos=posUser.z+10, opt='x')

quick_sort(numeros,0 ,len(numeros)-1,x__a, posUser.y, posUser.z+10, 'x')