import time
from tkinter import Canvas

from PIL import Image, ImageTk

from .mandelbrot import Mandelbrot


class InteractiveCanvas(Canvas):
    def __init__(self, parent, width, height):
        Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0)
        self.pack(fill='both', expand=True)

        self._photoImage = None
        self._image_widget_ref = None

        self._text_widget_ref = self.create_text(
            width - 10, height - 10, anchor='se', justify='right',
            fill='white', font=('normal', 15, 'bold'))

        self._fractal = Mandelbrot(width, height, zoomFactor=0.1)
        self._render()

        self.bind('<Button-1>', self._zoom_in)
        self.bind('<Button-2>', self._zoom_out)
        self.bind('<Control-1>', self._move)

    def _move(self, event):
        self._fractal.move(event)
        self._render()

    def _zoom_in(self, event):
        self._fractal.zoom_in(event)
        self._render()

    def _zoom_out(self, event):
        self._fractal.zoom_out(event)
        self._render()

    def _render(self):
        start = time.time()
        self._fractal.update_pixels()
        c_end = time.time()

        image = Image.frombuffer(mode='RGBA', data=self._fractal.pixels, size=self._fractal.pixels.shape)
        self._photoImage = ImageTk.PhotoImage(image)

        self.delete(self._image_widget_ref)
        self._image_widget_ref = self.create_image(0, 0, image=self._photoImage, anchor='nw')

        self.tag_raise(self._text_widget_ref, self._image_widget_ref)
        self.itemconfig(self._text_widget_ref, text=f'X: {self._fractal.xCenter:.3g}, '
                                                    f'Y: {self._fractal.yCenter:.3g}, '
                                                    f'Δ: {self._fractal.delta:.3g}')

        end = time.time()
        print(f'Rendering took {end - start:.2f} seconds (C++ part: {(c_end - start) / (end - start) * 100:.2f}%)')
