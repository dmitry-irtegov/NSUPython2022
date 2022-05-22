from mandelbrot import calculate_image


class Mandelbrot:
    def __init__(self, width, height, zoomFactor, x=-0.75, y=0.0, m=1.5):
        self.width, self.height = width, height
        self.xCenter, self.yCenter = x, y
        self.delta = m
        self.pixels = None

        if width > height:
            self._xDelta = m / (height / width)
            self._yDelta = m
        else:
            self._yDelta = m / (width / height)
            self._xDelta = m

        self._xMin = x - self._xDelta
        self._xMax = x + self._xDelta

        self._yMin = y - self._yDelta
        self._yMax = y + self._yDelta

        self._zoomFactor = zoomFactor
        self._yScaleFactor = self.height / height
        self._xScaleFactor = self.width / width

    def update_pixels(self):
        self.pixels = calculate_image(self.width, self.height, self._xMin, self._xMax, self._yMin, self._yMax)

    def move(self, event):
        self._update_center(event)
        self._update_bounds()

    def zoom_in(self, event):
        self._update_center(event)
        self.delta *= self._zoomFactor
        self._xDelta *= self._zoomFactor
        self._yDelta *= self._zoomFactor
        self._update_bounds()

    def zoom_out(self, event):
        self._update_center(event)
        self.delta /= self._zoomFactor
        self._xDelta /= self._zoomFactor
        self._yDelta /= self._zoomFactor
        self._update_bounds()

    def _update_center(self, event):
        self.xCenter = Mandelbrot._translate(event.x * self._xScaleFactor, 0, self.width, self._xMin, self._xMax)
        self.yCenter = Mandelbrot._translate(event.y * self._yScaleFactor, self.height, 0, self._yMin, self._yMax)

    def _update_bounds(self):
        self._xMin, self._xMax = self.xCenter - self._xDelta, self.xCenter + self._xDelta
        self._yMin, self._yMax = self.yCenter - self._yDelta, self.yCenter + self._yDelta

    @staticmethod
    def _translate(value, left_min, left_max, right_min, right_max):
        left_span = left_max - left_min
        right_span = right_max - right_min
        value_scaled = float(value - left_min) / float(left_span)
        return right_min + (value_scaled * right_span)
