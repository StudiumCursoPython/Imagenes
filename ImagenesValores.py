from PIL import Image

ancho = input("Dame el ancho: ")
alto = input("Dame el alto: ")

def redimensionar_imagen(ruta_entrada, ruta_salida, tamaño):
    with Image.open(ruta_entrada) as img:
        # método de la librería PIL para redimensionar la imagen
        imagen_redimensionada = img.resize(tamaño)

        # Método de la librería para guardar los cambios, similitud al tratamiento de archivos
        imagen_redimensionada.save(ruta_salida)

# Ejemplo de uso
ruta_entrada = r'C:/Users/Pepe/Documents/CursoFormacionPython/Imagenes/ImgCurso.png'
ruta_salida = r'C:/Users/Pepe/Documents/CursoFormacionPython/Imagenes/redimensionadaEjercicio2.png'

# Nuevo tamaño en píxeles
nuevo_tamaño = (ancho, alto)  

redimensionar_imagen(ruta_entrada, ruta_salida, nuevo_tamaño)