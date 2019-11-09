from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def leeImg(src):
    img = cv2.imread(src)
    return img

def muestaImg(img):
    # Usa la libreria matplotlib para mostar una imagen en una ventana
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
    plt.show()

def escribeImg(img, nombre, formato):
    src_salida = creaDirSalida()
    # guardar la imagen en formato JPG
    cv2.imwrite(src_salida +"/"+ nombre + "." + formato, img)
    print("Se guardo la imagen con el nombre: " + nombre + ", src: " + src_salida)

def creaDirSalida():
    # Crea un directorio con el nombre /img-salida, si no existe y retorna la ruta de la carpeta creada

    script_dir = os.path.dirname(__file__) #ruta absoluta del script
    nombre = "img-salida"
    try:
        os.stat(script_dir + "/" + nombre)
        print("El directorio de salida /"+ nombre +" ya existe.") 
        return(""+ script_dir + "/" + nombre) 
    except:
        os.mkdir(script_dir + "/img-salida")
        print("Se creo el directorio /"+ nombre)
        return(""+ script_dir + "/" + nombre) 


if __name__ == "__main__":
    
    src = "C:/Users/Valentina/Documents/Procesaminento-de-imagenes-master/Procesaminento-de-imagenes-master/mariposa.jpg"
    
    imagen = leeImg(src)
    muestaImg(imagen)
    escribeImg(imagen, "copia", "png")


      