from email.mime import image
import tkinter
from tkinter import *
import cv2
import math 


def escalaGrises(imagen, version):
    """
    Funcion para calcular el filtro de una imagen a escala de grises la version
    depende a la formula que necesitemos
    """
    y,x,d = imagen.shape
    
    for i in range(1,y):
        
        for j in range(1,x):
            if version == 1:
                gris = math.floor((imagen.item(i, j, 0) + imagen.item(i, j, 1)+ imagen.item(i, j, 2))/3)
            if version == 2:
                gris = 0.11*(imagen.item(i, j, 0))  + 0.59*(imagen.item(i, j, 1))+ 0.3*(imagen.item(i, j, 2))
            if version == 3:
                gris = 0.0722*(imagen.item(i, j, 0))  + 0.7152*(imagen.item(i, j, 1))+ 0.2126*(imagen.item(i, j, 2))
            if version == 4:
                gris = 0.114*(imagen.item(i, j, 0))  + 0.587*(imagen.item(i, j, 1))+ 0.299*(imagen.item(i, j, 2))    
            if version == 5: 
                gris = math.floor((max(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)) + min(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)))/2)  
            if version == 6:
                gris = max(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2))
            if version == 7:
                gris = min(imagen.item(i, j, 0),imagen.item(i, j, 1),imagen.item(i, j, 2)) 

            imagen.itemset((i, j, 0), gris)
            imagen.itemset((i, j, 1), gris)
            imagen.itemset((i, j, 2), gris)   
    return imagen

def filtroDimensional(iamgen, color):
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
                 
def mosaico(iamgen, rangoX, rangoY):
    pass

if __name__ == '__main__':

    imagen = cv2.imread('img.jpg')
    y,x,d = imagen.shape
    
    #imagenNueva = cv2.imwrite('final.jpg',escalaGrises(imagen,7))
    #imagenNueva = cv2.imwrite('final.jpg',filtroDimensional(imagen,'azul'))
    


    
    #ventana = Tk()
    #ventana.mainloop()

