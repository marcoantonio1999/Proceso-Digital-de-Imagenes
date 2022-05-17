import cv2
import numpy as np
import math

def promedio(img):
    y,x = img.shape
    
    suma = 0
    for j in range(y):
        for i in range(x):
            suma += img[j,i]         
    prom = suma/(y*x)
    return prom 

if __name__ == "__main__":
    imagen = cv2.imread("caja.jpg")
    x,y,d = imagen.shape
    w = int(x/4)
    h = int(y/4)
    imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagenRescalada = cv2.resize( imagen ,(w, h) ) 
    imagenRescaladaGrises = cv2.cvtColor(imagenRescalada, cv2.COLOR_BGR2GRAY)

    for k in range(15):
        img = imagenRescaladaGrises.copy()
        for j in range(h):
            for i in range(w):
                gris = img[j,i] + 9*(k+1)
                
                if gris > 255:
                    gris = 255
                img[j,i] = gris
        cv2.imwrite('final{}.jpg'.format(15-k),img )


    for k in range(15):
        img = imagenRescaladaGrises.copy()
        for j in range(h):
            for i in range(w):
                gris = img[j,i] - 8*(k+1)
                
                if gris < 0:
                    gris = 0
                img[j,i] = gris

                img[j,i] = gris

        cv2.imwrite('final{}.jpg'.format((k+1)+15),img ) 

    x,y,d = imagen.shape
    
    rangoX = 70
    rangoY = 70


    anchoSeccion = math.ceil(x/rangoX)
    alturaSeccion = math.ceil(y/rangoY)
    
    
    imagenesConcatX= []
    for i in range(rangoX):
        imagenesConcat = []

        for j in range(rangoY):
            if (j+1)*alturaSeccion > y:
                break
            if (i+1)*anchoSeccion >x:
                break
            
            imgP = imagenGris[j*alturaSeccion : (j+1)*alturaSeccion,i*anchoSeccion:(i+1)*anchoSeccion]
            yd, xd = imgP.shape
            if yd == 0 or xd == 0:
                continue
            prom =255-promedio(imgP)
            numImagen = 0
            
            for k in range(30):
                if prom >= 240:
                    numImagen = 30
                    break
                if k*8 <= prom <= (k+1)*8:
                    numImagen = k+1
            
            imagenC = cv2.imread("final{}.jpg".format(int(numImagen)) )   
             
            imagenesConcat.append(imagenC)
        
        imagenesConcatX.append(imagenesConcat)
        
    

    
    print(len(imagenesConcatX))
    print(len(imagenesConcatX[0]))
    
    for k in range(len(imagenesConcatX[0])):
        imgNuevo = cv2.vconcat(imagenesConcatX[k])
        cv2.imwrite("finalY{}.jpg".format(k+1), imgNuevo)
    
    
    listay = []
    for k in range(len(imagenesConcatX[0])):
        listay.append(cv2.imread( "finalY{}.jpg".format(k+1)))


    imgFinal = cv2.hconcat(listay)
    cv2.imwrite("Final.jpg", imgFinal)
    