from base64 import encode
from struct import unpack
import cv2
from numpy import packbits, unpackbits
import numpy as np




def codificar(pixel, lista):
    bBinario = format((pixel[0]), '08b')
    gBinario = format((pixel[1]), '08b')
    rBinario = format((pixel[2]), '08b')
    
    newBbinario = int((bBinario[:-1] + lista[0]),2)
    newGbinario = int((gBinario[:-1] + lista[1]),2)
    newRbinario = int((rBinario[:-1] + lista[2]),2)

    return [newBbinario, newGbinario, newRbinario]
    



if __name__ == "__main__":
    img= cv2.imread("imgO.bmp")
    
    imgO = img.copy()

    imgG = cv2.imread("img.bmp")
    
    y,x,d = imgG.shape
    
    ancho = 210
    altura = 210

    anchoBit = format(ancho, "015b")
    alturaBit = format(altura, "015b")

    listaBitsImg = []
    for k in anchoBit:
        listaBitsImg.append(k)
    for k in alturaBit:
        listaBitsImg.append(k)


    for j in range(y):
        for i in range(x):
            for k in format(imgG[j,i,0],'08b'):
                listaBitsImg.append(k)
            for k in format(imgG[j,i,1],'08b'):
                listaBitsImg.append(k)
            for k in format(imgG[j,i,2],'08b'):
                listaBitsImg.append(k)
        

    y,x,d = imgO.shape
    for j in range(y):
        for i in range(x):
            if len(listaBitsImg) < 3:
                break
            nuevoPixel = codificar( imgO[j,i], listaBitsImg[:3])
            del listaBitsImg[:3]
            imgO[j,i] = nuevoPixel

    """
    texto = "hola mundo| asdfdsaf asdfsdf sdf sdaf sdaf sadfsdaf sdaf sdaf sadf s"
    textoAscci = []
    for i in texto:
        textoAscci.append(ord(i))
    
    textoBits = []
    for i in textoAscci:
        for j in '{0:08b}'.format(i):
            textoBits.append(j)

    y,x,d = img.shape
    for j in range(y):
        for i in range(x):
            if len(textoBits)==0:
                break

            if len(textoBits) <3:
                break
            print(textoBits[:3])
            nuevoPixel = codificar( img[j,i], textoBits[:3])
            del textoBits[:3]
            img[j,i] = nuevoPixel
    
    a = format(1,'08b')
    print(a)

    b = int(a)
    print(b)
    
    """



    
    cv2.imwrite("final.bmp", imgO)
    

    #print(chr(int(i,2)))






       