class Ball:
    def __init__(self,canvas,x,y,diameter,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x-diameter,y-diameter,x+diameter,y+diameter,fill=color)