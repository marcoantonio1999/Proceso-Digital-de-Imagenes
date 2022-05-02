from email.mime import image
from tkinter import *
import cv2
import math
from PIL import Image, ImageTk
import copy
import numpy as np

imagen = cv2.imread("photo.jpg")


def calSuma(matriz):
    blue = 0
    green = 0
    red = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            blue = matriz[i][j][0] + blue
            green = matriz[i][j][1] + green
            red = matriz[i][j][2] + red
            
    return blue, green, red


def blur(imagen, k):
    x,y,d = imagen.shape
    
    for i in range(x):
        for j in range(y):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                continue

            porcion = imagen[i-(k//2):i+(k//2)+1 , j-(k//2):j+(k//2)+1]
            mul = (1/(k*k))*porcion
            b,g,r = calSuma(mul)
                   
            imagen.itemset((i,j,0),b)
            imagen.itemset((i,j,1),g)
            imagen.itemset((i,j,2),r)
    return imagen

def motionBlur(imagen, k):
    x,y,d = imagen.shape
    copia = imagen.copy()
    matrizS = []
    for i in range(k):
        matrizS.append([])
        for j in range(k):
            matrizS[i].append([])
    
    
    for i in range(k):
        for j in range(k):
            if i == j:
                matrizS[i][j] =  [1,1,1]
                continue
            matrizS[i][j] = [0,0,0]

    matriz = np.array(matrizS)
    
    
    for i in range(x):
        for j in range(y):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[i-(k//2):i+(k//2)+1 , j-(k//2):j+(k//2)+1]


            mul = (1/k)*matriz*porcion
            b,g,r = calSuma(mul)
                   
            imagen.itemset((i,j,0),b)
            imagen.itemset((i,j,1),g)
            imagen.itemset((i,j,2),r)
    return imagen

def findEdges(imagen):

    y,x,d = imagen.shape
    copia = imagen.copy()

    matrizS = []
    for i in range(5):
        matrizS.append([])
        for j in range(5):
            matrizS[i].append([])
    
    
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 0:
                matrizS[i][j] =  [-1,-1,-1]
            elif i == 2 and j == 1:
                matrizS[i][j] =  [-1,-1,-1]
            elif i == 2 and j == 2: 
                matrizS[i][j] =  [4,4,4]
            elif i == 2 and j == 3:
                matrizS[i][j] =  [-1,-1,-1]
            elif i == 2 and j == 4:
                matrizS[i][j] =  [-1,-1,-1]
            else:
                matrizS[i][j] = [0,0,0]

   
   

    matriz = np.array(matrizS)
    

    for j in range(y):
        for i in range(x):
            if i-(5//2) < 0 or i+(5//2)+1>x:
                        continue   
            if j-(5//2) < 0 or j+(5//2)+1>y:
                        continue
            porcion = copia[j-(5//2):j+(5//2)+1,   i-(5//2):i+(5//2)+1 ]


            

            mul = matriz*porcion
            b,g,r = calSuma(mul)


            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = b+diferencia
                g = g+diferencia
                r = r+diferencia            

            if  maximo>255:
                diferencia = maximo -255
                b = b-diferencia
                g = g-diferencia
                r = r-diferencia

            


            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)

    return imagen

def sharppen(imagen, version):
    y,x,d = imagen.shape

    copia = imagen.copy()
    matrizS = []
    if version == 5:
        matrizS = [
            [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
            [[-1,-1,-1],[2,2,2],[2,2,2],[2,2,2],[-1,-1,-1]],
            [[-1,-1,-1],[2,2,2],[8,8,8],[2,2,2],[-1,-1,-1]],
            [[-1,-1,-1],[2,2,2],[2,2,2],[2,2,2],[-1,-1,-1]],
            [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        ]
    
    if version == 3:
        for i in range(3):
            matrizS.append([])
            for j in range(3):
                matrizS[i].append([])
        for i in range(3):
            for j in range(3):
                if i == 1 and j ==1:
                    matrizS[i][j] = [9,9,9]
                else:
                    matrizS[i][j] = [-1,-1,-1]        

    matriz = np.array(matrizS)

    k = 3 if version==3 else 5

    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]
            mul = (1/8)*matriz*porcion if version == 5 else  matriz*porcion
            
            b,g,r = calSuma(mul)

            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = b+diferencia
                g = g+diferencia
                r = r+diferencia

            if  maximo>255:
                diferencia = maximo -255
                b = b-diferencia
                g = g-diferencia
                r = r-diferencia

            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)
    return imagen


def emboos():
    pass

def promedio():
    pass

def mediana():
    pass

def mica(imagen,mica):
    b,g,r = mica
    y,x,d = imagen.shape

    for j in range(y):
        for i in range(x):
            imagen[j,i,0] = imagen[j,i,0] and b 
            imagen[j,i,1] = imagen[j,i,1] and g
            imagen[j,i,2] = imagen[j,i,2] and r 
    return imagen

filtro = motionBlur(imagen,9)

imagenNueva = cv2.imwrite('prueba.jpg',filtro)
