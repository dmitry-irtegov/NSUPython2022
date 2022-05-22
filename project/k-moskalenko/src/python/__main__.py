from tkinter import Tk

from .canvas import InteractiveCanvas

if __name__ == '__main__':
    root = Tk()
    root.title("Mandelbrot")
    root.resizable(False, False)

    width, height = 1200, 900
    canvas = InteractiveCanvas(root, width, height)

    root.mainloop()
