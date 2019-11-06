from PIL import Image
import time

def leeImg(src):
    img = Image.open(src)
    return img

def muestaImg(img):
    img.show()

def escribeImg(img):
    img.save("C:/Users/kevin/Documents/Procesamiento-de-imagenes/granja-copia.jpg", "png")
    #print("El nombre de la imagen es: " + img.filename)   
   
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
    imagen = leeImg("C:/Users/kevin/Desktop/granja.png")
    #muestaImg(imagen)
    escribeImg(imagen)