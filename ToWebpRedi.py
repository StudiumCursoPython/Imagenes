import tkinter as tk
from tkinter import filedialog, simpledialog, PhotoImage, messagebox
from PIL import Image
import sys, os

def seleccionar_y_procesar_imagen():
    # Abre un diálogo para seleccionar la imagen
    file_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.webp")])
    if file_path:
        # Se piden las dimensiones de la imagen
        ancho, alto = solicitar_dimensiones()
        
        # Llama a la función para procesar la imagen
        convertir_y_redimensionar_imagen(file_path, ancho, alto)

def solicitar_dimensiones():
    # Se pide al usuario los valores de ancho y alto, se perimten valores vacios.
    ancho = simpledialog.askstring("Ancho", "Dame el ancho (en blanco valor original):")
    alto = simpledialog.askstring("Alto", "Dame el alto (en blanco valor original):")

    try:
        ancho = int(ancho) if ancho else None
        alto = int(alto) if alto else None
    except ValueError:
        print("Error en los tamaños.")
        messagebox.showerror("Error", "Las dimensiones no son correctas" + "\nSe mantendrá el tamaño original")
        return None, None
    
    return ancho, alto

def convertir_y_redimensionar_imagen(ruta_entrada, ancho, alto):
    with Image.open(ruta_entrada) as img:
        # Cuando las dimensiones son válidas redimensiona
        if ancho and alto:
            img = img.resize((ancho, alto))

        # Pasa la imagen a WEBP
        ruta_salida = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WEBP", "*.webp")])
        if ruta_salida:
            img.save(ruta_salida, format="webp")
            print("Archivo WEBP guardado en:", ruta_salida)

# Ventana de la aplicación
app = tk.Tk()
app.title("Conversor de Imágenes a WEBP")
app.geometry("400x200")
app.resizable(False, False)

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Cargar las imágenes
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Ruta de la imagen de fondo para cargarla
background_image = PhotoImage(file="redimensionadaEjercicio1.png")

# Label para el fondo
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta la imagen al tamaño de la ventana

# Botón para seleccionar imágenes
select_button = tk.Button(app, text="Selecciona una imagen", command=seleccionar_y_procesar_imagen)
select_button.pack(pady=20)

# Ejecutar la aplicación
app.iconphoto(True, icono)
app.mainloop()

