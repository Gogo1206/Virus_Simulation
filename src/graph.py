from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import variable

HEIGHT = variable.Y_LIMIT/10
WIDTH = variable.X_LIMIT/10
window = Tk()
window.geometry(str(int(WIDTH)*2)+"x"+str(int(HEIGHT)))

fig = Figure()
y = [i for i in range(101)]
z = [101-i for i in range(101)]


canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
graph=FigureCanvasTkAgg(fig,master = window)
window.title('Plotting in Tkinter')

plot1 = fig.add_subplot()
plot1.plot(y)
plot1.plot(z)
graph.draw()
graph.get_tk_widget().pack(side='right',anchor='nw',expand=True,fill='both')
canvas.pack(side='left',anchor='nw',expand=True,fill='both')

window.mainloop()