import cv2
import numpy as np





def calculaFreciencias(img):
    y,x = img.shape

    listaFreciencias = []
    for i in range(256):
        listaFreciencias.append(0)


    for k in range(256):
        for j in range(y):
            for i in range(x):
                if img[j,i] == k:
                    listaFreciencias[k] += 1


    lf = listaFreciencias.copy()
    cdf = []
    
    cdf.append(listaFreciencias.pop(0))
    for i in range(255):
        cdf.append(cdf[-1] + listaFreciencias.pop(0))


    for j in range(y):
        for i in range(x):
            img[j,i] = abs(((cdf[img[j,i]]-1)/ cdf[-1]) *255  )

    return img



if __name__== '__main__':
    imgO = cv2.imread("img.jpg")
    imgGrises = cv2.cvtColor(imgO, cv2.COLOR_BGR2GRAY)
    filtro = calculaFreciencias(imgGrises)
    cv2.imwrite("final.jpg", filtro)