
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

Aplicacion para hacer filtros de la tarea2

"""

def escalaGrises(version):
    """
    Funcion para calcular el filtro de una imagen a escala de grises la version
    depende a la formula que necesitemos
    """
    y,x,d = imagen.shape
    copia = imagen.copy()
    print(version)
    for i in range(y):
        
        for j in range(x):
            if version == 0:
                gris = math.floor((imagen.item(i, j, 0) + imagen.item(i, j, 1)+ imagen.item(i, j, 2))/3)
            elif version == 1:
                gris = 0.11*(imagen.item(i, j, 0))  + 0.59*(imagen.item(i, j, 1))+ 0.3*(imagen.item(i, j, 2))
            elif version == 2:
                gris = 0.0722*(imagen.item(i, j, 0))  + 0.7152*(imagen.item(i, j, 1))+ 0.2126*(imagen.item(i, j, 2))
            elif version == 3:
                gris = 0.114*(imagen.item(i, j, 0))  + 0.587*(imagen.item(i, j, 1))+ 0.299*(imagen.item(i, j, 2))    
            elif version == 4: 
                gris = math.floor((max(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)) + min(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)))/2)  
            elif version == 5:
                gris = max(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2))
            elif version == 6 :
                gris = min(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)) 
            else:
                print("error")
                break

            copia.itemset((i, j, 0), gris)
            copia.itemset((i, j, 1), gris)
            copia.itemset((i, j, 2), gris)   
    return copia

def filtroDimensional(color):
    """
    filtro que se llama dimensional pues recordemos que la imagen la podemos ver como
    un vector de tres dimesiones en las cuales son el RGB
    """
    y,x,d = imagen.shape
    copia = imagen.copy()
    for i in range(1,y):
        for j in range(1,x):
            if color == 'rojo':
                copia.itemset((i, j, 0), 0)
                copia.itemset((i, j, 1), 0)
            if color == 'verde':
                copia.itemset((i, j, 0), 0)
                copia.itemset((i, j, 2), 0)

            if color == 'azul':
                copia.itemset((i, j, 1), 0)
                copia.itemset((i, j, 2), 0)
    return copia

def promedioM(lista):
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


def mosaico(rangoX, rangoY):
    """
    Funcion para calcular el filtro de pixeleado en una imagen dependiendo de un rango x,y dado
    """
    copia = imagen.copy()

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
            b,g,r = promedioM(matrizSecciones[i][j])
            for h,k in matrizSecciones[i][j]:
                copia.itemset((k,h,0), b)
                copia.itemset((k,h,1), g)
                copia.itemset((k,h,2), r)

    return copia
        
def altoContraste(version):
    """
    Funcion para calcular el filtro de alto contraste, si el valor de un pixel es mayor o menor a 8 millones se ponen en
    negro o en blanco dependiendo de la version del filtro
    """
    copia = imagen.copy()
    y,x,d = imagen.shape
    for j in range(y):
        for i in range(x):
            b = imagen.item(j,i,0)
            g = imagen.item(j,i,1)
            r = imagen.item(j,i,2)
            #print(b*g*r)
            if version == "Alto Contraste":
                if b*g*r > 8290000:
                    copia.itemset((j,i,0), 255)
                    copia.itemset((j,i,1), 255)
                    copia.itemset((j,i,2), 255)
                else:
                    copia.itemset((j,i,0), 0)
                    copia.itemset((j,i,1), 0)
                    copia.itemset((j,i,2), 0)
            else :
                if b*g*r < 8290000:
                    copia.itemset((j,i,0), 255)
                    copia.itemset((j,i,1), 255)
                    copia.itemset((j,i,2), 255)
                else:
                    copia.itemset((j,i,0), 0)
                    copia.itemset((j,i,1), 0)
                    copia.itemset((j,i,2), 0)
    return copia

def brillo(constante):
    """
    Funcion para subir el brillo de una imagen
    """
    x,y,d = imagen.shape
    copia = imagen.copy()
    for i in range(x):
        for j in range(y):
            valorB = imagen.item(i,j,0)
            b = valorB + constante
            valorG = imagen.item(i,j,1)
            g = valorG + constante
            valorR = imagen.item(i,j,2)
            r = valorR + constante
            if b > 255:
                copia.itemset((i,j,0),255)
            elif b < 0:
                copia.itemset((i,j,0),0)
            else: 
                copia.itemset((i,j,0),b)
            if g > 255:
                copia.itemset((i,j,1),255)
            elif g < 0:
                copia.itemset((i,j,1),0)
            else: 
                copia.itemset((i,j,1),g)
            if r > 255:
                copia.itemset((i,j,2),255)
            elif r < 0:
                copia.itemset((i,j,2),0)
            else: 
                copia.itemset((i,j,2),r)
    return copia

def funcionGris(version):
    """
    Funcion para mostrar una nueva pantalla con el resultado del filtro gris
    """
    filtro = escalaGrises(version)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()
   
def filtroDim(color):
    """
    Funcion poara mostrar una nueva ventana con los resultados de los filtros de colores
    """

    filtro = filtroDimensional(color)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

def mosaicoTop(entradaX, entradaY):
    """
    funcion para mostrar en una nueva pantalla el resultado de la imagen con el filtro del mosaico
    """
    
    filtro = mosaico(int(entradaX), int(entradaY))
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

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
    botonAceptar = Button(top, text='Aceptar', command= lambda: mosaicoTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )

def contrasteTop(version):
    """"
    Funcion para crear una nueva ventana para mostrar el resultado de contraste
    """
    filtro = altoContraste(version)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

def brilloTop(constante):
    """
    Funcion para mostrar una nueva ventana con el resultado del filtro del brillo
    """
    filtro = brillo(constante)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()


def brilloFun():
    """
    Funcion para mostrar la pantalla con la opcion para modificar el brillo
    """
    top = Toplevel(ventana)
    top.geometry('400x200')
    scale = Scale(top, from_=-255, to=255, orient=HORIZONTAL)
    scale.place(x = 50, y = 20)
    botonAceptar = Button(top, text='Aceptar', command= lambda: brilloTop(int(scale.get()) ))
    botonAceptar.place(x = 100, y = 100 )


def mica(b,g,r):
    """
    Funcion para hacer el filtro de la mica dependiendo de los valores RGB
    """

    y,x,d = imagen.shape
    copia = imagen.copy()
    for j in range(y):
        for i in range(x):
            copia[j,i,0] = int((hex(imagen[j,i,0]) and hex(b)),16)
            copia[j,i,1] = int((hex(imagen[j,i,1]) and hex(g)),16)
            copia[j,i,2] = int((hex(imagen[j,i,2]) and hex(r)),16) 
    return copia

def micaTop(b,g,r):
    """
    Funcion para guardar el filtro de la mica y sacar la ventana emergente para poder meter los datos
    """
    filtro = mica(b,g,r)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()


def micaFun():
    """
    Funcion para mostrar la pantalla con la opcion para modificar los datos de la mica
    """
    top = Toplevel(ventana)
    top.geometry('400x800')


    

    labelB = Label(top,text="Componente Azul")
    labelB.place(x=50, y=20)
    scaleb = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    scaleb.place(x = 50, y = 50)

    labelG = Label(top,text="Componente Verde")
    labelG.place(x=50, y=110)
    scaleg = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    scaleg.place(x = 50, y = 140)

    labelR = Label(top,text="Componente Rojo")
    labelR.place(x=50, y=200)
    scaler = Scale(top, from_=0, to=255, orient=HORIZONTAL)
    scaler.place(x = 50, y = 240)

    botonAceptar = Button(top, text='Aceptar', command= lambda: micaTop(int(scaleb.get()), int(scaleg.get()),int(scaler.get())  ))
    botonAceptar.place(x = 100, y = 290 )


def calSuma(matriz):
    """
    Funcion para sumar los valores rgb dada una matriz de pixeles
    """
    blue = 0
    green = 0
    red = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            blue = matriz[i][j][0] + blue
            green = matriz[i][j][1] + green
            red = matriz[i][j][2] + red
            
    return blue, green, red

def blur():
    """
    Funcion para calcular el filtro de Blur
    """
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

            porcion = imagen[i-(5//2):i+(5//2)+1 , j-(5//2):j+(5//2)+1]
            mul = (1/13)*matriz*porcion
            b,g,r = calSuma(mul)
                   
            copia.itemset((i,j,0),b)
            copia.itemset((i,j,1),g)
            copia.itemset((i,j,2),r)
    return copia


def blurTop():
    """
    Funcion para guardar y mostrar el resulado del filtro
    """
    filtro = blur()
    cv2.imwrite('final.jpg',filtro)
    abreResultante()
    

def mediaFun():
    """
    Funcion para mostrar las opcion de la matriz que se quiere en el filtro de la media
    """

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
    """
    Funcion para aplicar el filtro de la media y mostrarlo
    """
    filtro = mediana()
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

def motionBlur(k):
    """
    Funcion para aplicar el filtro de motion blur dado el tamanio de la matriz k
    """
    x,y,d = imagen.shape
    copia = imagen.copy()
    resultante = imagen.copy()

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
                   
            resultante.itemset((i,j,0),b)
            resultante.itemset((i,j,1),g)
            resultante.itemset((i,j,2),r)
    return resultante


def motionTop(tamanio):
    """
    Funcion para guardar y mostrar el filtro de motion blur
    """
    filtro = motionBlur(tamanio)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

def motionFun():
    """
    Funcion para mostrar las opcion del filtro de motion blur
    """
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
    """
    Funcion para calcular el filtro de buscar las aristas dada la version si es el de vertical, horizontal,
    noventa grados o en todas las direcciones.
    """

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
            porcion = imagen[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]
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
            copia.itemset((j,i,0),b)
            copia.itemset((j,i,1),g)
            copia.itemset((j,i,2),r)

    return copia

def funTop(version):
    """
    Funcion para guardar y mostrar el litro de encontrar aristas
    """
    filtro = findEdges(version)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()
    
def abreResultante():
    """
    Funcion para mostrar el resultado de aplicar alguno de los filtros
    """

    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()


def funFind():
    """
    Funcion para mostrar las opciones para el filtro de buscar aristas
    """
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
    """
    Funcion para calcular el filtro sharpen
    """
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
            porcion = imagen[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]
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

            copia.itemset((j,i,0),b)
            copia.itemset((j,i,1),g)
            copia.itemset((j,i,2),r)
    return copia

def sharpenTop(version):
    """
    Funcion para guardar el archivo de sharpen 
    """
    filtro = sharpen(version)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

def funSharpen():
    """
    Funcion para mostrar las opciones del filtro sharpen
    """
    top = Toplevel(ventana)
    top.geometry('500x300')
    
    label = Label(top, text="Escoge el tamanio de la matriz")
    label.place(x = 10, y= 10)
    boton3 = Button(top, text = "3", command= lambda : [sharpenTop(3), top.destroy()])
    boton3.place(x = 10, y= 60)
    boton5 = Button(top, text = "5", command= lambda : [sharpenTop(5), top.destroy()])
    boton5.place(x = 10, y= 110)


def promedio(k):
    """
    Funcion para calcular el filtro promedio
    """
    y,x,d = imagen.shape
    copia = imagen.copy()
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = imagen[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]

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

            copia.itemset((j,i,0),b)
            copia.itemset((j,i,1),g)
            copia.itemset((j,i,2),r)

    return copia

def promedioTop(version):
    """
    Funcion para guardar el resultado del filtro promedio
    """
    filtro = mediana(version)
    cv2.imwrite('final.jpg',filtro)
    abreResultante

def promedioFun():
    """
    Funcion para mostrar las opciones para calcular el filtro promedio
    """
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
    """
    Funcion para calcular la mediana dada una matriz
    """
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
    """
    Funcion para calcular el filtro de la mediana
    """
    y,x,d = imagen.shape
    copia = imagen.copy()
    for j in range(y):
        for i in range(x):
            if i-(k//2) < 0 or i+(k//2)+1>x:
                        continue   
            if j-(k//2) < 0 or j+(k//2)+1>y:
                        continue
            porcion = imagen[j-(k//2):j+(k//2)+1,   i-(k//2):i+(k//2)+1 ]

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

            


            copia.itemset((j,i,0),b)
            copia.itemset((j,i,1),g)
            copia.itemset((j,i,2),r)

    return copia

def medianaTop(version):
    """
    Funcion para guardar el filtro mediana
    """
    filtro = mediana(version)
    cv2.imwrite('final.jpg',filtro)
    abreResultante()

def medianaFun():
    """
    Funcion para mostrar las opciones del filtro mediana
    """
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
    """
    Funcion para calcular el filtro emboss
    """
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
            porcion = imagen[j-(3//2):j+(3//2)+1,   i-(3//2):i+(3//2)+1 ]
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

            copia.itemset((j,i,0),b)
            copia.itemset((j,i,1),g)
            copia.itemset((j,i,2),r)
    return copia

def embossTop():
    """
    Funcion para guardar el filtro de emboss
    """
    filtro = emboss()
    cv2.imwrite('final.jpg',filtro)
    abreResultante()


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

    nombreBotones = ['Escala Grises 1.0', 'Escala Grises 2.0', 'Escala Grises 3.0', 'Escala Grises 4.0', 'Escala Grises 5.0',
    'Escala Grises 6.0', 'Escala Grises 7.0','rojo', 'verde', 'azul', 'Mosaico', 'Alto Contraste',
    'Inverso',"Brillo", "Blur", "Motion Blur", "Find Edges", "Sharpen", "Emboss", "Promedio", "Mediana" ,"Mica"
    ]


    funciones = [funcionGris, filtroDim, mosaicoF,contrasteTop, brilloFun, blurTop,motionFun, funFind, funSharpen, 
    embossTop, promedioFun, medianaFun, micaFun
    ]

    botones = []


    for i in range(len(nombreBotones)):
        
        if 0<=i<= 6:
            boton = Button(ventana, text=nombreBotones[i], command= lambda i=i: funciones[0](i))
        elif 7<=i<=9:
            boton = Button(ventana, text=nombreBotones[i], command= lambda i=i: funciones[1](nombreBotones[i]))
        elif i == 10:
            boton = Button(ventana, text=nombreBotones[i], command= lambda: funciones[2]())
        elif 11<=i<=12:
            boton = Button(ventana, text=nombreBotones[i], command= lambda i=i: funciones[3](nombreBotones[i])) 
        else:
            boton = Button(ventana, text=nombreBotones[i], command= lambda i=i: funciones[i-9]()) 


        botones.append(boton)

    contador = 0
    for i in botones:
        i.place(x = 10, y = 50 + 40*(contador))
        contador = contador +1


    ventana.mainloop()