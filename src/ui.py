from tkinter import *
from tkinter.ttk import *
from ball import Ball
import variable
import matplotlib.pyplot as plt

HEIGHT = variable.Y_LIMIT/10
WIDTH = variable.X_LIMIT/10
window = Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
graph=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
window.title("Virus Simulation")

def start_ui():
    window.geometry(str(int(WIDTH))+"x"+str(int(HEIGHT)))
    canvas.pack()

def ui_redraw(person,day):
    if(person.status==variable.disease_status.VULNERABLE):
        if(person.masked and person.vaccinated):
            color="#00008b"
        elif(person.masked):
            color="#ADD8E6"
        elif(person.vaccinated):
            color="#4d4dff"
        else:
            color="white"
    if(person.status==variable.disease_status.INCUBATION):
        color="yellow"
    if(person.status==variable.disease_status.ASYMPTOMATIC):
        color="orange"
    if(person.status==variable.disease_status.SYMPTOMATIC):
        color="red"
    if(person.status==variable.disease_status.IMMUNE):
        color="green"
    if(person.status==variable.disease_status.DEAD):
        color="black"
    ball = Ball(canvas,person.location.getX()/10,person.location.getY()/10,5,color)
    canvas.create_text(55, 20, text="Day "+str(day), fill="black", font=('Helvetica 24'))

def ui_refresh():
    window.update()

def ui_delete():
    canvas.delete("all")
    
def print_graph(max_day,max_infected_at_once,vulnerable_history,incubation_history,asymptomatic_history,symptomatic_history,infected_history,immune_history,dead_history):
    plt.xlim(0,max_day-1)
    plt.xlabel("Hours #")
    plt.ylabel("Population #")
    plt.axhline(y=max_infected_at_once,color="red",linestyle="--",label="Max Infection")
    plt.plot(vulnerable_history,label="Vulnerable #",lw=3,color='blue')
    plt.plot(incubation_history,label="Incubation #",color="yellow")
    plt.plot(asymptomatic_history,label="Asymptomatic #",color="orange")
    plt.plot(symptomatic_history,label="Sysptomatic #",color="red")
    plt.plot(infected_history,label="Total Infected #",lw=3,color="purple")
    plt.plot(immune_history,label="Immune #",lw=3,color="green")
    plt.plot(dead_history,label="Dead #",color="black")
    plt.legend()
    plt.show()