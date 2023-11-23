from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image
import tkinter as tk
import os
import sys

def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.webp")])
    if file_paths:
        convertir_imagen_webp(file_paths)

def convertir_imagen_webp(image_paths):
    for image_path in image_paths:
        image = Image.open(image_path)
        image_rgb = image.convert("RGB")

        # Define el nombre del archivo de salida
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = filedialog.asksaveasfilename(initialfile=base_name, defaultextension=".webp", filetypes=[("WEBP", "*.webp")])
        if output_path:
            image_rgb.save(output_path, format="webp")
            print("Se ha creado el archivo WEBP en:", output_path)

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
select_button = tk.Button(app, text="Seleccionar imágenes", command=select_images)
select_button.pack(pady=20)

# Ejecutar la aplicación
app.iconphoto(True, icono)
app.mainloop()
