class Shape:
    def __init__(self,canvas):
        self.canvas = canvas
    def change_canvas(self,canvas):
        self.canvas = canvas
    def draw_oval(self,x,y,diameter,color):
        self.canvas.create_oval(x-diameter,y-diameter,x+diameter,y+diameter,fill=color)
    def draw_square(self,x,y,side_len,color):
        self.canvas.create_rectangle(x-side_len/2,y-side_len/2,x+side_len/2,y+side_len/2,fill=color)