import numba
import numpy as np


class Mandelbrot:
    def __init__(self, height, width):
        self.pixels = []
        self.zoomFactor = 0.1
        self.m = 1.5
        self.x = -0.5
        self.y = 1.75
        self.h = height
        self.w = width
        self.xmin = self.x - self.m
        self.xmax = self.x + self.m
        self.ymin = self.y - self.m
        self.ymax = self.y + self.m

    def draw(self):
        self.pixels = self.mandelbrot(1000)
        return self.pixels

    def mandelbrot(self, max_iter):
        redb = 0.046889442590892436
        redc = 152.13901099951926
        greenb = 0.04027682889217683
        greenc = 147.10775385307488
        blueb = 0.0328962581527727
        bluec = 80.3177542266761

        grid1D = np.arange(0, self.w)
        grid2D = np.arange(0, self.w)
        xv, yv = np.meshgrid(grid1D, grid2D)
        iters = get_max_iter(xv, yv, self.w, self.h, max_iter, self.xmin, self.ymin, self.xmax, self.ymax).reshape((self.w, self.w, 1))
        pixels = np.where(iters == np.array([max_iter - 1]),
                          np.array([0, 0, 0]),
                          256 * (0.5 * np.sin(iters * np.array([redb, greenb, blueb]) + np.array([redc, greenc, bluec]))
                                 + 0.5))
        return pixels

    def resize(self, new_w=None, new_h=None):
        if new_w != self.w and new_w is not None:
            self.x = self.translate(self.x, 0, new_w, self.xmin, self.xmax)
            self.w = new_w
        if new_h != self.h and new_h is not None:
            self.y = self.translate(self.y, 0, new_h, self.ymin, self.ymax)
            self.h = new_h
        return self.update_xy()

    def zoom(self, event, zoom_in=True):
        self.x = self.translate(event.x, 0, self.w, self.xmin, self.xmax)
        self.y = self.translate(event.y, 0, self.h, self.ymin, self.ymax)
        if zoom_in is True:
            self.m *= self.zoomFactor
        else:
            self.m /= self.zoomFactor
        return self.update_xy()

    def update_xy(self):
        self.xmin = self.x - self.m
        self.xmax = self.x + self.m
        self.ymin = self.y - self.m
        self.ymax = self.y + self.m
        return self.draw()

    @staticmethod
    def translate(value, left_min, left_max, right_min, right_max):
        left_span = left_max - left_min
        right_span = right_max - right_min
        value_scaled = float(value - left_min) / float(left_span)
        return right_min + (value_scaled * right_span)


@numba.vectorize(['int64(int64, int64, int64, int64, int64, float64, float64, float64, float64)'], target="parallel")
def get_max_iter(x, y, width, height, max_iter, xmin, ymin, xmax, ymax):
    c0 = complex(xmin + (xmax - xmin) * x / width,
                 ymin + (ymax - ymin) * y / width)
    c = 0
    for i in range(1, max_iter):
        if abs(c) > 2:
            break
        c = c * c + c0
    return i
