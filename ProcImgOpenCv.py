from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from Tkinter import *

# -*- coding: utf-8 -*- 
def leeImg(src):
    img = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    return img

def muestaImg(img):
    # Usa la libreria matplotlib para mostar una imagen en una ventana
    cv2.namedWindow('window',cv2.WINDOW_NORMAL)
    cv2.imshow('window',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
    
    color = ('r','g','b')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        plt.plot(hist, color = 'gray')
        plt.xlim([0,256])
        

    plt.show()
    cv2.destroyAllWindows()

def histograma2(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    Max = max(hist)
    arrayY=[]
    for i in hist :
        escala=((100*i)/Max)
        arrayY.append(escala)
    plt.plot(arrayY, color = 'black')
    plt.xlim([0,255])

    plt.show()
    print (Max)

def interfaz():
    

    ventana = Frame(height=250, width=250)
    ventana.pack(padx=25,pady=25)

    boton1 = Button(ventana,text="Mostrar imagen").place(x=50,y=0)
    boton2 = Button(ventana,text="RGB a YUV").place(x=50,y=50)
    boton3 = Button(ventana,text="Histograma").place(x=50,y=100)


    ventana.mainloop()


if __name__ == "__main__":
    
    src = "foto 8001.png"
    
    #interfaz()


    imagen = leeImg(src)
    histograma2(imagen)
    muestaImg(imagen)    
    escribeImg(imagen, "copia", "jpg")
    


      