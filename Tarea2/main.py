from tkinter import *
import cv2
import math
from PIL import Image, ImageTk
import copy

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

    
    botonAceptar = Button(top, text='Aceptar', command= lambda : setImagen(entradaNombre.get()))
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
    ventana.geometry('1500x900')
    titulo = Label(ventana, text='Filtros basicos Tarea 1')
    titulo.place(x = 620, y = 10)

    getImagen()


    img = imagen.copy()
    filtro = blur(img)
    imagenNueva = cv2.imwrite('final.jpg',filtro)
    res = Toplevel(ventana)
    res.geometry('800x800')
    imgf = ImageTk.PhotoImage(Image.open('final.jpg'))
    resultado = Label(res, text='Filtros resultante')
    resultado.place(x=10, y=10)
    labelImg = Label(res, image=imgf    )
    labelImg.place(x=50, y = 50)
    res.mainloop()
    

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
    

    ventana.mainloop()

