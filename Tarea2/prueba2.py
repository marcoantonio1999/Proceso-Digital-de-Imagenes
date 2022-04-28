from cgi import print_environ
from time import process_time
from tkinter import *
import cv2
import math
from PIL import Image, ImageTk
import copy
import numpy as np

imagen = cv2.imread("img1.jpg")


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
    print(imagen[-1:2, -1:2])
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
    print(matriz)
    
    for i in range(x):
        for j in range(y):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = imagen[i-(k//2):i+(k//2)+1 , j-(k//2):j+(k//2)+1]


            mul = matriz*porcion
            b,g,r = calSuma(mul)
                   
            imagen.itemset((i,j,0),b/k)
            imagen.itemset((i,j,1),g/k)
            imagen.itemset((i,j,2),r/k)
    return imagen





filtro = motionBlur(imagen, 9)

imagenNueva = cv2.imwrite('prueba.jpg',filtro)
