from cgi import print_environ
from curses.ascii import BS
import pathlib
import os
import os.path
from PIL import Image
import cv2
import csv 
    
def calculaProm(img):
    y,x,d = img.shape

    bSum = 0
    gSum = 0
    rSum = 0


    for j in range(y):
        for i in range(x):
            bSum += img[j,i,0]
            gSum += img[j,i,1]
            rSum += img[j,i,2]

    bProm = bSum/(x*y)
    gProm = gSum/(x*y)
    rProm = rSum/(x*y)
    return [bProm, gProm, rProm]

entrada = int(input("introduce el numero de fotos que tiene tu archivo ImagenesProcesar"))
print("introuce la ruta completa del directorio donde te ecuentras")
print("ejemplo")
print("Linux:   /home/marco/Documents/")
print("Windos:  C:usrs/marco/Documents/")

path = input()

print("Se creara un archivo llamado base,csv donde se guardara el promedio rgb por cada imagen procesada")

with open('base.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for i in range(entrada):
        imagen = cv2.imread("{}ImagenesProcesadas/{}.jpg".format(path,i))
        prom = calculaProm(imagen)
        prom = [i] + prom
        writer.writerow(prom)
