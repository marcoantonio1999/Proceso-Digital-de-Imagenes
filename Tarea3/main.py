import math
import cv2

import math
def promedio(imagen):
    """
    Funcion para calcular el promedio de una lista de duplas de pixeles, esto para calcular el promedio de los
    colores del BGR de todos los pixeles
    """
    y,x,d = imagen.shape

    sumB = 0
    sumG = 0
    sumR = 0
    
    for j in range(y):
        for i in range(x):
            sumB += imagen[j,i,0]
            sumG += imagen[j,i,1]
            sumR += imagen[j,i,2]

    promB = sumB/(x*y)
    promG = sumG/(x*y)
    promR = sumR/(x*y)

    return promB,promG, promR


def aplicaPromedio(b,g,r,porcion):
    y,x,d = porcion.shape
    for j in range(y):
        for i in range(x):
            porcion[j,i] = [b,g,r]
    return porcion

def matrizColores(imagen, anchoX, anchoY):
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


def letrasColores(imagen,ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
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

def letrasGrises(imagen,ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.html', 'w')

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

def letrasGrisesVariadas(imagen,ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.html', 'w')
     
    dibujo = ""

    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = (matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3
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
            dibujo = dibujo  + '<span style="font-family:Courier New" style = color:rgb('+str(prom) +','+ str(prom) + ',' + str(prom) +')>'+letra +'</span>'  
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

def letrasColoresVariadas(imagen,ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.html', 'w')
     
    dibujo = ""

    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = (matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3
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


def letrasGrisesVariadas(imagen,ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.html', 'w')
     
    dibujo = ""

    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            prom = (matriz[i][j][2] + matriz[i][j][1] +  matriz[i][j][0])/3
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
            dibujo = dibujo  + '<span style= color:rgb('+str(prom) +','+ str(prom) + ',' + str(prom) +')>'+letra +'</span>\n'  
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


def fraseColoresVariadas(imagen,ancho, altura, frase):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.html', 'w')
     
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


def naipes(imagen, ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.txt', 'w')

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


def domino(imagen, ancho, altura):
    matriz = matrizColores(imagen, ancho, altura)
    f = open('letrasColores.txt', 'w')

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


    

if __name__ == "__main__":
    imagen = cv2.imread("img.jpg")
    filtro = fraseColoresVariadas(imagen, 100,100, "Hola Mami")
    

    