import numpy as np
import cv2


def calculaFrecuencia(img):
    valores = []
    y,x = img.shape
    
    for j in range(y):
        for i in range(x):
            valores.append(img[j,i])

    fdist=dict(zip(*np.unique(valores, return_counts=True)))            

    return list(fdist)[-1]





def acuarela(imagen,k):
    y,x = imagen.shape
    copia = imagen.copy()  
    
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[j-(k//2):j+(k//2)+1, i-(k//2):i+(k//2)+1 ]

            gris = calculaFrecuencia(porcion)
                   
            imagen[j,i] = gris
    return imagen


if __name__ == "__main__":
    imgO = cv2.imread("al1.jpg") 
    imgGrises = cv2.cvtColor(imgO, cv2.COLOR_BGR2GRAY)

    filtro = acuarela(imgGrises,7)
    cv2.imwrite("final.jpg", filtro)

