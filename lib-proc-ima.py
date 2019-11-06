from PIL import Image
import time
import os

def leeImg(src):
    img = Image.open(src)
    return img

def muestaImg(img):
    img.show()

def escribeImg(img, nombre, formato):
    src_salida = creaDirSalida()
    img.save(src_salida +"/"+ nombre + "." + formato)
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
   
def convRGVtoYUV(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/kevin/Desktop/" + im)
    im = Image.open(ruta)
    im.show()
    
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i,j))
            #g = (r + g + b) / 3
            #gris = int(g)
            y = 0.299*r + 0.587*g + 0.114*b
            u = -0.147*r - 0.289*g + 0.436*b
            v = 0.615*r - 0.515*g - 0.100*b
            pixel = tuple([int(y), int(u), int(v)])
            im2.putpixel((i,j), pixel)
            j+=1
        i+=1
    im2.show()
    
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, 'Segundos')   

if __name__ == "__main__":
    
    #Ejecucion de los metodos que lee, muestra y guarda una imagen
    imagen = leeImg("C:/Users/kevin/Documents/Procesamiento-de-imagenes/images/21_training.tif")
    muestaImg(imagen)
    escribeImg(imagen, "copia2", "png")