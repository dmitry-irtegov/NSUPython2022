import time
from tkinter import Canvas, EventType

from PIL import Image, ImageTk

from fractal import Mandelbrot


class InteractiveCanvas(Canvas):
    def __init__(self, parent, width, height):
        Canvas.__init__(self, parent, width=width, height=height, highlightthickness=0)
        self.pack(fill='both', expand=True)

        self._photoImage = None
        self._image_widget_ref = None

        self._text_widget_ref = self.create_text(
            width - 10, height - 10, anchor='se', justify='right',
            fill='white', font=('normal', 15, 'bold'))

        self._fractal = Mandelbrot(width, height, zoom_factor=0.3)
        self.render()

        self.bind('<Double-Button-1>', self._zoom_in)
        self.bind('<Button-2>', self._zoom_out)
        self.bind('<Button-3>', self._zoom_out)

        self.bind('<B1-Motion>', self._move)
        self.bind('<Button-1>', self._move_begin)
        self.bind('<ButtonRelease-1>', self._move_end)

        self.bind('<Up>', self._move)
        self.bind('<Down>', self._move)
        self.bind('<Left>', self._move)
        self.bind('<Right>', self._move)

        self.bind('-', self._zoom_out)
        self.bind('_', self._zoom_out)
        self.bind('+', self._zoom_in)
        self.bind('=', self._zoom_in)

        self.focus_set()

    def _move(self, event):
        mid_x = self._fractal.width // 2
        mid_y = self._fractal.height // 2
        move_amount = 10

        if event.keysym == 'Up':
            self._fractal.move(mid_x, mid_y - move_amount)
        elif event.keysym == 'Down':
            self._fractal.move(mid_x, mid_y + move_amount)
        elif event.keysym == 'Left':
            self._fractal.move(mid_x - move_amount, mid_y)
        elif event.keysym == 'Right':
            self._fractal.move(mid_x + move_amount, mid_y)
        else:
            self._fractal.move(mid_x - event.x + self._motionX,
                               mid_y - event.y + self._motionY)
            self._motionX = event.x
            self._motionY = event.y

        self.render()

    def _move_begin(self, event):
        self._motionX = event.x
        self._motionY = event.y

    def _move_end(self, event):
        self._motionX = None
        self._motionY = None

    def _zoom_in(self, event):
        if event.type == EventType.KeyPress:
            self._fractal.zoom_in(amount=0.75)
        else:
            self._fractal.zoom_in(event.x, event.y)
        self.render()

    def _zoom_out(self, event):
        if event.type == EventType.KeyPress:
            self._fractal.zoom_out(amount=0.75)
        else:
            self._fractal.zoom_out(event.x, event.y)
        self.render()

    def render(self):
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
