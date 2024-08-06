from tkinter import Tk, BOTH, Canvas
import tkinter as tk 


class Window():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.__root = tk.Tk()
        self.__root.title("Mi Ventana")
        self.canvas = tk.Canvas(self.__root, width=self.width, height=self.height) # canvas widget
        self.canvas.pack() #se empaqueta
        self.running = False # Estado de ejecución de la ventana

    def redraw(self):
        # Redibujar todos los gráficos en la ventana
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Establecer el estado de ejecución a True
        self.running = True
        
        # Continuar redibujando mientras la ventana esté en ejecución
        while self.running:
            self.redraw()

    def close(self):
        # Establecer el estado de ejecución a False
        self.running = False