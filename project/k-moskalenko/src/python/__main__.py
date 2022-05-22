from tkinter import Tk

from .canvas import InteractiveCanvas

if __name__ == '__main__':
    root = Tk()
    root.title("Mandelbrot")
    root.resizable(False, False)

    height = round(0.8 * root.winfo_screenheight())
    width = round(1.4 * height)
    canvas = InteractiveCanvas(root, width, height)

    root.mainloop()
