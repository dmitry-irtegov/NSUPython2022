import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib import cm
import pathlib
import ctypes
from PIL import Image, ImageTk
import time


class App:
	MINIMUM_ZOOM_FRAME_SIZE = 50

	window_height = 700
	window_width = 700
	canvas_scale = 1
	first_point = None
	second_point = None
	previous_center = None
	zoom_direction = 0

	def __init__(self, c_lib, window_height, window_width):
		self.c_lib = c_lib
		self.window_height = window_height
		self.window_width = window_width

		self.root = Tk()
		# frm = ttk.Frame(self.root, padding=10)
		# frm.grid()

		self.canvas = Canvas(self.root, width=self.window_width, height=self.window_height, highlightthickness=0)
		# self.canvas.grid(column=1, row=0)
		self.canvas.pack()
		self.canvas.bind('<B1-Motion>', self.leftMotion)
		self.canvas.bind('<Button-1>', self.leftPush)
		self.canvas.bind('<ButtonRelease-1>', self.leftRelease)
		self.canvas.bind('<Double-1>', self.leftDoubleClick) 

		self.canvas.bind('<B2-Motion>', self.rightMotion)
		self.canvas.bind('<Button-2>', self.rightPush)
		self.canvas.bind('<ButtonRelease-2>', self.rightRelease)
		
		
		self.canvas.bind('<MouseWheel>', self.mouseZoom)
		self.canvas.bind('<Left>', self.moveFrame)
		self.canvas.bind('<Right>', self.moveFrame)
		self.canvas.bind('<Up>', self.moveFrame)
		self.canvas.bind('<Down>', self.moveFrame)
		self.canvas.bind('+', self.buttonZoom)
		self.canvas.bind('=', self.buttonZoom)
		self.canvas.bind('-', self.buttonZoom)
		self.canvas.bind('_', self.buttonZoom)
		self.canvas.focus_set()


	def moveFrame(self, event):
		centerX = ctypes.c_int32(self.window_width // 2)
		centerY = ctypes.c_int32(self.window_height // 2)

		if (event.keysym == 'Left'):
			centerX = ctypes.c_int32(self.window_width // 2 - self.window_width // 50)
		elif (event.keysym == 'Right'):
			centerX = ctypes.c_int32(self.window_width // 2 + self.window_width // 50)
		elif (event.keysym == 'Up'):
			centerY = ctypes.c_int32(self.window_height // 2 - self.window_height // 50)
		elif (event.keysym == 'Down'):
			centerY = ctypes.c_int32(self.window_height // 2 + self.window_height // 50)

		self.c_lib.setCenterRelative(centerX, centerY)
		self.updateFrame()


	def zoomInFrame(self, point1, point2):
		xmin = max(min(point1[0], point2[0]), 0)
		ymin = max(min(point1[1], point2[1]), 0)
		xmax = min(max(point1[0], point2[0]), self.window_width  - 1)
		ymax = min(max(point1[1], point2[1]), self.window_height - 1)

		self.c_lib.zoomInFrame(xmin, ymin, xmax, ymax)
		self.updateFrame()

	def buttonZoom(self, event):
		if event.char == '+' or event.char == '=':
			self.canvas_scale += 0.1
		elif event.char == '-' or event.char == '_':
			self.canvas_scale -= 0.1

		scale = ctypes.c_double(self.canvas_scale)
		self.c_lib.scaleFrame(scale)
		self.updateFrame()
		self.canvas_scale = 1
		self.zoom_direction = 0

	def mouseZoom(self, event):
		ZOOM_THRESHOLD = 1
		self.zoom_direction += event.delta

		if self.zoom_direction >= ZOOM_THRESHOLD:
			self.canvas_scale += 0.1
		elif self.zoom_direction <= -ZOOM_THRESHOLD:
			self.canvas_scale -= 0.1

		if abs(self.zoom_direction) >= ZOOM_THRESHOLD:
			print('zoom_direction:', self.zoom_direction)
			scale = ctypes.c_double(self.canvas_scale)
			self.c_lib.scaleFrame(scale)
			self.updateFrame()
			self.canvas_scale = 1
			self.zoom_direction = 0


	def leftMotion(self, event):
		if self.first_point is not None:
			if (event.x - self.first_point[0] > event.y - self.first_point[1]):
				self.second_point = (event.x, self.first_point[1] + event.x - self.first_point[0])
			else:
				self.second_point = (self.first_point[0] + event.y - self.first_point[1], event.y)
			self.canvas.delete('rect')
			if (abs(self.first_point[0] - self.second_point[0]) +
				 abs(self.first_point[1] - self.second_point[1]) > App.MINIMUM_ZOOM_FRAME_SIZE):
				outline_color = '#4ee44e'
			else:
				outline_color = 'red'
			self.canvas.create_rectangle(self.first_point, self.second_point, tags=("rect"), outline=outline_color)

	def leftPush(self, event):
		self.first_point = (event.x, event.y)

	def leftRelease(self, event):
		if self.first_point is not None and self.second_point is not None: 
			if (abs(self.first_point[0] - self.second_point[0])
					+ abs(self.first_point[1] - self.second_point[1]) > App.MINIMUM_ZOOM_FRAME_SIZE):
				self.zoomInFrame(self.first_point, self.second_point)

			self.canvas.delete('rect')
		self.first_point = None
		self.second_point = None

	def leftDoubleClick(self, event):                           
		self.c_lib.setCenterRelative(event.x, event.y)
		self.updateFrame()

	
	def rightMotion(self, event):
		diffX = event.x - self.previous_center[0]
		diffY = event.y - self.previous_center[1]

		centerX = ctypes.c_int32(self.window_width // 2 - diffX)
		centerY = ctypes.c_int32(self.window_height // 2 - diffY)
		
		self.c_lib.setCenterRelative(centerX, centerY)
		self.updateFrame()
		self.previous_center = (event.x, event.y)

	def rightPush(self, event):
		self.previous_center = (event.x, event.y)

	def rightRelease(self, _):
		self.previous_center = None
	

	def recalculate(self):
		start = time.time()
		buffer = ctypes.create_string_buffer(self.window_height * self.window_width * 3)

		self.c_lib.calculate(buffer)

		self.image_array = np.frombuffer(buffer, dtype=np.uint8)
		self.image_array.resize((self.window_height, self.window_width, 3))
		self.image = ImageTk.PhotoImage(Image.fromarray(self.image_array))
		end = time.time()
		print("Recalculating finished:", end - start)

	def redraw(self):
		start = time.time()
		self.canvas.create_image(0,0, anchor="nw", image=self.image)
		end = time.time()
		print("Redrawing finished:", end - start)

	def updateFrame(self):
		self.recalculate()
		self.redraw()


def getColors(step_count):
	colormap = cm.get_cmap('viridis', step_count + 1)
	colors = []
	for r,g,b,_ in colormap.colors:
		colors.append((r * 255, g * 255, b * 255))
	return np.array(colors, dtype=np.uint8)


if __name__ == "__main__":
	WINDOW_HEIGHT = 700
	WINDOW_WIDTH = 700
	MAX_STEPS = 500

	libname = pathlib.Path().absolute() / "libcppmult.so"
	c_lib = ctypes.CDLL(libname)

	c_lib.setWindowSize(WINDOW_HEIGHT, WINDOW_WIDTH)
	c_lib.setMaxSteps(MAX_STEPS)

	app = App(c_lib, WINDOW_HEIGHT, WINDOW_WIDTH)
	app.updateFrame()
	app.root.mainloop()
