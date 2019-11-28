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
root.title('Signal Processing ...')
root.config(background='white')

figure = Figure(figsize=(6, 6), dpi=130)
plot1 = figure.add_subplot(2, 1, 1)
plot2 = figure.add_subplot(2, 1, 2)



def init_draw(plot, a=1, b=1):
    plot.clear()
    x = np.linspace(-2.2,2.2)
    y1 = -x-1
    y2 = x-1
    y3 = (x**2)/4
    y4 = x-x+1
    y5 = x-x
    plot1.plot(x,y1)
    plot1.plot(x,y2)
    plot1.plot(x,y3)
    plot1.plot(x,y4)
    plot1.plot(x,y5)
    plot1.plot(a, b, color="red", marker="o", linestyle="")

def draw_hn(plot, a=1, b=1):
    plot.clear()
    Yz = [1]
    Zz = [1, a, b]
    r, p, k = signal.residuez(Yz,Zz)
    n = np.linspace(0,150,151)
    h=0
    for i in range(len(r)):
       h+=r[i]*((p[i])**n) 
    h+=sum(k)
    plot.plot(n,h)

init_draw(plot1)
draw_hn(plot2)

def callback(event):
    a, b = event.inaxes.transData.inverted().transform((event.x, event.y))
    print((a,b))
    init_draw(plot1, a, b)
    draw_hn(plot2,a,b)
    canvas.draw()

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)
canvas.callbacks.connect('button_press_event', callback)



root.mainloop()