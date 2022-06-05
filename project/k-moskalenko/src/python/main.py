#!.venv/bin/python3

from tkinter import Tk, Frame, Label, OptionMenu, Scale, IntVar, StringVar

from mandelbrot import set_palette, set_max_iterate
from canvas import InteractiveCanvas


def update_palette(*_):
    index = palettes.index(current_palette.get())
    set_palette(index, palette_size.get())
    canvas.render()


def update_max_iterations(*_):
    set_max_iterate(max_iterations.get())
    canvas.render()


if __name__ == '__main__':
    root = Tk()
    root.title("Mandelbrot")
    root.resizable(False, False)

    palettes = ('Spectrum', 'Earth & Sky', 'Grayscale', 'Random')
    current_palette = StringVar(value=palettes[0])
    max_iterations = IntVar(value=250)
    palette_size = IntVar(value=250)

    controls = Frame(root)
    for col in range(4):
        controls.columnconfigure(col, weight=1)
    controls.pack(fill='both', expand=True)

    iter_scale = Scale(controls, orient='horizontal', label='Max Iterations',
                       variable=max_iterations, from_=25, to=5000)
    iter_scale.bind('<ButtonRelease-1>', update_max_iterations)
    iter_scale.grid(column=0, row=0, sticky='ew', padx=10, pady=5)

    size_scale = Scale(controls, orient='horizontal', label='Palette Size',
                       variable=palette_size, from_=50, to=5000)
    size_scale.bind('<ButtonRelease-1>', update_palette)
    size_scale.grid(column=1, row=0, sticky='ew', padx=10, pady=5)

    paletteFrame = Frame(controls)
    paletteFrame.grid(column=2, row=0, sticky='s')
    Label(paletteFrame, text='Current Palette').pack()

    om = OptionMenu(paletteFrame, current_palette, *palettes, command=update_palette)
    om.configure(width=max(map(len, palettes)))
    om.pack(padx=10, pady=5)

    Label(controls,
          text='Use the left mouse button to drag the plane.\n'
               'Double left click to zoom in, right click to zoom out.\n'
               'Use arrow keys to move, plus and minus to zoom.') \
        .grid(column=3, row=0, sticky='ew', padx=10, pady=5)

    height = round(0.7 * root.winfo_screenheight())
    width = round(1.5 * height)
    canvas = InteractiveCanvas(root, width, height)

    update_palette()
    update_max_iterations()

    root.mainloop()
