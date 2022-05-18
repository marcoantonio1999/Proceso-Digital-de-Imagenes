import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk



def calculaFreciencias():
    """
    Calcula las frecuencias de toda la imagen, segun la formula lo que hace
    es equalizar la imagen dejando las frecuencias altas bajandolas y las frecuencias 
    bajas las sube
    """
    img = imagenGris.copy()
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

    cv2.imwrite("final.jpg", img)

    imgFinalRescalada = cv2.resize(img, (1000,1000))
    cv2.imwrite("FinalRescalada.jpg", imgFinalRescalada)
    labelImgO.destroy()
    im = Image.open("FinalRescalada.jpg")
    ph = ImageTk.PhotoImage(im)
    labelImg = Label(ventana, image=ph)
    labelImg.image=ph
    labelImg.place(x=250,y=50)

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
    global labelImgO
    labelImgO = Label(ventana, image=ph)
    labelImgO.image=ph
    labelImgO.place(x=250,y=150)
    global imagenGris
    imgG = cv2.imread(imgen)
    imagenGris = cv2.cvtColor(imgG, cv2.COLOR_BGR2GRAY)



if __name__== '__main__':
    ventana = Tk()
    ventana.geometry("1500x1500")
    getImagen()
    botonRecursivo = Button(ventana, text="Aplicar filtro", command= lambda: calculaFreciencias())
    botonRecursivo.place(x= 10, y=10)

    ventana.mainloop()
