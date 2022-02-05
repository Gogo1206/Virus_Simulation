from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import variable
  
# plot function is created for 
# plotting the graph in 
# tkinter window
  
# the main Tkinter window
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
  
# button that displays the plot

# fig2 = Figure(figsize = (5, 5),
#                  dpi = 100)
  
#     # list of squares

  
#     # adding the subplot

  
#     # plotting the graph



# plot2 = fig2.add_subplot(111)

# plot2.plot(y)
  
#     # creating the Tkinter canvas
#     # containing the Matplotlib figure
# canvas = FigureCanvasTkAgg(fig,
#                                master = window)  
# canvas.draw()

# canvas2 = FigureCanvasTkAgg(fig2,
#                                master = window)  

# canvas2.draw()
  
#     # placing the canvas on the Tkinter window
# canvas.get_tk_widget().pack()

# canvas2.get_tk_widget().pack()
  
#     creating the Matplotlib toolbar
# toolbar = NavigationToolbar2Tk(canvas,
#                                    window)
# toolbar.update()
  
#     # placing the toolbar on the Tkinter window
# canvas.get_tk_widget().pack()
  
# run the gui
window.mainloop()