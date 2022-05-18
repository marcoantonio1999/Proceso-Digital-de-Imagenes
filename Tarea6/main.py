import cv2
import numpy as np
import math
from tkinter import *
from PIL import Image, ImageTk


def promedio(imgp):
    """
    Funcion para sacar el promedio de los griss dedo una porcion de una imagen
    """
    y,x = imgp.shape
    
    suma = 0
    for j in range(y):
        for i in range(x):
            suma += imgp[j,i]         
    prom = suma/(y*x)
    return prom 

def getImagen():
    """
    Funcion para crear una nueva pantalla y pedirle al usuario que introduzca el nombre del archivo a mostrar
    """
    top = Toplevel(ventana)
    top.geometry('300x200')
    labelCargar = Label(top, text="Introduce el nombre del archivo")
    labelCargar.place(x=10, y = 10 )
    entradaNombre = Entry(top)
    entradaNombre.place(x =50, y= 50 )
    botonAceptar = Button(top, text='Aceptar', command= lambda : [setImagen(entradaNombre.get()), top.destroy()])
    botonAceptar.place(x = 50, y= 100) 
    


def setImagen(nombreImg):
    """
    Funcion para poder configurar la imagen segun el nombre que se le asigno y poder verlo en pantalla
    """
    imgen = nombreImg+'.jpg'
    im = Image.open(imgen)
    ph = ImageTk.PhotoImage(im)
    labelImg = Label(ventana, image=ph)
    labelImg.image=ph
    labelImg.place(x=250,y=150)
    global imgG
    imgG = cv2.imread(imgen)
    
def recursivo():
    """
    Funcion para calcular el filtro recursivo

    """
    imagen = imgG.copy()

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
        
    
    for k in range(len(imagenesConcatX[0])):
        imgNuevo = cv2.vconcat(imagenesConcatX[k])
        cv2.imwrite("finalY{}.jpg".format(k+1), imgNuevo)
    
    
    listay = []
    for k in range(len(imagenesConcatX[0])):
        listay.append(cv2.imread( "finalY{}.jpg".format(k+1)))


    imgFinal = cv2.hconcat(listay)
    cv2.imwrite("Final.jpg", imgFinal)

    imgFinalRescalada = cv2.resize(imgFinal, (1000,1000))
    cv2.imwrite("FinalRescalada.jpg", imgFinalRescalada)


    im = Image.open("FinalRescalada.jpg")
    ph = ImageTk.PhotoImage(im)
    labelImg = Label(ventana, image=ph)
    labelImg.image=ph
    labelImg.place(x=250,y=150)

if __name__ == "__main__":

    ventana = Tk()
    ventana.geometry("1500x1500")
    getImagen()
    botonRecursivo = Button(ventana, text="Aplicar filtro", command= lambda: recursivo())
    botonRecursivo.place(x= 10, y=10)

    ventana.mainloop()