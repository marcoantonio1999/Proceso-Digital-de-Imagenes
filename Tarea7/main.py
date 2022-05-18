import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk

def calculaFrecuencia(img):
    """
    nos calcula las frecuencias de los pixeles de una porcion de la imagen y esa
    frecuencia es la que se cambia por el punto de interes
    """
    valores = []
    y,x = img.shape
    
    for j in range(y):
        for i in range(x):
            valores.append(img[j,i])

    fdist=dict(zip(*np.unique(valores, return_counts=True)))            
    return list(fdist)[-1]


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



def acuarela(k):
    """
    Funcion pora calcular el filtro de acuarela dada una matriz de tamanio k, el
    tamanio es 5 por defecto ya que no se ve un cambio significativo
    
    """
    y,x = imagenGris.shape
    copia = imagenGris.copy()  
    
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = imagenGris[j-(k//2):j+(k//2)+1, i-(k//2):i+(k//2)+1 ]

            gris = calculaFrecuencia(porcion)
                   
            copia[j,i] = gris

    cv2.imwrite("final.jpg", copia)

    imgFinalRescalada = cv2.resize(copia, (1000,1000))
    cv2.imwrite("FinalRescalada.jpg", imgFinalRescalada)
    labelImgO.destroy()
    im = Image.open("FinalRescalada.jpg")
    ph = ImageTk.PhotoImage(im)
    labelImg = Label(ventana, image=ph)
    labelImg.image=ph
    labelImg.place(x=250,y=150)
    



if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry("1500x1500")
    getImagen()
    botonRecursivo = Button(ventana, text="Aplicar filtro", command= lambda: acuarela(5))
    botonRecursivo.place(x= 10, y=10)

    ventana.mainloop()

