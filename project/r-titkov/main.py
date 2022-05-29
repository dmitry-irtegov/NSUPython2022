import argparse
import ctypes
import pathlib
import time
import tkinter as tk
from PIL import ImageTk, Image


class App:
	MINIMUM_ZOOM_FRAME_SIZE = 50

	window_height = 700
	window_width = 700
	canvas_scale = 1
	first_point = None
	second_point = None
	previous_center = None
	zoom_direction = 0
	infoMenu = None

	def __init__(self, c_lib, window_height=700, window_width=700, max_steps=600):
		self.c_lib = c_lib
		self.window_height = window_height
		self.window_width = window_width

		self.buffer = ctypes.create_string_buffer(self.window_height * self.window_width * 3)

		c_lib.setWindowSize(self.window_width, self.window_height)
		c_lib.setMaxSteps(max_steps)

		self.root = tk.Tk()
		self.root.minsize(300, 300)
		self.root.config(width=self.window_width, height=self.window_height)
	
		self.canvas = tk.Canvas(self.root, width=self.window_width, height=self.window_height, highlightthickness=0)
		self.canvas.pack()
		self.canvas.bind('<B1-Motion>', self.leftMotion)
		self.canvas.bind('<Button-1>', self.leftPush)
		self.canvas.bind('<ButtonRelease-1>', self.leftRelease)
		self.canvas.bind('<Double-1>', self.leftDoubleClick) 

		self.canvas.bind('<B2-Motion>', self.rightMotion)
		self.canvas.bind('<Button-2>', self.rightPush)
		self.canvas.bind('<ButtonRelease-2>', self.rightRelease)
		self.canvas.bind('<B3-Motion>', self.rightMotion)
		self.canvas.bind('<Button-3>', self.rightPush)
		self.canvas.bind('<ButtonRelease-3>', self.rightRelease)
		
		self.canvas.bind('<MouseWheel>', self.mouseZoom)
		self.canvas.bind('<Left>', self.moveFrame)
		self.canvas.bind('<Right>', self.moveFrame)
		self.canvas.bind('<Up>', self.moveFrame)
		self.canvas.bind('<Down>', self.moveFrame)
		self.canvas.bind('+', self.buttonZoom)
		self.canvas.bind('=', self.buttonZoom)
		self.canvas.bind('-', self.buttonZoom)
		self.canvas.bind('_', self.buttonZoom)

		self.root.bind("<Configure>", self.resizeWindow)
  
		self.infoButton = tk.Button(self.root, text="?", command=self.openMenu, height=2, width=1)
		self.infoButton.place(x=self.window_width - 50, y=10)

		self.canvas.focus_set()

	def closeMenu(self):
		if self.infoMenu is not None:
			self.infoMenu.destroy()
			self.infoMenu = None

	def openMenu(self):
		self.closeMenu()
		self.infoMenu = tk.Tk()
		self.infoMenu.title("Controls")
		self.infoMenu.minsize(400, 250)
		self.infoMenu.config(width=400, height=400)
		self.infoMenu.protocol("WM_DELETE_WINDOW", self.closeMenu)
		tk.Label(self.infoMenu, text="Arrows - move up/down/left/right").grid(
					row=0, column=0, sticky=tk.N, pady=5, padx=40)
		tk.Label(self.infoMenu, text="Motion with right button pressed - move image").grid(
					row=1, column=0, sticky=tk.N, pady=5, padx=40)
		tk.Label(self.infoMenu, text="Left Double click - set center").grid(
					row=2, column=0, sticky=tk.N, pady=5, padx=40)
		tk.Label(self.infoMenu, text="Move with left button presses - choose part to zoom in").grid(
					row=3, column=0, sticky=tk.N, pady=5, padx=40)
		tk.Label(self.infoMenu, text="Mouse scroll - zoom in / zoom out").grid(
					row=4, column=0, sticky=tk.N, pady=5, padx=40)
		tk.Label(self.infoMenu, text="+/- - zoom in / zoom out").grid(
					row=5, column=0, sticky=tk.N, pady=5, padx=40)
		tk.Label(self.infoMenu, text="Move with left button presses - choose part to zoom in").grid(
					row=6, column=0, sticky=tk.N, pady=5, padx=40)

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

	def resizeWindow(self, event):
		if event.width < 300 or event.height < 300:
			return
	
		self.window_height = event.height
		self.window_width = event.width

		self.buffer = ctypes.create_string_buffer(self.window_height * self.window_width * 3)
		self.canvas.config(width=self.window_width, height=self.window_height)
		c_lib.setWindowSize(self.window_width, self.window_height)
		self.updateFrame()

	def recalculate(self):
		# start = time.time()
		self.c_lib.calculate(self.buffer)
		self.image = ImageTk.PhotoImage(Image.frombuffer('RGB', (self.window_width, self.window_height), self.buffer, 'raw'))
		# end = time.time()
		# print("Recalculating finished:", end - start)

	def redraw(self):
		# start = time.time()
		self.canvas.create_image(0,0, anchor="nw", image=self.image)
		# end = time.time()
		# print("Redrawing finished:", end - start)

	def updateFrame(self):
		self.recalculate()
		self.redraw()
		centerXState = ctypes.c_double()
		centerYState = ctypes.c_double()
		dxState = ctypes.c_double()
		dyState = ctypes.c_double()
		self.c_lib.getState(ctypes.byref(centerXState), ctypes.byref(centerYState), 
									ctypes.byref(dxState), ctypes.byref(dyState))
		text = f'CX: {format(centerXState.value,".1E")}\nCY: {format(centerYState.value,".1E")}\n\
DX: {format(dxState.value,".1E")}\nDY: {format(dyState.value,".1E")}'
		self.canvas.create_text(10, 10, text=text, anchor=tk.NW, fill="white")
		self.infoButton.place(x = self.window_width - 50, y = 10)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('libname') 
	args = parser.parse_args()

	libname = pathlib.Path().absolute() / args.libname
	
	c_lib = ctypes.CDLL(libname)

	app = App(c_lib)
	app.updateFrame()
	app.root.mainloop()
