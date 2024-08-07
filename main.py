from tkinter import Tk, BOTH, Canvas
from window import Window, Point, Line, Cell


def main():
    # Crear una ventana
    window = Window(800, 600)

    # Crear algunos puntos y líneas
    p1 = Point(100, 200)
    p2 = Point(300, 400)
    p3 = Point(500, 600)
    p4 = Point(300, 200)

    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    # Crear y dibujar las celdas
    cell1 = Cell(50, 50, 100, 100, window)
    cell1.draw()
    cell2 = Cell(100, 50, 150, 100, window)
    cell2.draw()
    
    # Dibujar el movimiento entre las celdas
    cell1.draw_move(cell2)

    # Dibujar líneas en la ventana
    window.draw_line(line1, "black")
    window.draw_line(line2, "red")


    # Esperar a que se cierre la ventana
    window.wait_for_close()
if __name__ == "__main__":
    main()