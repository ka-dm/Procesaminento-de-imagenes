from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from Tkinter import *

# -*- coding: utf-8 -*- 
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

def histograma(img):
    # Muestra el histograma de la imagen
    
    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color = c)
        plt.xlim([0,256])

    plt.show()
    cv2.destroyAllWindows()

def interfaz():
    

    ventana = Frame(height=250, width=250)
    ventana.pack(padx=25,pady=25)

    boton1 = Button(ventana,text="Mostrar imagen").place(x=50,y=0)
    boton2 = Button(ventana,text="RGB a YUV").place(x=50,y=50)
    boton3 = Button(ventana,text="Histograma").place(x=50,y=100)


    ventana.mainloop()


if __name__ == "__main__":
    
    src = "hola.jpg"
    
    interfaz()


    imagen = leeImg(src)
    histograma(imagen)
    muestaImg(imagen)    
    escribeImg(imagen, "copia", "jpg")
    


      