from tkinter import Button, Canvas, PhotoImage
from PIL import Image, ImageDraw
import tkinter as tk
import sys, os

class AplicacionFirma:
    def __init__(self, raiz):
        self.raiz = raiz
        # self se utiliza para acceder y modificar los atributos de la instancia

        # Obtener la ruta de acceso a los recursos incluidos en el archivo para los archivos empaquetados
        ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        # Otra forma de obtener los recursos 
        # ruta_recursos = getattr(sys, 'os.path.dirname(os.path.abspath(__file__))', os.path.dirname(os.path.abspath(__file__)))

        # Cargar las imágenes
        icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))
        # Función que construye la ruta completa al archivo de imagen "Studium.png" válida para los sistemas W y Linux con '_MEIPASS'

        raiz.title("Firma con el Ratón")
        raiz.iconphoto(True,icono)
        raiz.resizable(False,False)


        self.lienzo = Canvas(raiz, width=400, height=200, bg="white")
        self.lienzo.pack()

        self.imagen = Image.new("RGB", (400, 200), "white")
        self.dibujo = ImageDraw.Draw(self.imagen)

        # Captura de evento de movimiento del ratón con botón izquierdo presionado
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
            #Para poder verlo
            self.lienzo.create_line((x1, y1, x2, y2), fill="black", width=2)
            #Para el posterior guardado en el archivo
            self.dibujo.line((x1, y1, x2, y2), fill="black", width=2)
        self.ultimo_punto = (evento.x, evento.y)

    def resetear_estado(self, evento): # Se necesitan los dos aunque en este caso evento no se usa. Pasa en algunos casos.
        self.ultimo_punto = None

    def borrar(self):
        self.lienzo.delete("all")
        self.dibujo.rectangle((0, 0, 400, 200), fill="white")

    def guardar(self):
        nombre_archivo = "firma.png"
        self.imagen.save(nombre_archivo)
        print(f"Firma guardada como {nombre_archivo}")

        # Mostrar el nombre del archivo en el lienzo
        self.lienzo.create_text(300, 180, text=f"Guardado como: {nombre_archivo}", fill="green")

        # Función para borrar el texto y limpiar el lienzo
        def borrar_texto():
            #self.lienzo.delete(texto_id)
            self.lienzo.delete("all")

        # Llamar a la función borrar_texto después de 3 segundos (3000 milisegundos)
        self.raiz.after(3000, borrar_texto)
        

# Crear la ventana principal y la aplicación
raiz = tk.Tk()
app = AplicacionFirma(raiz)

# Llama automáticamente al método __init__ de la clase AplicacionFirma
raiz.mainloop()
