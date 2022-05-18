from random import randint, random
import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk



def dilteringAleatorio():
    img = imagenGris.copy()
    y,x = img.shape

    for j in range(y):
        for i in range(x):
            numero = randint(0,255)
            if numero < img[j,i]:
                img[j,i] = 255
            else:
                img[j,i] = 0
    cv2.imwrite("final.jpg", img)

    imgFinalRescalada = cv2.resize(img, (1000,1000))
    cv2.imwrite("FinalRescalada.jpg", imgFinalRescalada)
    labelImgO.destroy()
    im = Image.open("FinalRescalada.jpg")
    ph = ImageTk.PhotoImage(im)
    labelImg = Label(ventana, image=ph)
    labelImg.image=ph
    labelImg.place(x=250,y=50)

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

    

def diltering( version):
    img = imagenGris.copy()
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




if __name__ == '__main__':
    ventana = Tk()
    ventana.geometry("1500x1500")
    getImagen()
    botonAleatorio = Button(ventana, text="Diltering Aleatorio", command= lambda: dilteringAleatorio())
    botonAleatorio.place(x= 10, y=10)
    botonOrdenado = Button(ventana, text="Diltering Ordenado", command= lambda: diltering("ordenado"))
    botonOrdenado.place(x= 10, y=60)
    botonDisperso = Button(ventana, text="Diltering Dipserso", command= lambda: diltering("disperso"))
    botonDisperso.place(x= 10, y=110)

    ventana.mainloop()
    
