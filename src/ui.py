from tkinter import *
from tkinter.ttk import *
from ball import Ball
import variable

HEIGHT = variable.Y_LIMIT/10
WIDTH = variable.X_LIMIT/10
window = Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
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
            color="#0000FF"
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