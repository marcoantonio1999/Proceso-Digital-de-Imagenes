from tkinter import Tk
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import math

"""
Marco Antonio Ordu;a Avila

Tarea 5 Estecanografia
"""


def codificar(pixel, lista):
    """
    Funcion que codifica 3 bits en un pixel
    """
    bBinario = format((pixel[0]), '08b')
    gBinario = format((pixel[1]), '08b')
    rBinario = format((pixel[2]), '08b')
    
    newBbinario = int((bBinario[:-1] + lista[0]),2)
    newGbinario = int((gBinario[:-1] + lista[1]),2)
    newRbinario = int((rBinario[:-1] + lista[2]),2)

    return [newBbinario, newGbinario, newRbinario]
    

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
    imgen = nombreImg+'.bmp'
    imagencv = cv2.imread(imgen)
    output = cv2.resize(imagencv, (700,400))

    cv2.imwrite('imgR.bmp',output)
    
    im = Image.open('imgR.bmp')
    ph = ImageTk.PhotoImage(im)
    global labelImg
    labelImg = Label(ventana, image=ph)
    labelImg.image=ph
    labelImg.place(x=1000,y=50)
    global imagen
    imagen = cv2.imread(imgen)

def mostrarCodificarTexto():
    """
    Funcion para mostrar la pantalla para elegir la imagen a la cual queremos
    codificar el texto

    """
    texto.delete('1.0', END)
    
    try:
        labelImg.destroy()
    except:
        getImagen()
    else:
        getImagen()


    global botonCodificar
    botonCodificar = Button(ventana, text="CODIFICAR", command=lambda: codificarTexto())
    botonCodificar.place(x=900, y=550)
    try:
        botonDecodificar.destroy()
    except:
        pass
def setImagenCodificar(nombreImg): 
    """
    Funcion para configurar la imagen en la ventana y poder manipularla
    la que se va a codificar
    """
    imgen = nombreImg+'.bmp'
    imagencv = cv2.imread(imgen)
    output = cv2.resize(imagencv, (700,400))

    cv2.imwrite('imgR.bmp',output)
    
    im = Image.open('imgR.bmp')
    ph = ImageTk.PhotoImage(im)
    global labelImgCodificar
    labelImgCodificar = Label(ventana, image=ph)
    labelImgCodificar.image=ph
    labelImgCodificar.place(x=200,y=50)
    global imagenCodificar
    imagenCodificar = cv2.imread(imgen)
    print(imagenCodificar)
 
def getImagenCodificar():
    """
    Obtiene la imagen que hay que codificar
    """
    top = Toplevel(ventana)
    top.geometry('300x200')
    labelCargar = Label(top, text="Introduce el nombre del archivo a Codificar")
    labelCargar.place(x=10, y = 10 )
    entradaNombre = Entry(top)
    entradaNombre.place(x =50, y= 50 )
    botonAceptar = Button(top, text='Aceptar', command= lambda : [setImagenCodificar(entradaNombre.get()), top.destroy()])
    botonAceptar.place(x = 50, y= 100) 

def codificarI():
    """
    Funcion que codifica una imagen dentro de otra
    """
    
    imgO = imagen.copy()
    
    

    imgG = imagenCodificar.copy()
    y,x,d = imgG.shape

    ancho = x
    altura = y
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
    
    cv2.imwrite("final.bmp", imgO)
    topSalio = Toplevel()
    topSalio.geometry("200x200")
    labelSalio = Label(topSalio, text="imagen codificada en final.bmp")
    labelSalio.place(x =20,y=20)

def mostrarCodificarImagen():
    """
    Muestra la pantalla para saber la imagen que se va a modificar
    """

    getImagen()
    getImagenCodificar()
    global botonCodificarI
    texto.destroy()
    botonCodificarI = Button(ventana, text="CODIFICAR", command=lambda: codificarI())
    botonCodificarI.place(x=900, y=550) 
    botonDecodificarI.destroy()

def mostrarDecodificarImagen():
    """
    Funcion para mostrar la pantalla donde se requiere la imagan que se
    requiere modificar
    """
    texto.delete('1.0', END)
    getImagen()
    global botonDecodificarI
    texto.destroy()
    botonDecodificarI = Button(ventana, text="DECODIFICAR", command=lambda: decodificarI())
    botonDecodificarI.place(x=900, y=550)
    botonCodificarI.destroy()

def decodificarI():
    """
    Funcion para decodificar una imagen dentro de otra
    """

    y,x,d = imagen.shape

    listaDimensionBits = []
    for i in range(30):
        listaDimensionBits += decodificar(imagen[0,i])
            
    alturaBit = ""
    anchoBit = ""
    listaDimension = listaDimensionBits[0:30]

    for i in range(15):
        anchoBit += listaDimension[i]
    del listaDimension[0:15]
    for i in range(15):
        alturaBit += listaDimension[i]

    ancho = int(anchoBit, 2)
    altura = int(alturaBit, 2)


    numPixelesAcodificar = ancho*altura*3*8 + 10


    listaBits = []
    cont =0
    for j in range(y):
        for i in range(x):
            if numPixelesAcodificar  == cont:
                break
            listaBits += decodificar(imagen[j,i])
            cont +=1
    del listaBits[:30]
    by = []
    for i in range(len(listaBits)//8):
        by.append(listaBits[i*8:(i+1)*8])

    matrizS = []
    for i in range(altura):
        matrizS.append([])
        for j in range(ancho):
            matrizS[i].append([])


    for j in range(altura):
        for i in range(ancho):
            b = ""
            for k in range(8):
                b += by[0][k]  
            g = ""
            del by[0]
            for k in range(8):
                g += by[0][k]
            del by[0]
            r = ""
            for k in range(8):
                r += by[0][k]
            del by[0]
            blue =int(b,2)
            green = int(g,2)
            red = int(r,2)
            
            matrizS[j][i] = [blue, green, red]
        
  
    imagenN = np.array(matrizS)
    cv2.imwrite('finalDeco.jpg',imagenN)   
    topSalio = Toplevel()
    topSalio.geometry("200x200")
    labelSalio = Label(topSalio, text="imagen decodificada en finalDeco.bmp")
    labelSalio.place(x =20,y=20)


def mostrarDecodificarTexto():
    """
    Funcion para mostrar la pantalla para decodificar un texto
    """
    try:
        labelImg.destroy()
    except:
        print("")
    else:
        texto.delete('1.0', END)
        getImagen()
        global botonDecodificar
        botonCodificar.destroy()
        botonDecodificar = Button(ventana, text="DECODIFICAR", command=lambda: decodificarTexto())
        botonDecodificar.place(x=900, y=550) 
    


def codificarTexto():
    """
    Funcion para codificar un texto dado
    """
    img = imagen.copy()
    textoC = texto.get("1.0",END)
    textoSinBreak = textoC[:-1]
    textoSinBreak += "|"
    
    textoAscci = []
    for i in textoSinBreak:
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
    cv2.imwrite("final.bmp", img)
    topSalio = Toplevel()
    topSalio.geometry("200x200")
    labelSalio = Label(topSalio, text="texto codificado en final.bmp")
    labelSalio.place(x =20,y=20)

def decodificar(pixel):

    """
    funcion para decodificar un pixel
    """
    b,g,r = pixel
    blueBits = format(b, '08b')
    greenBits = format(g,'08b')
    redBits = format(r,'08b')

    lista = [blueBits[-1], greenBits[-1], redBits[-1]]  
    
    return lista

def decodificarTexto():
    """
    Fucion para decodificar un texto dada la imagen cargada
    """
    y,x,d = imagen.shape

    bitsAdecodificar = []
    for j in range(y):
        for i in range(x):
            bit = decodificar(imagen[j,i])
            bitsAdecodificar +=  bit
            
    letras = []
    for i in range(math.floor(len(bitsAdecodificar)/8)):
        byte = bitsAdecodificar[:8]

        byteD = ''
        for i in byte:
            byteD += i
        
        letra = chr(int(byteD,2))
        
        if letra == "|":
            break
        letras.append(letra)
        del bitsAdecodificar[:8]

    textoDe = ""
    for i in letras:
        textoDe += i

    texto.insert(END, textoDe)
    print("entro",textoDe)

if __name__ == "__main__":

    ventana = Tk()
    ventana.geometry('1600x1000')
    titulo = Label(ventana, text='Estecanografia')

    global texto
    texto = Text(ventana)
    texto.place(x=150,y =50)
    top = Toplevel(ventana)
    top.geometry('600x250')
    
    resultado = Label(top, text='Escoge si quieres codificar o decodificar un texto o una imagen')
    resultado.place(x=10, y=10)

    botonCtexto = Button(ventana, text="Codificar Texto", command= lambda: mostrarCodificarTexto())
    botonDtexto = Button(ventana, text="Codificar Texto", command= lambda: mostrarDecodificarTexto())
    botonCimagen = Button(ventana, text="Codificar Texto", command= lambda: mostrarCodificarImagen())
    botonDimagen = Button(ventana, text="Codificar Texto", command= lambda: mostrarDecodificarImagen())

    botonCtexto.place(x=10, y=60)
    botonDtexto.place(x=10, y=110)
    botonCimagen.place(x=10, y=160)
    botonDimagen.place(x=10, y=210)


    top.mainloop()