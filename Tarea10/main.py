import pathlib
import os
import os.path
from PIL import Image
import cv2
from PIL import ImageFile
from torch import diag_embed
ImageFile.LOAD_TRUNCATED_IMAGES = True

if __name__ == "__main__":

    entrada = input("Introduce el nombre del directorio en el cual tienes tu dataset de imagenes")
    print("Las imagenes se procesaran a una resolucion un poco menor para que el mosaico pueda quedar bien")
    print("Se escogen imagenes cuadradas para simplificar el algoritmo")
    dimension = int(input("introduce el ancho del cual quieres cada imagen que se procese"))
    print("las imagenes se guardaran en un nuevo directorio llamado ImagenesProcesadas")

    directory = "ImagenesProcesadas"
    
    
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory " , directory ,  " Created ")
    else:    
        print("Directory " , directory ,  " already exists")

    c = 0
    for file in pathlib.Path(entrada).iterdir():
        filename = "{}.jpg".format(c)
        im = Image.open(file)
        newsize = (dimension, dimension)
        im = im.resize(newsize)
        print(file)
        im.save("{}/{}.jpg".format(directory,c))
        
        c += 1
