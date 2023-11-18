import tkinter as tk
from tkinter import Button, Canvas, PhotoImage
from PIL import Image, ImageDraw
import sys, os

class AplicacionFirma:
    def __init__(self, raiz):
        self.raiz = raiz

        ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

        raiz.title("Firma con el Ratón")
        raiz.iconphoto(True,icono)
        raiz.resizable(False,False)


        self.lienzo = Canvas(raiz, width=400, height=200, bg="white")
        self.lienzo.pack()

        self.imagen = Image.new("RGB", (400, 200), "white")
        self.dibujo = ImageDraw.Draw(self.imagen)

        #Cuando se presiona el botón izquierdo del ratón
        self.lienzo.bind("<B1-Motion>", self.dibujar)
        #Cuando se suelta el mismo
        self.lienzo.bind("<ButtonRelease-1>", self.resetear_estado)

        self.boton_borrar = Button(raiz, text="Borrar", command=self.borrar)
        self.boton_borrar.pack(side="left")

        self.boton_guardar = Button(raiz, text="Guardar", command=self.guardar)
        self.boton_guardar.pack(side="right")

        self.ultimo_punto = None

    def dibujar(self, evento):
        if self.ultimo_punto:
            x1, y1 = self.ultimo_punto
            x2, y2 = evento.x, evento.y
            self.lienzo.create_line((x1, y1, x2, y2), fill="black", width=2)
            #Para el posterior guardado en el archivo
            self.dibujo.line((x1, y1, x2, y2), fill="blue", width=2)
        self.ultimo_punto = (evento.x, evento.y)

    def resetear_estado(self, evento):
        self.ultimo_punto = None

    def borrar(self):
        self.lienzo.delete("all")
        self.dibujo.rectangle((0, 0, 400, 200), fill="white")

    def guardar(self):
        nombre_archivo = "firma.png"
        self.imagen.save(nombre_archivo)
        print(f"Firma guardada como {nombre_archivo}")

# Crear la ventana principal y la aplicación
raiz = tk.Tk()
app = AplicacionFirma(raiz)
raiz.mainloop()
