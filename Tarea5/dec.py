from base64 import encode
from struct import unpack
import cv2
from numpy import packbits, unpackbits
import numpy as np



def decodificar(pixel):
    b,g,r = pixel
    blueBits = format(b, '08b')
    greenBits = format(g,'08b')
    redBits = format(r,'08b')

    lista = [blueBits[-1], greenBits[-1], redBits[-1]]
    
    return lista




imagen = cv2.imread("final.bmp")

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
print(len(listaBits))
del listaBits[:30]
print(len(listaBits))
by = []
for i in range(len(listaBits)//8):
    by.append(listaBits[i*8:(i+1)*8])


print(len(by))

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

    
cv2.imwrite('final.jpg',imagenN)        



#texto = ""
#for i in letras:
#    letra = ""
#    for j in i:
#        letra += j
#    if(chr(int(letra,2)) == "|"):
#        break
#    texto += chr(int(letra,2))
       
#print(texto)
