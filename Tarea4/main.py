import numpy as np
import cv2


def quiarMarca(imagen):
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
    imagen = input("introduce el nombre del la imagen a quitar el filtro\n")
    img = cv2.imread("{}.jpg".format(imagen))
    filtro = quiarMarca(img)
    cv2.imwrite('final.jpg',filtro)