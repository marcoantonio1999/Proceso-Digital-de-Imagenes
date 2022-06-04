from email.mime import image
import cv2
import numpy as np
import math
from tkinter import *
from PIL import Image, ImageTk

def euclides(bo,go,ro, b,g,r):
    return math.sqrt(((bo-b)**2) + ((go-g)**2)+ ((ro-r)**2) )


def obtenIndice(pixel):
    file = open("base.csv")
    distanciaActual = 1000000
    indiceActual = 0
    for line in file:
        indice,b,g,r = line.split(",")
        distancia = euclides(pixel[0], pixel[1], pixel[2],b,g,r )
        if distanciaActual > distancia:
            distanciaActual = distancia
            indiceActual= indice
            
    return indiceActual

imagen = cv2.imread("imgO.jpg")

y,x,d = imagen.shape

anchoPorcentaje = 0.1
altoPorcentaje = 0.1

ancho = math.floor(x/anchoPorcentaje)
altura = math.floor(y/altoPorcentaje)

imagenRescalada = cv2.resize(imagen, (ancho,altura))



file = open("base.csv")

    
imgConcatY = []
for j in range(y):
    imgConcatX = []
    for i in range(x):
        imagenPromedio = cv2.inread("/home/marco/Documents/imgP/{}.jpg".format(obtenIndice(imagenRescalada[j,i])))
        imgConcatX.append(imagenPromedio)
    imgConcatY.append(imgConcatX)
         
for k in range(len(imgConcatX[0])):
    imgNuevo = cv2.vconcat(imgConcatX[k])
    cv2.imwrite("finalY{}.jpg".format(k+1), imgNuevo)
    
    
listay = []
for k in range(len(imgConcatX[0])):
    listay.append(cv2.imread( "finalY{}.jpg".format(k+1)))
    imgFinal = cv2.hconcat(listay)
    cv2.imwrite("Final.jpg", imgFinal)



