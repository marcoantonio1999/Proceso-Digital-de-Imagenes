from email.mime import image
import cv2
import numpy as np
import math
from tkinter import *
from PIL import Image, ImageTk

def euclides(bo,go,ro, b,g,r):
    return math.sqrt((bo-b)**2 + (go-g)**2+ (ro-r)**2 )


def obtenIndice(pixel):
    file = open("base.csv")
    distanciaActual = 1000
    indiceActual = 0
    for line in file:
        indice,b,g,r = line.split(",")
        distancia = euclides(pixel[0], pixel[1], pixel[2], float(b),float(g),float(r) )
        if distanciaActual > distancia:
            distanciaActual = distancia
            indiceActual= indice
            
    return indiceActual

entrada = input("introduce el nombre de la foto a la cual le quieres hacer el mosaico")

imagen = cv2.imread(entrada)

y,x,d = imagen.shape

anchoPorcentaje = 0.1
altoPorcentaje = 0.1

ancho = math.floor(x*anchoPorcentaje)
altura = math.floor(y*altoPorcentaje)

imagenRescalada = cv2.resize(imagen, (ancho,altura))

print("introce de nuevo la ruta del directorio donde te encuentras")
path = input()

file = open("base.csv")
y,x,d = imagenRescalada.shape
contador = 1
imgConcatY = []
for j in range(y):
    imgConcatX = []
    for i in range(x):
        if contador%100 ==0:
            print("estas en el pixel ",contador,":", (i,j), "de", y*x, "pixeles \n")
        contador += 1
        indice = obtenIndice(imagenRescalada[j,i])
        if contador%100 ==0:
            print("se cargo la imagen", "{}.jpg".format(indice))
        imagenPromedio = cv2.imread("{}/ImagenesProcesadas/{}.jpg".format(path,indice))
        
        imgConcatX.append(imagenPromedio)
    imgConcatY.append(imgConcatX)


listaYaConcatenar = []
for k in imgConcatY:
    imgNuevo = cv2.hconcat(k)
    listaYaConcatenar.append(imgNuevo)
    
imgFinal = cv2.vconcat(listaYaConcatenar)
cv2.imwrite("FINAL.jpg", imgFinal)
print("la imagen se guardo en FINAL.jpg")

