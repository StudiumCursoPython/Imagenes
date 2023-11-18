import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image
import sys
import os

def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Imágenes", "*.png;*.jpg;*.webp")])
    if file_paths:
        convert_images_to_pdf(file_paths)

def convert_images_to_pdf(image_paths):
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if not output_path:
        return

    images = []
    for image_path in image_paths:
        image = Image.open(image_path)
        images.append(image.convert("RGB"))

    if len(images) > 0:
        images[0].save(output_path, save_all=True, append_images=images[1:])
        print("Se ha creado el archivo PDF en:", output_path)


# Ventana de la aplicación
app = tk.Tk()
app.title("Conversor de Imágenes a Pdf")
app.geometry("400x200")
app.resizable(False, False)

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Cargar las imágenes
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Ruta de la imagen de fondo para cargarla, se ha generado y dimensionado en el ejercicio1 ImagenesBasic
background_image = PhotoImage(file="redimensionadaEjercicio1.png")

# Label para el fondo
background_label = tk.Label(app, image=background_image)
# Para ajustar la imagen al tamaño de la ventana
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

# Botón para seleccionar imágenes
select_button = tk.Button(app, text="Seleccionar imágenes", command=select_images)
select_button.pack(pady=20)

# Ejecutar la aplicación
app.iconphoto(True, icono)
app.mainloop()

