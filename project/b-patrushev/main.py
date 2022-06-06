import math
from tkinter import *
from PIL import Image, ImageTk
from mandelbrot import Mandelbrot


class GUI(Frame):
    def __init__(self, parent, h, w):
        Frame.__init__(self, parent)
        self.background = None
        self.palette = None
        self.parent = parent
        self.parent.title("Mandelbrot")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.mandel = Mandelbrot(height=h, width=w)
        self.pixels = self.mandel.draw(self.mandel.x, self.mandel.y)
        self.setPalette()
        self.pixelColors = []
        self.draw()
        parent.bind("<Button-1>", self.zoomIn)
        parent.bind("<Button-3>", self.zoomOut)
        parent.bind("<Configure>", lambda event: self.handle_configure(parent))

    def handle_configure(self, parent):
        if self.mandel.w != parent.winfo_width() or self.mandel.h != parent.winfo_height():
            self.mandel.resize(parent.winfo_width(), parent.winfo_height())
            self.draw()

    def zoomIn(self, event):
        self.pixels = self.mandel.zoom(event)
        self.draw()

    def zoomOut(self, event):
        self.pixels = self.mandel.zoom(event, zoom_in=False)
        self.draw()

    def draw(self):
        self.getColors()
        self.drawPixels()
        self.canvas.create_image(0, 0, image=self.background, anchor=NW)
        self.canvas.pack(fill=BOTH, expand=1)

    def drawPixels(self):
        img = Image.new('RGB', (self.mandel.w, self.mandel.h), "black")
        pixels = img.load()
        for index, p in enumerate(self.pixels):
            pixels[int(p[0]), int(p[1])] = self.pixelColors[index]
        self.background = ImageTk.PhotoImage(img.resize((self.mandel.w, self.mandel.h)))

    def getColors(self):
        pixelColors = []
        for p in self.pixels:
            pixelColors.append(self.palette[p[2] % 256])
        self.pixelColors = pixelColors

    def setPalette(self):
        palette = [(0, 0, 0)]
        redb = 0.046889442590892436
        redc = 152.13901099951926
        greenb = 0.04027682889217683
        greenc = 147.10775385307488
        blueb = 0.0328962581527727
        bluec = 80.3177542266761

        for i in range(256):
            r = clamp(int(256 * (0.5 * math.sin(redb * i + redc) + 0.5)))
            g = clamp(int(256 * (0.5 * math.sin(greenb * i + greenc) + 0.5)))
            b = clamp(int(256 * (0.5 * math.sin(blueb * i + bluec) + 0.5)))
            palette.append((r, g, b))
        self.palette = palette


def clamp(x):
    return max(0, min(x, 255))


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
