from random import randint, random
import numpy as np
import cv2

def dilteringAleatorio(img):
    y,x = img.shape

    for j in range(y):
        for i in range(x):
            numero = randint(0,255)
            if numero < img[j,i]:
                img[j,i] = 255
            else:
                img[j,i] = 0
    return img

def aplicaMatriz(porcion,version):

    

    if version == 1:
        if porcion[0,0]/28 > 8:
            porcion[0,0] = 255
        else:
            porcion[0,0] = 0

        if porcion[0,1]/28 > 3:
            porcion[0,1] = 255
        else:
            porcion[0,1] = 0

        if porcion[0,2]/28 > 4:
            porcion[0,2] = 255
        else:
            porcion[0,2] = 0


        if porcion[1,0]/28 > 6:
            porcion[1,0] = 255
        else:
            porcion[1,0] = 0
        
        if porcion[1,1]/28 > 1:
            porcion[1,1] = 255
        else:
            porcion[1,1] = 0


        if porcion[1,2]/28 > 2:
            porcion[1,2] = 255
        else:
            porcion[1,2] = 0

        if porcion[2,0]/28 > 7:
            porcion[2,0] = 255
        else:
            porcion[2,0] = 0

        if porcion[2,1]/28 > 5:
            porcion[2,1] = 255
        else:
            porcion[2,1] = 0

        if porcion[2,2]/28 > 9:
            porcion[2,2] = 255
        else:
            porcion[2,2] = 0
    if version == 2:
        if porcion[0,0]/28 > 1:
            porcion[0,0] = 255
        else:
            porcion[0,0] = 0

        if porcion[0,1]/28 > 7:
            porcion[0,1] = 255
        else:
            porcion[0,1] = 0

        if porcion[0,2]/28 > 4:
            porcion[0,2] = 255
        else:
            porcion[0,2] = 0


        if porcion[1,0]/28 > 5:
            porcion[1,0] = 255
        else:
            porcion[1,0] = 0
        
        if porcion[1,1]/28 > 8:
            porcion[1,1] = 255
        else:
            porcion[1,1] = 0


        if porcion[1,2]/28 > 3:
            porcion[1,2] = 255
        else:
            porcion[1,2] = 0

        if porcion[2,0]/28 > 6:
            porcion[2,0] = 255
        else:
            porcion[2,0] = 0

        if porcion[2,1]/28 > 2:
            porcion[2,1] = 255
        else:
            porcion[2,1] = 0

        if porcion[2,2]/28 > 9:
            porcion[2,2] = 255
        else:
            porcion[2,2] = 0

    return porcion

    

def diltering(img, version):
    y,x = img.shape

    for j in range(y):
        for i in range(x):
            if (j+1)*3 > y or (i+1)*3>x:
                break


            pedazo = img[j*3:(j+1)*3, i*3: (i+1)*3 ]
            if version == 'ordenado':
                nuevoPedazo = aplicaMatriz(pedazo,1)
            if version == 'disperso':
                nuevoPedazo = aplicaMatriz(pedazo,2)
            img[j*3:(j+1)*3, i*3: (i+1)*3] = nuevoPedazo
    return img





if __name__ == '__main__':
    imgO = cv2.imread("al1.jpg")
    imgGrises = cv2.cvtColor(imgO, cv2.COLOR_BGR2GRAY)
    filtro = diltering(imgGrises,'disperso')
    cv2.imwrite("final.jpg", filtro)
    
