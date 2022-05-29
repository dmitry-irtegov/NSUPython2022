from mandelbrot import calculate_image


class Mandelbrot:
    def __init__(self, width, height, zoom_factor, x=-0.75, y=0.0, m=1.5):
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

        self._zoomFactor = zoom_factor
        self._yScaleFactor = self.height / height
        self._xScaleFactor = self.width / width

    def update_pixels(self):
        self.pixels = calculate_image(self.width, self.height, self._xMin, self._xMax, self._yMin, self._yMax)

    def move(self, x, y):
        self._update_center(x, y)
        self._update_bounds()

    def zoom_in(self, x=None, y=None, amount=None):
        if x and y:
            self._update_center(x, y)
        if amount is None:
            amount = self._zoomFactor
        self.delta *= amount
        self._xDelta *= amount
        self._yDelta *= amount
        self._update_bounds()

    def zoom_out(self, x=None, y=None, amount=None):
        if x and y:
            self._update_center(x, y)
        if amount is None:
            amount = self._zoomFactor
        self.delta /= amount
        self._xDelta /= amount
        self._yDelta /= amount
        self._update_bounds()

    def _update_center(self, x, y):
        self.xCenter = Mandelbrot._translate(x * self._xScaleFactor, 0, self.width, self._xMin, self._xMax)
        self.yCenter = Mandelbrot._translate(y * self._yScaleFactor, self.height, 0, self._yMin, self._yMax)

    def _update_bounds(self):
        self._xMin, self._xMax = self.xCenter - self._xDelta, self.xCenter + self._xDelta
        self._yMin, self._yMax = self.yCenter - self._yDelta, self.yCenter + self._yDelta

    @staticmethod
    def _translate(value, left_min, left_max, right_min, right_max):
        left_span = left_max - left_min
        right_span = right_max - right_min
        value_scaled = float(value - left_min) / float(left_span)
        return right_min + (value_scaled * right_span)
