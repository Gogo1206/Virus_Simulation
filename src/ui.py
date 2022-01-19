# import streamlit as st
# import pandas as pd
from tkinter import *
from tkinter.ttk import *
import numpy as np
import matplotlib.pyplot as plt
from ball import Ball
import person
import variable

HEIGHT = variable.Y_LIMIT/10
WIDTH = variable.X_LIMIT/10
window = Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT)

def start_ui():
    canvas.pack()
    #window.mainloop()

def ui_redraw(person):
    if(person.status==variable.disease_status.VULNERABLE):
        color="blue"
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

def ui_refresh():
    window.update()

def ui_delete():
    canvas.delete("all")