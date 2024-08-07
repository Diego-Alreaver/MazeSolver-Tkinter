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
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(
            self.p1.x, self.p1.y, 
            self.p2.x, self.p2.y, 
            fill=fill_color, 
            width=2)

class Cell:
    def __init__(self, x1, y1, x2, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2)
        if self.has_right_wall:
            self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2)
        if self.has_top_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1)
        if self.has_bottom_wall:
            self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2)

    def draw_move(self, to_cell, undo = False):
        x1,y1 = self.calcularmedio()
        x2,y2 = to_cell.calcularmedio()
        color = "red" if not undo else "gray"
        line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(line, color)

    def calcularmedio(self):
        medioX = (self._x1 + self._x2) / 2
        medioY = (self._y1 + self._y2) / 2
        return medioX, medioY

