from tkinter import *
from tkinter.ttk import *

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler

import numpy as np
from scipy import signal

root = Tk()
root.config(background='white')
#root.geometry("1000x700")

figure = Figure(figsize=(6, 6), dpi=130)
plot1 = figure.add_subplot(2, 1, 1)
plot2 = figure.add_subplot(2, 1, 2)

x = np.linspace(-2.5,2.5)
y1 = -x-1
y2 = x-1
y3 = (x**2)/4
y4 = x-x+1
y5 = x-x
x1 = 0
plot1.plot(x,y1)
plot1.plot(x,y2)
plot1.plot(x,y3)
plot1.plot(x,y4)
plot1.plot(x,y5)

def callback(event):
    a, b = event.inaxes.transData.inverted().transform((event.x, event.y))
    print((a,b))
    # plot1.clear()
    # plot2.clear()
    # plot1.plot(y1)
    # plot2.plot(y1)
    # plot1.plot(a, b, color="red", marker="o", linestyle="")
    # canvas.draw()

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)
canvas.callbacks.connect('button_press_event', callback)



root.mainloop()