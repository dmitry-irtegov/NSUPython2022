import ctypes


class Mandelbrot:
    def __init__(self, height, width):
        self.fractal = [[0] * width] * height
        self.zoomFactor = 0.1
        self.m = 1.5
        self.x = -0.75
        self.y = 0
        self.h = height
        self.w = width
        self.xmin = self.x - self.m
        self.xmax = self.x + self.m
        self.ymin = self.y - self.m
        self.ymax = self.y + self.m
        so_file = "./Mandelbrot.so"
        self.cp = ctypes.CDLL(so_file)
        self.cp.mandelbrot.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int]
        self.cp.mandelbrot.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))
        self.pixels = []

    def draw(self, x, y):
        self.fractal = self.cp.mandelbrot(ctypes.c_double(x), ctypes.c_double(y), ctypes.c_double(self.m),
                                          ctypes.c_int(self.w),
                                          ctypes.c_int(self.h))
        for i in range(self.w):
            for j in range(self.h):
                self.pixels.append((i, j, self.fractal[j][i]))

        return self.pixels

    def resize(self, new_w=None, new_h=None):
        if new_w != self.w and new_w is not None:
            self.x = self.translate(event.x, 0, new_w, self.xmin, self.xmax)
            self.w = new_w
        if new_h != self.h and new_h is not None:
            self.y = self.translate(event.y, 0, new_h, self.ymin, self.ymax)
            self.h = new_h
        self.xmin = self.x - self.m
        self.xmax = self.x + self.m
        self.ymin = self.y - self.m
        self.ymax = self.y + self.m
        self.draw(self.x, self.y)

    def zoom(self, event, zoom_in=True):
        new_x = self.translate(event.x, 0, self.w, self.xmin, self.xmax)
        new_y = self.translate(event.y, 0, self.h, self.ymin, self.ymax)
        if zoom_in is True:
            self.m *= self.zoomFactor
        else:
            self.m /= self.zoomFactor
        self.xmin = new_x - self.m
        self.xmax = new_x + self.m
        self.ymin = new_y - self.m
        self.ymax = new_y + self.m
        return self.draw(new_x, new_y)

    @staticmethod
    def translate(value, left_min, left_max, right_min, right_max):
        left_span = left_max - left_min
        right_span = right_max - right_min
        value_scaled = float(value - left_min) / float(left_span)
        return right_min + (value_scaled * right_span)
