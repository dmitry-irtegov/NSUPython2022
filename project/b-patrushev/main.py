from tkinter import Frame, BOTH, Canvas, Label, Tk, NW
from PIL import Image, ImageTk
from mandelbrot import Mandelbrot
import numpy as np


class GUI(Frame):
    def __init__(self, parent, h, w):
        Frame.__init__(self, parent)
        self.workFlag = False
        self.background = None
        self.parent = parent
        self.parent.title("Mandelbrot")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.mandel = Mandelbrot(height=h, width=w)
        self.pixels = self.mandel.draw()
        self.pixelColors = []
        self.draw()
        self.parent.bind("<Button-1>", self.zoomIn)
        self.parent.bind("<Button-3>", self.zoomOut)
        self.parent.bind("<Configure>", lambda event: self.handle_configure(parent))

    def handle_configure(self, parent):
        if self.mandel.w != parent.winfo_width() or self.mandel.h != parent.winfo_height():
            self.pixels = self.mandel.resize(parent.winfo_width(), parent.winfo_height())
            self.draw()

    def zoomIn(self, event):
        self.parent.title("Loading")
        if not self.workFlag:
            self.workFlag = True
            self.pixels = self.mandel.zoom(event)
            self.draw()
            self.workFlag = False
        self.parent.title("Done")

    def zoomOut(self, event):
        self.parent.title("Loading")
        if not self.workFlag:
            self.workFlag = True
            self.pixels = self.mandel.zoom(event, zoom_in=False)
            self.draw()
            self.workFlag = False
        self.parent.title("Done")

    def draw(self):
        self.drawPixels()
        self.canvas.create_image(0, 0, image=self.background, anchor=NW)
        self.canvas.pack(fill=BOTH, expand=1)

    def drawPixels(self):
        if isinstance(self.pixels, list):
            pixels = np.asarray(self.pixels).astype(np.uint8)
        if self.pixels.dtype != "uint8":
            pixels = self.pixels.astype(np.uint8)
        self.background = ImageTk.PhotoImage(Image.fromarray(pixels, mode='RGB').resize((self.mandel.w, self.mandel.h)))


def hide_show_label(label):
    if label.winfo_ismapped():
        label.pack_forget()
    else:
        label.pack()


def close_window(master):
    master.destroy()


def main():
    master = Tk()
    height = round(master.winfo_screenheight() * 0.9)
    label = Label(master, text="◉ Left click - ZoomIn \n◉ Right click - ZoomOut \n◉ z - close/open legend\n◉ Esc - "
                               "Exit")
    GUI(master, height, height)
    master.geometry("{}x{}".format(height, height))
    master.bind("<Escape>", lambda event: close_window(master))
    master.bind("z", lambda event: hide_show_label(label))

    label.pack()
    master.mainloop()


if __name__ == '__main__':
    labelFlag = True
    main()
