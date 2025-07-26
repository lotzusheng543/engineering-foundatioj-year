import tkinter as tk


class arrow:
    def __init__(self, canvas, startx,starty, endx,endy, value, winysize):
        self.canvas = canvas
        self.canvas.delete("vectors")
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.value = value
        self.winysize = winysize
        self.resultant_line = self.canvas.create_line(startx,starty, endx,endy,fill='white',tags= 'vectors')
        self.y_line1 = self.canvas.create_line(startx,starty,startx, starty + value * winysize/500, fill='white',tags='vectors')
        self.y_line2 = self.canvas.create_line(endx,endy,endx,endy - value * winysize/250, fill='white',tags= 'vectors')
        self.boat_speed1 = self.canvas.create_line(startx, starty + value * winysize/250,endx,endy, fill='white',tags= 'vectors')
        self.boat_speed2 = self.canvas.create_line(startx,starty,endx,endy - value * winysize/250, fill='white',tags= 'vectors')

    def configure(self,endx, endy,value, winysize):
        self.value = value
        self.canvas.coords(self.resultant_line, self.startx,self.starty , endx,endy)
        self.canvas.coords(self.y_line1, self.startx,self.starty,self.startx,self.starty + self.value* winysize/250)
        self.canvas.coords(self.y_line2,endx, endy, endx,endy - self.value * winysize/250)
        self.canvas.coords(self.boat_speed1, self.startx, self.starty + self.value * winysize/250, endx, endy )
        self.canvas.coords(self.boat_speed2,self.startx,self.starty,endx, endy - self.value * winysize/250)


    def remove(self):
        self.canvas.delete("vectors")
    
    def show(self, startx,starty, endx,endy, value, winysize):
        #self.canvas.delete("vectors")
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.value = value
        self.winysize = winysize
        self.canvas.coords(self.resultant_line, self.startx,self.starty , endx,endy)
        self.canvas.coords(self.y_line1, self.startx,self.starty,self.startx,self.starty + self.value* winysize/250)
        self.canvas.coords(self.y_line2,endx, endy, endx,endy - self.value * winysize/250)
        self.canvas.coords(self.boat_speed1, self.startx, self.starty + self.value * winysize/250, endx, endy )
        self.canvas.coords(self.boat_speed2,self.startx,self.starty,endx, endy - self.value * winysize/250)


