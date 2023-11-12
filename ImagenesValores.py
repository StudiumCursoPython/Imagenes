from PIL import Image

ancho = input("Dame el ancho")
alto = input("Dame el alto")

'''
#Captura excepciones numéricas
def solicitar_numero(mensaje):
    while True:
        try:
            # Solicitar el valor al usuario
            valor = input(mensaje)

            # Intentar convertirlo a entero
            valor_numerico = int(valor)
            return valor_numerico
        except ValueError:
            # Manejar el error si el valor no es un número
            print("Por favor, introduce un número válido.")

# Solicitar ancho y alto al usuario
ancho = solicitar_numero("Dame el ancho: ")
alto = solicitar_numero("Dame el alto: ")
'''

def redimensionar_imagen(ruta_entrada, ruta_salida, tamaño):
    with Image.open(ruta_entrada) as img:
        # método de la librería PIL para redimensionar la imagen
        imagen_redimensionada = img.resize(tamaño)

        # Método de la librería para guardar los cambios, similitud al tratamiento de archivos
        imagen_redimensionada.save(ruta_salida)

# Ejemplo de uso
ruta_entrada = r'C:/Users/Pepe/Documents/CursoFormacionPython/Imagenes/ImgCurso.png'
ruta_salida = r'C:/Users/Pepe/Documents/CursoFormacionPython/Imagenes/redimensionada.png'
nuevo_tamaño = (ancho, alto)  # Nuevo tamaño en píxeles

redimensionar_imagen(ruta_entrada, ruta_salida, nuevo_tamaño)