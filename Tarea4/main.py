from email.mime import image
import numpy as np
import cv2

def blending(img1, img2, porcentaje):
    y1,x1,d1 = img1.shape
    y2,x2,d2 = img2.shape

    print(x1,y1)
    print(x2,y2)


    for j in range(y1):
        for i in range(x1):
            b = (img1[j,i,0]*porcentaje) + ((img2[j,i,0])*(1-porcentaje))
            g = (img1[j,i,1]*porcentaje) + ((img2[j,i,1])*(1-porcentaje))
            r = (img1[j,i,2]*porcentaje) + ((img2[j,i,2])*(1-porcentaje))

            img1[j,i] = [b,g,r]

    return img1

def quiarMarca(imagen, porcentaje):
    y,x,d = imagen.shape
    
    for j in range(y):
        for i in range(x):
            bl =  int(imagen[j,i,0])
            gr = int(imagen[j,i,1])
            re = int(imagen[j,i,2])
            lista = [bl,gr,re]
            lista.sort()
            resta = lista[0] - lista[1]
            resta2 = lista[1]- lista[2]
            if abs(resta) + abs(resta2) < 10:
                continue
            
            
            valor = int(imagen[j,i,0]) * int(imagen[j,i,1]) * int(imagen[j,i,2])

            if valor > 7000000:
                
                imagen.itemset((j,i,0),250)
                imagen.itemset((j,i,1),250)
                imagen.itemset((j,i,2),250)
                
                continue
            if 6000000 < valor < 7000000:
                
                imagen.itemset((j,i,0),245)
                imagen.itemset((j,i,1),245)
                imagen.itemset((j,i,2),245)
                
                continue

            if 5000000 < valor < 6000000:
                
                imagen.itemset((j,i,0),225)
                imagen.itemset((j,i,1),225)
                imagen.itemset((j,i,2),225)
                continue

            if 4000000 < valor < 5000000:
                
                imagen.itemset((j,i,0),205)
                imagen.itemset((j,i,1),205)
                imagen.itemset((j,i,2),205)
                continue
            if 3000000 <valor <4000000:
                imagen.itemset((j,i,0),185)
                imagen.itemset((j,i,1),185)
                imagen.itemset((j,i,2),185)
                continue
            if 2000000 <valor <3000000:
                imagen.itemset((j,i,0),165)
                imagen.itemset((j,i,1),165)
                imagen.itemset((j,i,2),165)
                continue
            if 1000000 <valor <2000000:
                imagen.itemset((j,i,0),145)
                imagen.itemset((j,i,1),145)
                imagen.itemset((j,i,2),145)
                continue
            if 500000 <valor <1000000:
                imagen.itemset((j,i,0),125)
                imagen.itemset((j,i,1),125)
                imagen.itemset((j,i,2),125)
                continue
            if 250000 <valor <500000:
                imagen.itemset((j,i,0),105)
                imagen.itemset((j,i,1),105)
                imagen.itemset((j,i,2),105)
                continue
            if 0 <valor <250000:
                imagen.itemset((j,i,0),85)
                imagen.itemset((j,i,1),85)
                imagen.itemset((j,i,2),85)
                continue

    return imagen


if __name__ == "__main__":
    #img1 = cv2.imread("r1.jpg")
    #img2 = cv2.imread("imgr.jpg")

    img = cv2.imread("r2.jpg")

    filtro = quiarMarca(img,0.6)

    
    #filtro =  blending(img1, img2, 0.375)
    cv2.imwrite('final.jpg',filtro)