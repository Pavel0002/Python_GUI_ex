import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from random import random
import time
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *


def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement

tickersCount = 100;
chartList = ['ticker_' + str(x) for x in range(0, tickersCount, 1)]
#print(chartList)
maxSamplesPerTicker = 1200;
tickersDict = {chartItem:[0] for chartItem in chartList}

# for secondsIndex in range(maxSamplesPerTicker-1):
#     for tickerName, tickerSamples in tickersDict.items():
#         tickerSamples.append(tickerSamples[-1] + generate_movement())
#     time.sleep(1)


plt.ion()
class DynamicUpdate():
    #Suppose we know the x range
    min_x = 0
    max_x = 10

    def on_launch(self):
        #Set up plot
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[], 'o')
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()
        root = tk.Tk()
        bar1 = FigureCanvasTkAgg(self.figure, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        
        #start= mclass (root)
        self.variable = StringVar(root)
        tickersCount = 100;
        chartList = ['ticker_' + str(x) for x in range(0, tickersCount, 1)]
        self.variable.set(chartList[0])
        self.w = OptionMenu(root, self.variable, *chartList).pack()
        #window.mainloop()
        #root.mainloop()
        ...

    def on_running(self, xdata, ydata):
        #Update data (with the new _and_ the old points)
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)
        #Need both of these in order to rescale
        self.ax.relim()
        self.ax.autoscale_view() 
        # figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        # ax1 = figure1.add_subplot(111)
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    #Example
    def __call__(self):
        import numpy as np
        import time
        self.on_launch()
        xdata = []
        ydata = []
        
        for x in np.arange(0,maxSamplesPerTicker-1,1):
            xdata.append(x)
            #ydata.append(x)
            #ydata = list(tickersDict.values())[0]
            self.ax.set_xlim(self.min_x, len(xdata))
            self.on_running(xdata, list(tickersDict[self.variable.get()]))
            
            for tickerName, tickerSamples in tickersDict.items():
                tickerSamples.append(tickerSamples[-1] + generate_movement())
            
            time.sleep(1)
        return xdata, ydata

d = DynamicUpdate()
d()
