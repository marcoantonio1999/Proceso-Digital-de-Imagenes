from curses.panel import bottom_panel
from tkinter import *
import cv2
import math
from PIL import Image, ImageTk
import copy
import numpy as  np
from numpy import matrix
import statistics
"""
Author: Marco Antonio Orduna Avila

Aplicacion para hacer fiiltros sencillos de la tarea 1

"""

def escalaGrises(imagen, version):
    """
    Funcion para calcular el filtro de una imagen a escala de grises la version
    depende a la formula que necesitemos
    """
    y,x,d = imagen.shape
    
    for i in range(y):
        
        for j in range(x):
            if version == 0:
                gris = math.floor((imagen.item(i, j, 0) + imagen.item(i, j, 1)+ imagen.item(i, j, 2))/3)
            if version == 1:
                gris = 0.11*(imagen.item(i, j, 0))  + 0.59*(imagen.item(i, j, 1))+ 0.3*(imagen.item(i, j, 2))
            if version == 2:
                gris = 0.0722*(imagen.item(i, j, 0))  + 0.7152*(imagen.item(i, j, 1))+ 0.2126*(imagen.item(i, j, 2))
            if version == 3:
                gris = 0.114*(imagen.item(i, j, 0))  + 0.587*(imagen.item(i, j, 1))+ 0.299*(imagen.item(i, j, 2))    
            if version == 4: 
                gris = math.floor((max(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)) + min(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)))/2)  
            if version == 5:
                gris = max(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2))
            if version == 6 :
                gris = min(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)) 

            imagen.itemset((i, j, 0), gris)
            imagen.itemset((i, j, 1), gris)
            imagen.itemset((i, j, 2), gris)   
    return imagen

def filtroDimensional(imagen, color):
    """
    filtro que se llama dimensional pues recordemos que la imagen la podemos ver como
    un vector de tres dimesiones en las cuales son el RGB
    """
    y,x,d = imagen.shape
    for i in range(1,y):
        for j in range(1,x):
            if color == 'rojo':
                imagen.itemset((i, j, 0), 0)
                imagen.itemset((i, j, 1), 0)
            if color == 'verde':
                imagen.itemset((i, j, 0), 0)
                imagen.itemset((i, j, 2), 0)

            if color == 'azul':
                imagen.itemset((i, j, 1), 0)
                imagen.itemset((i, j, 2), 0)
    return imagen

def promedio(lista, imagen):
    """
    Funcion para calcular el promedio de una lista de duplas de pixeles, esto para calcular el promedio de los
    colores del BGR de todos los pixeles
    """
    sumB = 0
    sumG = 0
    sumR = 0
    
    for i,j in lista:
            sumB = sumB + imagen.item(j,i,0)
            sumG = sumG + imagen.item(j,i,1)
            sumR = sumR + imagen.item(j,i,2)
    promB = sumB/len(lista)
    promG = sumG/len(lista)
    promR = sumR/len(lista)
    
    return promB,promG, promR


def mosaico(imagen, rangoX, rangoY):
    """
    Funcion para calcular el filtro de pixeleado en una imagen dependiendo de un rango x,y dado
    """

    x,y,d = imagen.shape
    
    anchoSeccion = math.ceil(x/rangoX)
    alturaSeccion = math.ceil(y/rangoY)
    matrizSecciones = []
    for i in range(anchoSeccion):
        matrizSecciones.append([])
        for j in range(alturaSeccion):
            matrizSecciones[i].append([])
    
    for i in range(x):
        for j in range(y):
            for k in range(anchoSeccion):
                for l in range(alturaSeccion):
                    if i//rangoX == k and j//rangoY == l:
                        matrizSecciones[k][l].append((j,i))    
    for i in range(anchoSeccion):
        for j in range(alturaSeccion):
            b,g,r = promedio(matrizSecciones[i][j], imagen)
            for h,k in matrizSecciones[i][j]:
                imagen.itemset((k,h,0), b)
                imagen.itemset((k,h,1), g)
                imagen.itemset((k,h,2), r)

    return imagen
        
def altoContraste(imagen, version):
    """
    Funcion para calcular el filtro de alto contraste, si el valor de un pixel es mayor o menor a 8 millones se ponen en
    negro o en blanco dependiendo de la version del filtro
    """
    x,y,d = imagen.shape
    for i in range(x):
        for j in range(y):
            b = imagen.item(i,j,0)
            g = imagen.item(i,j,1)
            r = imagen.item(i,j,2)
            #print(b*g*r)
            if version == 0:
                if b*g*r > 8000000:
                    imagen.itemset((i,j,0), 255)
                    imagen.itemset((i,j,1), 255)
                    imagen.itemset((i,j,2), 255)
                else:
                    imagen.itemset((i,j,0), 0)
                    imagen.itemset((i,j,1), 0)
                    imagen.itemset((i,j,2), 0)
            else :
                if b*g*r < 8000000:
                    imagen.itemset((i,j,0), 255)
                    imagen.itemset((i,j,1), 255)
                    imagen.itemset((i,j,2), 255)
                else:
                    imagen.itemset((i,j,0), 0)
                    imagen.itemset((i,j,1), 0)
                    imagen.itemset((i,j,2), 0)
    return imagen

def blur(imagen):
    x,y,d = imagen.shape
    
    for i in range(x):
        for j in range(y):
            b = imagen.item(i,j,0)
            g = imagen.item(i,j,1)
            r = imagen.item(i,j,2)

            if i == 0 and j == 0:
                blue = b *0.2 + imagen.item(0,1,0)*0.2 + imagen.item(1,0,0)*0.2
                green = g * 0.2 + imagen.item(0,1,1)*0.2 +imagen.item(1,0,1)*0.2
                red = r * 0.2 + imagen.item(0,1,2)*0.2 + imagen.item(1,0,2)*0.2

                imagen.itemset((0,0,0), blue)
                imagen.itemset((0,0,1), green)
                imagen.itemset((0,0,2), red)
                continue
            
            if i == x and j == 0:
                blue = b *0.2 + imagen.item(x-1,0,0)*0.2 + imagen.item(x,1,0)*0.2
                green = g * 0.2 + imagen.item(x-1,0,1)*0.2 +imagen.item(x,1,1)*0.2
                red = r * 0.2 + imagen.item(x-1,0,2)*0.2 + imagen.item(x,1,2)*0.2

                imagen.itemset((0,0,0), blue)
                imagen.itemset((0,0,1), green)
                imagen.itemset((0,0,2), red)
                continue
            if i == 0 and j == y:
                blue = b *0.2 + imagen.item(0,y-1,0)*0.2 + imagen.item(1,y,0)*0.2
                green = g * 0.2 + imagen.item(0,y-1,1)*0.2 +imagen.item(1,y,1)*0.2
                red = r * 0.2 + imagen.item(0,y-1,2)*0.2 + imagen.item(1,y,2)*0.2

                imagen.itemset((0,0,0), blue)
                imagen.itemset((0,0,1), green)
                imagen.itemset((0,0,2), red)
                continue
            if i == x and j == y:
                blue = b *0.2 + imagen.item(x,y-1,0)*0.2 + imagen.item(x-1,y,0)*0.2
                green = g * 0.2 + imagen.item(x,y-1,1)*0.2 +imagen.item(x-1,y,1)*0.2
                red = r * 0.2 + imagen.item(x,y-1,2)*0.2 + imagen.item(x-1,y,2)*0.2

                imagen.itemset((0,0,0), blue)
                imagen.itemset((0,0,1), green)
                imagen.itemset((0,0,2), red)
                continue
    return imagen

def brillo(imagen, constante):
    """
    Funcion para subir el brillo de una imagen
    """
    x,y,d = imagen.shape

    for i in range(x):
        for j in range(y):
            valorB = imagen.item(i,j,0)
            b = valorB + constante
            valorG = imagen.item(i,j,1)
            g = valorG + constante
            valorR = imagen.item(i,j,2)
            r = valorR + constante
            if b > 255:
                imagen.itemset((i,j,0),255)
            elif b < 0:
                imagen.itemset((i,j,0),0)
            else: 
                imagen.itemset((i,j,0),b)
            if g > 255:
                imagen.itemset((i,j,1),255)
            elif g < 0:
                imagen.itemset((i,j,1),0)
            else: 
                imagen.itemset((i,j,1),g)
            if r > 255:
                imagen.itemset((i,j,2),255)
            elif r < 0:
                imagen.itemset((i,j,2),0)
            else: 
                imagen.itemset((i,j,2),r)
    return imagen

def funcionGris(imagen,version):
    """
    Funcion para mostrar una nueva pantalla con el resultado del filtro gris
    """
    img = imagen.copy()
    filtro = escalaGrises(img, version)
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()
   
def filtroDim(imagen, color):
    """
    Funcion poara mostrar una nueva ventana con los resultados de los filtros de colores
    """

    img = imagen.copy()
    filtro = filtroDimensional(img, color)
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def mosaicoTop(imagen, entradaX, entradaY):
    """
    funcion para mostrar en una nueva pantalla el resultado de la imagen con el filtro del mosaico
    """
    img = imagen.copy()
    filtro = mosaico(img, int(entradaX), int(entradaY))
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def mosaicoF():
    """
    Funcion que nos muestra una nueva pantalla para poder introducir los valores para el filtro mosaico
    """

    top = Toplevel(ventana)
    top.geometry('400x200')
    labelx = Label(top, text='distancia de la seccion X')
    entradaX = Entry(top)
    labely = Label(top, text='distancia de la seccion Y')
    entradaY = Entry(top)
    labelx.place(x= 10,y=10)
    entradaX.place(x=200, y=10)
    labely.place(x= 10,y=60)
    entradaY.place(x =200, y= 60)
    botonAceptar = Button(top, text='Aceptar', command= lambda: mosaicoTop(imagen, entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )

def contrasteTop(imagen, version):
    """"
    Funcion para crear una nueva ventana para mostrar el resultado de contraste
    """
    img = imagen.copy()
    filtro = altoContraste(img, version)
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def brilloTop(imagen,constante):
    """
    Funcion para mostrar una nueva ventana con el resultado del filtro del brillo
    """
    img = imagen.copy()
    filtro = brillo(img, constante)
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()


def brilloFun():
    """
    Funcion para mostrar la pantalla con la opcion para modificar el brillo
    """
    top = Toplevel(ventana)
    top.geometry('400x200')
    scale = Scale(top, from_=-255, to=255, orient=HORIZONTAL)
    scale.place(x = 50, y = 20)
    botonAceptar = Button(top, text='Aceptar', command= lambda: brilloTop(imagen, int(scale.get()) ))
    botonAceptar.place(x = 100, y = 100 )


def micaTop(b,g,r):
    y,x,d = imagen.shape

    for j in range(y):
        for i in range(x):
            imagen[j,i,0] = imagen[j,i,0] and b 
            imagen[j,i,1] = imagen[j,i,1] and g
            imagen[j,i,2] = imagen[j,i,2] and r 
    return imagen

def micaFun():
    """
    Funcion para mostrar la pantalla con la opcion para modificar el brillo
    """
    top = Toplevel(ventana)
    top.geometry('400x200')
    scaleb = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    scaleb.place(x = 50, y = 20)

    scaleg = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    scaleg.place(x = 50, y = 20)

    scaler = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    scaler.place(x = 50, y = 20)

    botonAceptar = Button(top, text='Aceptar', command= lambda: micaTop(int(scaleb.get()), int(scaleg.get()),int(scaler.get())  ))
    botonAceptar.place(x = 100, y = 100 )


def calSuma(matriz):
    blue = 0
    green = 0
    red = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            blue = matriz[i][j][0] + blue
            green = matriz[i][j][1] + green
            red = matriz[i][j][2] + red
            
    return blue, green, red

def blur(imagen):
    x,y,d = imagen.shape
    copia = imagen.copy()

    matrizS = [
        [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]],
        [[0,0,0],[1,1,1],[1,1,1],[1,1,1],[0,0,0]],
        [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]],
        [[0,0,0],[1,1,1],[1,1,1],[1,1,1],[0,0,0]],
        [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]
    ]
    matriz = np.array(matrizS)
    
    for i in range(x):
        for j in range(y):
            if i-(5//2) < 0 or i+(5//2)+1>x:
                continue   
            if j-(5//2) < 0 or j+(5//2)+1>y:
                continue

            porcion = copia[i-(5//2):i+(5//2)+1 , j-(5//2):j+(5//2)+1]
            mul = (1/13)*matriz*porcion
            b,g,r = calSuma(mul)
                   
            imagen.itemset((i,j,0),b)
            imagen.itemset((i,j,1),g)
            imagen.itemset((i,j,2),r)
    return imagen


def blurTop():
    img = imagen.copy()
    print("cargando")
    filtro = blur(img)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()
    

def mediaFun():
    top = Toplevel(ventana)
    top.geometry('500x200')
    
    label = Label(top, text="Introduce la dimension de la matriz")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "3", command= lambda : [mediaTop(3), top.destroy()])
    boton3.place(x = 50, y= 60)
    boton5 = Button(top, text = "5", command= lambda : [mediaTop(5), top.destroy()])
    boton5.place(x = 100, y= 60)
    boton7 = Button(top, text = "7", command= lambda : [mediaTop(7), top.destroy()])
    boton7.place(x = 150, y= 60)
    boton9 = Button(top, text = "9", command= lambda : [mediaTop(9), top.destroy()])
    boton9.place(x = 200, y= 60)
    boton11 = Button(top, text = "11", command= lambda : [mediaTop(11), top.destroy()])
    boton11.place(x = 250, y= 60)


def mediaTop():
    img = imagen.copy()
    print("cargando")
    filtro = mediana(img)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def motionBlur(k):
    x,y,d = imagen.shape
    copia = imagen.copy()
    matrizS = []
    for i in range(k):
        matrizS.append([])
        for j in range(k):
            matrizS[i].append([])
    
    
    for i in range(k):
        for j in range(k):
            if i == j:
                matrizS[i][j] =  [1,1,1]
                continue
            matrizS[i][j] = [0,0,0]

    matriz = np.array(matrizS)
    
    
    for i in range(x):
        for j in range(y):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[i-(k//2):i+(k//2)+1 , j-(k//2):j+(k//2)+1]


            mul = (1/k)*matriz*porcion
            b,g,r = calSuma(mul)
                   
            imagen.itemset((i,j,0),b)
            imagen.itemset((i,j,1),g)
            imagen.itemset((i,j,2),r)
    return imagen


def motionTop(tamanio):
    img = imagen.copy()
    print("cargando")
    filtro = motionBlur(tamanio)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def motionFun():
    top = Toplevel(ventana)
    top.geometry('500x200')
    
    label = Label(top, text="Introduce la dimension de la matriz")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "3", command= lambda : [motionTop(3), top.destroy()])
    boton3.place(x = 50, y= 60)
    boton5 = Button(top, text = "5", command= lambda : [motionTop(5), top.destroy()])
    boton5.place(x = 100, y= 60)
    boton7 = Button(top, text = "7", command= lambda : [motionTop(7), top.destroy()])
    boton7.place(x = 150, y= 60)
    boton9 = Button(top, text = "9", command= lambda : [motionTop(9), top.destroy()])
    boton9.place(x = 200, y= 60)
    boton11 = Button(top, text = "11", command= lambda : [motionTop(11), top.destroy()])
    boton11.place(x = 250, y= 60)

def findEdges(version):
    y,x,d = imagen.shape
    copia = imagen.copy()

    matrizS = []

    if version == "v":
        for i in range(5):
            matrizS.append([])
            for j in range(5):
                matrizS[i].append([])
    
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 0:
                    matrizS[i][j] =  [-1,-1,-1]
                elif i == 2 and j == 1:
                    matrizS[i][j] =  [-1,-1,-1]
                elif i == 2 and j == 2: 
                    matrizS[i][j] =  [4,4,4]
                elif i == 2 and j == 3:
                    matrizS[i][j] =  [-1,-1,-1]
                elif i == 2 and j == 4:
                    matrizS[i][j] =  [-1,-1,-1]
                else:
                    matrizS[i][j] = [0,0,0]
    if version == "h":
        for i in range(5):
            matrizS.append([])
            for j in range(5):
                matrizS[i].append([])
    
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 0:
                    matrizS[i][j] =  [-1,-1,-1]
                elif i == 2 and j == 1:
                    matrizS[i][j] =  [-1,-1,-1]
                elif i == 2 and j == 2: 
                    matrizS[i][j] =  [2,2,2]
                else:
                    matrizS[i][j] = [0,0,0]
    if version==45:
        for i in range(5):
            matrizS.append([])
            for j in range(5):
                matrizS[i].append([])
    
        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                    matrizS[i][j] =  [-1,-1,-1]
                elif i == 1 and j == 1:
                    matrizS[i][j] =  [-2,-2,-2]
                elif i == 2 and j == 2: 
                    matrizS[i][j] =  [6,6,6]
                elif i == 2 and j == 3:
                    matrizS[i][j] =  [-2,-2,-2]
                elif i == 2 and j == 4:
                    matrizS[i][j] =  [-1,-1,-1]
                else:
                    matrizS[i][j] = [0,0,0]

    if version == "t":
        for i in range(3):
            matrizS.append([])
            for j in range(3):
                matrizS[i].append([])
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    matrizS[i][j] =  [8,8,8]
                else:
                    matrizS[i][j] = [-1,-1,-1]   
    
    matriz = np.array(matrizS)
    k = 3 if version == "t" else 5
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]
            mul = matriz*porcion
            b,g,r = calSuma(mul)
            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = b+diferencia
                g = g+diferencia
                r = r+diferencia            
            if  maximo>255:
                diferencia = maximo -255
                b = b-diferencia
                g = g-diferencia
                r = r-diferencia
            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)

    return imagen

def funTop(version):
    img = imagen.copy()
    print("cargando")
    filtro = findEdges(version)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def funFind():
    top = Toplevel(ventana)
    top.geometry('500x300')
    
    label = Label(top, text="Escoge el algoritmo de buscar aristas")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "vertical", command= lambda : [funTop("v"), top.destroy()])
    boton3.place(x = 10, y= 60)
    boton5 = Button(top, text = "horizontal", command= lambda : [funTop("h"), top.destroy()])
    boton5.place(x = 10, y= 110)
    boton7 = Button(top, text = "45 grados", command= lambda : [funTop(45), top.destroy()])
    boton7.place(x = 10, y= 160)
    boton9 = Button(top, text = "En todas las direcciones", command= lambda : [funTop("t"), top.destroy()])
    boton9.place(x = 10, y= 210)


def sharpen(version):
    y,x,d = imagen.shape

    copia = imagen.copy()
    matrizS = []
    if version == 5:
        matrizS = [
            [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],
            [[-1,-1,-1],[2,2,2],[2,2,2],[2,2,2],[-1,-1,-1]],
            [[-1,-1,-1],[2,2,2],[8,8,8],[2,2,2],[-1,-1,-1]],
            [[-1,-1,-1],[2,2,2],[2,2,2],[2,2,2],[-1,-1,-1]],
            [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        ]
    
    if version == 3:
        for i in range(3):
            matrizS.append([])
            for j in range(3):
                matrizS[i].append([])
        for i in range(3):
            for j in range(3):
                if i == 1 and j ==1:
                    matrizS[i][j] = [9,9,9]
                else:
                    matrizS[i][j] = [-1,-1,-1]        

    matriz = np.array(matrizS)

    k = 3 if version==3 else 5

    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]
            mul = (1/8)*matriz*porcion if version == 5 else  matriz*porcion
            
            b,g,r = calSuma(mul)

            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = b+diferencia
                g = g+diferencia
                r = r+diferencia

            if  maximo>255:
                diferencia = maximo -255
                b = b-diferencia
                g = g-diferencia
                r = r-diferencia

            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)
    return imagen

def sharpenTop(version):
    img = imagen.copy()
    print("cargando")
    filtro = sharpen(version)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def funSharpen():
    top = Toplevel(ventana)
    top.geometry('500x300')
    
    label = Label(top, text="Escoge el tamanio de la matriz")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "3", command= lambda : [sharpenTop(3), top.destroy()])
    boton3.place(x = 10, y= 60)
    boton5 = Button(top, text = "5", command= lambda : [sharpenTop(5), top.destroy()])
    boton5.place(x = 10, y= 110)


def promedio(k):
    y,x,d = imagen.shape
    copia = imagen.copy()
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]


            

            mul = (1/(k*k))*porcion
            b,g,r = calSuma(mul)


            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = b+diferencia
                g = g+diferencia
                r = r+diferencia            

            if  maximo>255:
                diferencia = maximo -255
                b = b-diferencia
                g = g-diferencia
                r = r-diferencia

            


            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)

    return imagen

def promedioTop(version):
    img = imagen.copy()
    print("cargando")
    filtro = mediana(version)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def promedioFun():
    top = Toplevel(ventana)
    top.geometry('500x200')
    
    label = Label(top, text="Introduce la dimension de la matriz")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "3", command= lambda : [medianaTop(3), top.destroy()])
    boton3.place(x = 50, y= 60)
    boton5 = Button(top, text = "5", command= lambda : [medianaTop(5), top.destroy()])
    boton5.place(x = 100, y= 60)
    boton7 = Button(top, text = "7", command= lambda : [medianaTop(7), top.destroy()])
    boton7.place(x = 150, y= 60)
    boton9 = Button(top, text = "9", command= lambda : [medianaTop(9), top.destroy()])
    boton9.place(x = 200, y= 60)
    boton11 = Button(top, text = "11", command= lambda : [medianaTop(11), top.destroy()])
    boton11.place(x = 250, y= 60)

def calMediana(matriz):
    blue = 0
    green = 0
    red = 0
    listaBlue = []
    listaGreen = []
    listared = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            listaBlue.append(matriz[i][j][0]) 
            listaGreen.append(matriz[i][j][1]) 
            listared.append(matriz[i][j][2]) 

    blue = statistics.median(listaBlue) 
    green = statistics.median(listaGreen)
    red = statistics.median(listared)   

    return blue, green, red

def mediana(k):
    y,x,d = imagen.shape
    copia = imagen.copy()
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = copia[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]


            

            mul = porcion
            b,g,r = calMediana(mul)


            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = b+diferencia
                g = g+diferencia
                r = r+diferencia            

            if  maximo>255:
                diferencia = maximo -255
                b = b-diferencia
                g = g-diferencia
                r = r-diferencia

            


            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)

    return imagen

def medianaTop(version):
    img = imagen.copy()
    print("cargando")
    filtro = mediana(version)
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()

def medianaFun():
    top = Toplevel(ventana)
    top.geometry('500x200')
    
    label = Label(top, text="Introduce la dimension de la matriz")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "3", command= lambda : [medianaTop(3), top.destroy()])
    boton3.place(x = 50, y= 60)
    boton5 = Button(top, text = "5", command= lambda : [medianaTop(5), top.destroy()])
    boton5.place(x = 100, y= 60)
    boton7 = Button(top, text = "7", command= lambda : [medianaTop(7), top.destroy()])
    boton7.place(x = 150, y= 60)
    boton9 = Button(top, text = "9", command= lambda : [medianaTop(9), top.destroy()])
    boton9.place(x = 200, y= 60)
    boton11 = Button(top, text = "11", command= lambda : [medianaTop(11), top.destroy()])
    boton11.place(x = 250, y= 60)



def emboss():
    y,x,d = imagen.shape

    copia = imagen.copy()
    
    
    matrizS = [
            [[-1,-1,-1],[-1,-1,-1],[0,0,0]],
            [[-1,-1,-1],[0,0,0],[1,1,1]],
            [[0,0,0],[1,1,1],[1,1,1]]
            ]
    
    

    matriz = np.array(matrizS)

   

    for j in range(y):
        for i in range(x):
            if i-(3//2) < 0 or i+(3//2)+1>x:
                        continue   
            if j-(3//2) < 0 or j+(3//2)+1>y:
                        continue
            porcion = copia[j-(3//2):j+(3//2)+1,   i-(3//2):i+(3//2)+1 ]
            mul = matriz*porcion 
            
            b,g,r = calSuma(mul)

            minimo = min(b,g,r)
            maximo = max(b,g,r)
            if  minimo<0:
                diferencia = -1 * minimo
                b = diferencia
                g = diferencia
                r = diferencia


                

            if  maximo>255:
                diferencia = maximo -255
                b = diferencia
                g = diferencia
                r = diferencia

            
            


            imagen.itemset((j,i,0),b)
            imagen.itemset((j,i,1),g)
            imagen.itemset((j,i,2),r)
    return imagen

def embossTop():
    img = imagen.copy()
    print("cargando")
    filtro = emboss()
    print("terminado")
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()


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
    global img1 
    img1 = ImageTk.PhotoImage(Image.open(imgen))
    labelImg.config(image=img1)
    global imagen
    imagen = cv2.imread(imgen)
    
    

if __name__ == '__main__':
    """
    El main de la aplicacion, aqui se muestran todos los botones que accionan las funcionallidades de la app
    """
    ventana = Tk()
    ventana.geometry('1600x1000')
    titulo = Label(ventana, text='Filtros basicos Tarea 1')
    titulo.place(x = 620, y = 10)

    getImagen()


    labelImg = Label(ventana, text='hola')
    labelImg.place(x=500, y = 50)

    filtrosGrises = ['Escala Grises 1.0', 'Escala Grises 2.0', 'Escala Grises 3.0', 'Escala Grises 4.0', 'Escala Grises 5.0',
    'Escala Grises 6.0', 'Escala Grises 7.0' ]
    botones = []
    rangoB = []

    for i in range(len(filtrosGrises)):
        rangoB.append(i)
        boton = Button(ventana, text=filtrosGrises[i], command= lambda i=i:  funcionGris(imagen,i))
        botones.append(boton)
    contador = 1

    for i in botones:  
        i.place(x = 10, y = 50 + 40*(contador))
        contador = contador +1 

    filtroColores = ['rojo', 'verde', 'azul']
    botonesColores = []

    for i in range(len(filtroColores)):
        boton = Button(ventana, text= filtroColores[i], command= lambda i=i : filtroDim(imagen,filtroColores[i]))
        botonesColores.append(boton)

    for i in botonesColores:
        i.place(x = 10, y = 50 + 40*(contador))
        contador = contador + 1

    botonMosaico = Button(ventana, text='Mosaico', command=lambda : mosaicoF())
    botonMosaico.place(x = 10, y = 50 + 40*(contador))
    contador = contador + 1
    botonContraste = ['Alto contraste', 'Inverso']
    versionContraste = [0,1]
    botonesContrastes = []

    

    for i in range(len(botonContraste)):
        boton = Button(ventana,text=botonContraste[i], command= lambda i=i: contrasteTop(imagen, versionContraste[i] ))
        botonesContrastes.append(boton)

    for i in botonesContrastes:
        i.place(x = 10, y = 50 + 40*(contador))
        contador = contador + 1
    botonBrillo = Button(ventana, text='Brillo', command= lambda: brilloFun())
    botonBrillo.place(x = 10, y = 50 + 40*(contador))
    contador += 1
    botonBlur = Button(ventana, text="Blur", command= lambda: blurTop() )
    botonBlur.place(x= 10, y = 50 + 40*(contador))
    contador += 1
    botonMotion = Button(ventana, text="Motion Blur", command= lambda: motionFun() )
    botonMotion.place(x= 10, y = 50 + 40*(contador))
    contador += 1
    botonFind = Button(ventana, text = "Find Edges", command= lambda: funFind())
    botonFind.place(x=10, y= 50 + 40*contador  )
    contador += 1
    
    botonSharpen = Button(ventana, text="Sharpen", command= lambda: funSharpen())
    botonSharpen.place(x = 10, y = 50 + 40*contador )

    contador += 1
    botonEmboss = Button(ventana, text="Emboss", command=lambda: embossTop())
    botonEmboss.place(x = 10, y = 50 + 40*contador)


    contador += 1
    botonPromedio = Button(ventana , text="Promedio", command= lambda: promedioFun())
    botonPromedio.place(x = 10, y = 50 + 40*contador)

    contador += 1
    botonMedianan = Button(ventana, text="mediana", command=lambda: medianaFun())
    botonMedianan.place(x = 10, y = 50 + 40*contador)

    contador += 1
    botonMica = Button(ventana, text="mica", command=lambda: micaFun())
    botonMica.place(x = 10, y = 50 + 40*contador)

    ventana.mainloop()

