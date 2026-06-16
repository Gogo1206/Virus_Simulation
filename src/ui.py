import tkinter as tk
from tkinter import ttk

import variable
import ppmodel
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk,
)
from shape import Shape

HEIGHT = variable.Y_LIMIT / 10
WIDTH = variable.X_LIMIT / 10
fig = Figure()
plot1 = fig.add_subplot()
window = tk.Tk()
frame = ttk.Frame(window)
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
graph = FigureCanvasTkAgg(fig, master=window)
window.title("Virus Simulation")
toolbar = NavigationToolbar2Tk(graph, frame)
shape = Shape(canvas)


def start_ui():
    """Initialize and display the Tkinter UI window."""
    window.geometry(str(int(WIDTH) * 2) + "x" + str(int(HEIGHT) + 50))
    frame.pack(side=tk.BOTTOM)
    graph.get_tk_widget().pack(
        side='right', anchor='nw', expand=True, fill='both')
    canvas.pack(side='left', anchor='nw', expand=True, fill='both')
    toolbar.update()


def ui_redraw(person):
    """Draw a person onto the canvas with status-based color."""
    if person.status == variable.DiseaseStatus.VULNERABLE:
        if person.masked and person.vaccinated:
            color = "#00008b"
        elif person.masked:
            color = "#ADD8E6"
        elif person.vaccinated:
            color = "#4d4dff"
        else:
            color = "white"
    if person.status == variable.DiseaseStatus.INCUBATION:
        color = "yellow"
    if person.status == variable.DiseaseStatus.ASYMPTOMATIC:
        color = "orange"
    if person.status == variable.DiseaseStatus.SYMPTOMATIC:
        color = "red"
    if person.status == variable.DiseaseStatus.IMMUNE:
        color = "green"
    if person.status == variable.DiseaseStatus.DEAD:
        color = "black"
    shape.draw_oval(person.location.getX() / 10,
                    person.location.getY() / 10, 5, color)


def draw_popularPlace():
    """Draw popular places on the canvas."""
    for place in ppmodel.popularPlaces:
        shape.draw_square(place.getX() / 10, place.getY() / 10, 20, 'pink')


def ui_refresh(day):
    """Refresh canvas with current day label."""
    canvas.create_text(55, 20, text="Day " + str(day),
                       fill="black", font=('Helvetica 24'))
    window.update()


def ui_delete():
    """Clear the canvas."""
    canvas.delete("all")


def print_graph(hours_past, max_infected_at_once, vulnerable_history,
                incubation_history, asymptomatic_history,
                symptomatic_history, infected_history, immune_history,
                dead_history):
    """Plot the simulation data on the matplotlib graph."""
    plot1.clear()
    plot1.set_xlim([0, hours_past])
    plot1.set_ylim([0, variable.NUM_PEOPLE])
    plot1.set_xlabel("Hours #")
    plot1.set_ylabel("Population #")
    plot1.axhline(y=max_infected_at_once, color="red", linestyle="--",
                  label="Max Infection")
    plot1.plot(vulnerable_history, label="Vulnerable #", lw=3, color='blue')
    plot1.plot(incubation_history, label="Incubation #", color="yellow")
    plot1.plot(asymptomatic_history, label="Asymptomatic #", color="orange")
    plot1.plot(symptomatic_history, label="Symptomatic #", color="red")
    plot1.plot(infected_history, label="Total Infected #", lw=3,
               color="purple")
    plot1.plot(immune_history, label="Immune #", lw=3, color="green")
    plot1.plot(dead_history, label="Dead #", color="black")
    plot1.legend(loc='lower center', bbox_to_anchor=(0.5, 1),
                 ncol=3, fancybox=True, shadow=True)
    graph.draw()


def end():
    """Display end page and start Tkinter main loop."""
    window.mainloop()
