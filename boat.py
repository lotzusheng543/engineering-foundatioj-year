
from PIL import Image, ImageTk 
import math

class boat:
    def __init__(self,canvas, x, y , width = None, height = None):
        self.canvas = canvas
        self.boat_img = Image.open('@image_boat.png')
        self.startx = x
        self.starty = y
        # Resize image if width or height is provided
        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / self.boat_img.size[1] * self.boat_img.size[0])
            if height is None:
                height = int(float(width) / self.boat_img.size[0] * self.boat_img.size[1])
            self.width = width
            self.height = height
            self.boat_img = self.boat_img.resize((self.width, self.height), Image.Resampling.LANCZOS)
            self.boat_img_copy = self.boat_img.copy()
        self.boat = ImageTk.PhotoImage(self.boat_img)

        self.boat_act = self.canvas.create_image(x, y , anchor = 'c', image = self.boat, tag = 'animation')


    def rotation (self, rotate):
        boat_img = Image.open('@image_boat.png')
        boat_img = boat_img.resize((self.width,self.height), Image.Resampling.LANCZOS)
        boat_img = boat_img.rotate(rotate, expand = False)

        self.boat = ImageTk.PhotoImage(boat_img)

        self.canvas.itemconfig(self.boat_act, image = self.boat)

    def move(self, command, queue, queue2):
        self.canvas.tag_raise('animation')
        self.canvas.tag_raise("vectors")
        print('hello')
        self.command = command
        print('command')
        queues2 = queue2.get()
        print('move')
        self.end_x = self.command.horizontal_distance(self.widthposi)
        if  self.x >= self.end_x:
            print("boatx: ",self.x)
            print("endingx: ",self.end_x)

            queue.put(2)
            queue2.queue.clear()
            #print('hi')
            queue2.put(0)

        elif queues2 == 1:
            self.vx = 5
            #self.command.actual_velocity() * math.sin(math.radians(self.command.actual_angle()))
            #end point~start point= s

            self.end_y = self.command.vertical_distance() 
            #self.command.actual_velocity() * math.cos(math.radians(self.command.actual_angle()))
            self.gradient = -(self.end_y - self.starty)/(self.end_x- self.startx)
            self.vy = self.gradient
            
            self.x = self.x + self.vx
            self.y = self.y - self.vy*self.vx
            print("boatxcoor: ",self.x,"boatycoor: ", self.y)
            self.canvas.coords(self.boat_act,self.x,self.y)
            self.canvas.update()
            self.canvas.after(10)
            queue2.put(1)

    def reset(self):
        # Reset the boat's rotation
        self.rotation(0)

        # Move the boat back to its original position
        self.canvas.coords(self.boat_act, self.startx, self.starty)

        # Reset the boat's image to the original unrotated image
        self.boat = ImageTk.PhotoImage(self.boat_img)
        self.canvas.itemconfig(self.boat_act, image=self.boat)

    def configure(self, x, y, command1):
        self.command1 = command1
        self.startx = x * 0.5
        self.starty = y * 0.5
        self.x = x * 0.5
        self.y = y * 0.5
        self.widthposi = x
        try:
            self.end_x = self.command.horizontal_distance(x)
            print("endingx: ", self.end_x)
        except AttributeError:
            pass

        self.canvas.coords(self.boat_act, self.startx,self.starty)

   
