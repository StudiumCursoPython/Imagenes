from PIL import Image

def solicitar_numero(mensaje): 
    valor = input(mensaje)
    try:
        return int(valor)
    except ValueError:
        print("Por favor, introduce un número válido.")

# Solicitar ancho y alto al usuario
ancho = solicitar_numero("Dame el ancho: ")
alto = solicitar_numero("Dame el alto: ")

def redimensionar_imagen(ruta_entrada, ruta_salida, tamaño):
    with Image.open(ruta_entrada) as img:
        imagen_redimensionada = img.resize(tamaño)
        imagen_redimensionada.save(ruta_salida)

# Ejemplo de uso
ruta_entrada = r'C:/Users/Pepe/Documents/CursoFormacionPython/Imagenes/ImgCurso.png'
ruta_salida = r'C:/Users/Pepe/Documents/CursoFormacionPython/Imagenes/redimensionadaEjercicio3.png'
nuevo_tamaño = (ancho, alto)  # Nuevo tamaño en píxeles

redimensionar_imagen(ruta_entrada, ruta_salida, nuevo_tamaño)
