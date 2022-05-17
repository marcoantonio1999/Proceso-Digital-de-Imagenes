import math
import cv2
from tkinter import *
import math
from PIL import Image, ImageTk


def promedio(porcion):
    """
    Funcion para calcular el promedio de una lista de duplas de pixeles, esto para calcular el promedio de los
    colores del BGR de todos los pixeles
    """
    y,x,d = porcion.shape
    sumB = 0
    sumG = 0
    sumR = 0
    
    for j in range(y):
        for i in range(x):
            sumB += porcion[j,i,0]
            sumG += porcion[j,i,1]
            sumR += porcion[j,i,2]

    promB = sumB/(x*y)
    promG = sumG/(x*y)
    promR = sumR/(x*y)
    return promB,promG, promR


def aplicaPromedio(b,g,r,porcion):
    """
    Funcion para aplicar un rgb a una porcion dada
    """
    y,x,d = porcion.shape
    for j in range(y):
        for i in range(x):
            porcion[j,i] = [b,g,r]
    return porcion

def matrizColores(anchoX, anchoY):
    """
    Funcion para sacar una matriz del promedio de los colores dados la altura y el ancho de cada porcion
    """
    copia = imagen.copy()
    y,x,d = imagen.shape
    anchoSeccion = math.floor(x/anchoX)
    alturaSeccion = math.floor(y/anchoY)
    matrizColores = []
    for i in range(anchoY):
        matrizColores.append([])
        for j in range(anchoX):
            matrizColores[i].append([])

    for j in range(anchoY):
        for i in range(anchoX):
            porcion = imagen[(j*alturaSeccion) : ((j+1)*alturaSeccion) ,i*anchoSeccion:(i+1)*anchoSeccion ]
            b,g,r = promedio(porcion)
            matrizColores[j][i] = (b,g,r)
            copia[(j*alturaSeccion) : ((j+1)*alturaSeccion) ,i*anchoSeccion:(i+1)*anchoSeccion ] = aplicaPromedio(b,g,r,porcion)

    
    return matrizColores


def letrasColores(ancho, altura):
    """
    Funcion para calcular el filtro de las letras de colores
    """
    matriz = matrizColores(ancho, altura)
    f = open('letrasColores.html', 'w')
    dibujo = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            dibujo = dibujo  + '<span style = color:rgb('+str(matriz[i][j][2]) +','+ str(matriz[i][j][1]) + ',' + str(matriz[i][j][0]) +')>M</span>'  
        dibujo = dibujo + "<br>"
    contenido = """
    <html>
    <head></head>
    <body>
    """+dibujo+"""
    </body>
    </html>
    """
    f.write(contenido)
    f.close() 

def letrasColoresTop(entradaX, entradaY):
    """
    Funcion para llamar la funcion del filtro de colores
    """
    letrasColores(int(entradaX), int(entradaY))
    abreResultante()

def letrasColoresFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: letrasColoresTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )

def letrasGrises(ancho, altura):
    """
    Funcion para calcular el filtro de las letras grises
    """
    matriz = matrizColores(ancho, altura)
    f = open('letrasGrises.html', 'w')

    dibujo = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = (matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3
            dibujo = dibujo  + '<span style = color:rgb('+str(prom) +','+ str(prom) + ',' + str(prom) +')>M</span>'  
        dibujo = dibujo + "<br>"
    contenido = """
    <html>
    <head></head>
    <body>
    """+dibujo+"""
    </body>
    </html>
    """
    f.write(contenido)
    f.close() 

def letrasGrisesTop(entradaX, entradaY):
    """
    Filtro para mandar a llamar la funcion que calcula el filtro de letras de grises
    y avisa que ya termino
    """
    letrasGrises(int(entradaX), int(entradaY))
    abreResultante()

def letrasGrisesFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: letrasGrisesTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )



def letrasByNVariadas(ancho, altura):
    """
    Funcion que calcula el filtro de las letras variadas en blanco negro
    """
    matriz = matrizColores(ancho, altura)
    f = open('letrasByNVariadas.html', 'w')
    dibujo = ""

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = int((matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3)
            letra = ""
            if 0<=prom<=15:
                letra = "M"
            if 16<=prom<=31:
                letra = "N"
            if 32<=prom<=47:
                letra = "H"
            if 48<=prom<=63:
                letra = "#"
            if 64<=prom<=79:
                letra = "M"
            if 80<=prom<=95:
                letra = "Q"
            if 96<=prom<=111:
                letra = "U"
            if 112<=prom<=127:
                letra = "D"
            if 128<=prom<=143:
                letra = "O"
            if 144<=prom<=159:
                letra = "Y"
            if 160<=prom<=175:
                letra = "2"
            if 176<=prom<=191:
                letra = "$"
            if 191<=prom<=209:
                letra = "%"
            if 210<=prom<=225:
                letra = "+"
            if 226<=prom<=239:
                letra = "."
            if 240<=prom<=255:
                letra = "&nbsp"
            dibujo = dibujo  + '<span>'+letra +'</span>'  
        dibujo = dibujo + "<br>"
    contenido = """
    <html>
    <head>
    <style type="text/css">
        span {
        font-family:Courier New

        }
    </style>
    
    </head>
    <body>
    """+dibujo+"""
    </body>
    </html>
    """
    f.write(contenido)
    f.close() 

def letrasByNVariadasTop(entradaX, entradaY):
    """
    Funcion para mandar a llamar la funcion que calcula el filtro de letras variadas en blanco 
    y negro y avisa si ya termino
    """
    letrasByNVariadas(int(entradaX), int(entradaY))
    abreResultante()

def letrasByNVariadasFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: letrasByNVariadasTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )






def letrasGrisesVariadas(ancho, altura):
    """
    Funcion para caulcar el filtro de letras variadas pero en escala de grises
    """
    matriz = matrizColores(ancho, altura)
    f = open('letrasGrisesVariadas.html', 'w')
    dibujo = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = int((matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3)
            letra = ""
            if 0<=prom<=15:
                letra = "M"
            if 16<=prom<=31:
                letra = "N"
            if 32<=prom<=47:
                letra = "H"
            if 48<=prom<=63:
                letra = "#"
            if 64<=prom<=79:
                letra = "M"
            if 80<=prom<=95:
                letra = "Q"
            if 96<=prom<=111:
                letra = "U"
            if 112<=prom<=127:
                letra = "D"
            if 128<=prom<=143:
                letra = "O"
            if 144<=prom<=159:
                letra = "Y"
            if 160<=prom<=175:
                letra = "2"
            if 176<=prom<=191:
                letra = "$"
            if 191<=prom<=209:
                letra = "%"
            if 210<=prom<=225:
                letra = "+"
            if 226<=prom<=239:
                letra = "."
            if 240<=prom<=255:
                letra = "&nbsp"
            dibujo = dibujo  + '<span style = color:rgb('+str(prom) +','+ str(prom) + ',' + str(prom) +')>'+letra +'</span>'  
        dibujo = dibujo + "<br>"
    contenido = """
    <html>
    <head>
    <style type="text/css">
        span {
        font-family:Courier New

        }
    </style>
    
    </head>
    <body>
    """+dibujo+"""
    </body>
    </html>
    """
    f.write(contenido)
    f.close() 

def letrasGrisesVariadasTop(entradaX, entradaY):
    """
    Funcion para mandar a llamar la funcion que calcula el filtro de letras variadas en escala
    de grises y avisa si ya termino
    """
    letrasGrisesVariadas(int(entradaX), int(entradaY))
    abreResultante()

def letrasGrisesVariadasFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: letrasGrisesVariadasTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )



def letrasColoresVariadasTop(entradaX, entradaY):
    """
    Funcion para mandar a llamar la funcion que calcula el filtro de letras variadas pero en colores
    y avisa si ya termino 
    """
    letrasColoresVariadas(int(entradaX), int(entradaY))
    abreResultante()

def letrasColoresVariadasFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: letrasColoresVariadasTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )



def letrasColoresVariadas(ancho, altura):
    """
    Funcion que calcula el filtro de letras de colores variadas
    """
    matriz = matrizColores(ancho, altura)
    f = open('letrasColoresVariadas.html', 'w')
    dibujo = ""

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = int((matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3)
            letra = ""
            if 0<=prom<=15:
                letra = "M"
            if 16<=prom<=31:
                letra = "N"
            if 32<=prom<=47:
                letra = "H"
            if 48<=prom<=63:
                letra = "#"
            if 64<=prom<=79:
                letra = "M"
            if 80<=prom<=95:
                letra = "Q"
            if 96<=prom<=111:
                letra = "U"
            if 112<=prom<=127:
                letra = "D"
            if 128<=prom<=143:
                letra = "O"
            if 144<=prom<=159:
                letra = "Y"
            if 160<=prom<=175:
                letra = "2"
            if 176<=prom<=191:
                letra = "$"
            if 191<=prom<=209:
                letra = "%"
            if 210<=prom<=225:
                letra = "+"
            if 226<=prom<=239:
                letra = "."
            if 240<=prom<=255:
                letra = "&nbsp"
            dibujo = dibujo  + '<span style= color:rgb('+str(int(matriz[i][j][2])) +','+ str(int(matriz[i][j][1])) + ',' + str(int(matriz[i][j][0])) +')>'+letra +'</span>\n'  
        dibujo = dibujo + "<br>\n"
    contenido = """
    <html>
    <head>
    <style type="text/css">
        span {
        font-family:Courier New

        }
    </style>
    
    </head>
    <body>
    """+dibujo+"""
    </body>
    </html>
    """
    f.write(contenido)
    f.close() 




def fraseColoresTop(entradaX, entradaY, frase):
    """
    Funcion para mandar a llamar el filtro de la frase de colores y avisa que ya termino
    """
    fraseColoresVariadas(int(entradaX), int(entradaY), frase)
    abreResultante()

def fraseColoresFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura, ancho y la frase
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
    labelFrase = Label(top, text="Frase")
    entradaFrase = Entry(top)
    labelFrase.place(x=10, y=110)
    entradaFrase.place(x=200, y= 110)
    botonAceptar = Button(top, text='Aceptar', command= lambda: fraseColoresTop(entradaX.get(), entradaY.get(), entradaFrase.get()))
    botonAceptar.place(x = 100, y = 160 )
    


def fraseColoresVariadas(ancho, altura, frase):
    """
    Funcion que calcula el filtro de las frases de colores
    """
    matriz = matrizColores(ancho, altura)
    f = open('fraseColores.html', 'w')
     
    dibujo = ""
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            
            
            dibujo = dibujo  + '<span style= color:rgb('+str(int(matriz[i][j][2])) +','+ str(int(matriz[i][j][1])) + ',' + str(int(matriz[i][j][0])) +')>'+frase[j%(len(frase))] +'</span>\n'  
        dibujo = dibujo + "<br>\n"
    contenido = """
    <html>
    <head>
    <style type="text/css">
        span {
        font-family:Courier New

        }
    </style>
    
    </head>
    <body>
    """+dibujo+"""
    </body>
    </html>
    """
    f.write(contenido)
    f.close() 


def naipesTop(entradaX, entradaY):
    """
    Funcion para mandar a llamar la funcion de los naipes y avisar que ya termino
    """
    naipes(int(entradaX), int(entradaY))
    abreResultante()

def naipesFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: naipesTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )



def naipes(ancho, altura):
    """
    Funcion para calcular el filtro de los naipes
    """
    matriz = matrizColores(ancho, altura)
    f = open('naipes.txt', 'w')

    dibujo = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = int((matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3)
            letra = ""
            if 0<=prom<=22:
                letra = "a"
            if 23<=prom<=45:
                letra = "b"
            if 46<=prom<=68:
                letra = "c"
            if 69<=prom<=91:
                letra = "d"
            if 92<=prom<=114:
                letra = "e"
            if 115<=prom<=137:
                letra = "f"
            if 138<=prom<=160:
                letra = "g"
            if 161<=prom<=183:
                letra = "h"
            if 184<=prom<=206:
                letra = "i"
            if 207<=prom<=229:
                letra = "j"
            if 230<=prom<=255:
                letra = "k"
            if letra == "":
                print("letraVacias", prom)
            dibujo = dibujo  +letra
        dibujo = dibujo + "\n"
    
    f.write(dibujo)
    f.close() 


def DominoTop(entradaX, entradaY):
    """
    Funcion que manda a llamar la funcion que calcula el domino y avisa si ya termino
    """
    domino(int(entradaX), int(entradaY))
    abreResultante()

def DominoFun():
    """
    Funcion para abrir una nueva ventana para poner las opciones de la altura y el ancho
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
    botonAceptar = Button(top, text='Aceptar', command= lambda: DominoTop(entradaX.get(), entradaY.get()))
    botonAceptar.place(x = 100, y = 100 )



def domino(ancho, altura):
    """
    Funcion para calcular el filtro de domino
    """
    matriz = matrizColores(ancho, altura)
    f = open('domino.txt', 'w')

    dibujo = ''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = (matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3
            
            letra = ""
            if 0<=prom<=25:
                letra = "0" if j%2 != 0 else ")"         
            if 26<=prom<=50:
                letra = "1" if j%2 != 0 else "!"
            if 50<=prom<=75:
                letra = "2" if j%2 != 0 else "@"
            if 75<=prom<=100:
                letra = "3" if j%2 != 0 else "#"
            if 100<=prom<=125:
                letra = "4" if j%2 != 0 else "$"
            if 125<=prom<=150:
                letra = "5" if j%2 != 0 else "%"
            if 150<=prom<=175:
                letra = "6" if j%2 != 0 else "^"
            if 175<=prom<=200:
                letra = "7" if j%2 != 0 else "&"
            if 200<=prom<=225:
                letra = "8" if j%2 != 0 else "*"
            if 225<=prom<=255:
                letra = "9" if j%2 != 0 else "("
            dibujo = dibujo  +letra
        dibujo = dibujo + "\n"
    
    f.write(dibujo)
    f.close() 


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
    
def abreResultante():
    """
    Funcion para mostrar el resultado de aplicar alguno de los filtros
    """

    res = Toplevel(ventana)
    res.geometry('250x250')
    
    resultado = Label(res, text='Filtro Guardado en la carpeta raiz')
    resultado.place(x=10, y=10)
    
    res.mainloop()   

if __name__ == "__main__":

    ventana = Tk()
    ventana.geometry('1600x1000')
    titulo = Label(ventana, text='Filtros basicos Tarea 1')
    titulo.place(x = 620, y = 10)
    getImagen()
    nombreBotones = ['Letras Colores', 'Letra con tono Grises', 'Letras variadas Blanco y Negro ', 'Efecto 1 y 3 combinados', 'Efecto 2 y 3 combinados',
    'texto predeterminado', 'Cartas','Domino'
    ]
    funciones = [letrasColoresFun, letrasGrisesFun, letrasByNVariadasFun,letrasColoresVariadasFun,
    letrasGrisesVariadasFun, fraseColoresFun,  naipesFun, DominoFun
    ]
    botones = []
    for i in range(len(nombreBotones)):
        boton = Button(ventana, text=nombreBotones[i], command= lambda i=i: funciones[i]()) 
        botones.append(boton)
    contador = 0
    for i in botones:
        i.place(x = 10, y = 50 + 40*(contador))
        contador = contador +1
    
    ventana.mainloop()
    