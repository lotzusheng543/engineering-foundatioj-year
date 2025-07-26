from tkinter import *
from PIL import Image, ImageTk
from threading import Thread



class wave:
    def __init__(self, canvas, x,y, width = None, height = None):
        
        self.canvas = canvas
        # Load the wave image and create a PhotoImage object
        self.wave_image = Image.open("@image_wave.png")

        # Resize image if width or height is provided
        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / self.wave_image.size[1] * self.wave_image.size[0])
            if height is None:
                height = int(float(width) / self.wave_image.size[0] * self.wave_image.size[1])
            self.wave_image = self.wave_image.resize((width, height), Image.Resampling.LANCZOS)
        
        self.wave_image = self.wave_image.resize((width, height), Image.Resampling.LANCZOS)
        self.wave_photo = ImageTk.PhotoImage(self.wave_image)
        

        self.width = x
        self.height = y

        # self.waves = []
        # Create an image object for the wave image at the coordinates of each star
        self.wave1 = self.canvas.create_image(self.width * 0.65, (self.height + 100) * 0, image=self.wave_photo)
        self.wave2 = self.canvas.create_image(self.width * 0.69, (self.height + 100) * 0.25, image=self.wave_photo)
        self.wave3 = self.canvas.create_image(self.width * 0.65, (self.height +100) * 0.5, image=self.wave_photo)
        self.wave4 = self.canvas.create_image(self.width * 0.69, (self.height + 100) * 0.75, image=self.wave_photo)

        # self.waves.append(self.wave1)
        # self.waves.append(self.wave2)
        # self.waves.append(self.wave3)


    def start(self, flow_speed):
        self.flow_speed = flow_speed
        print('waves')
        # while True:
        
        x, y = self.canvas.coords(self.wave1)
        x1,y1 = self.canvas.coords(self.wave2)
        x2,y2 = self.canvas.coords(self.wave3)
        x3,y3 = self.canvas.coords(self.wave4)
        #self.canvas.delete(self.wave1)
        if y >= self.height + 50:
            self.canvas.delete(self.wave1)
            self.wave1 = self.canvas.create_image(self.width * 0.65, -70, image = self.wave_photo)
            #self.canvas.tag_lower(self.wave1)
        elif y1 >= self.height + 50:
            self.canvas.delete(self.wave2)
            self.wave2 = self.canvas.create_image(self.width * 0.69, -70, image = self.wave_photo)
        elif y2 >= self.height + 50:
            self.canvas.delete(self.wave3)
            self.wave3 = self.canvas.create_image(self.width * 0.65, -70, image = self.wave_photo)
        elif y3 >= self.height + 50:
            self.canvas.delete(self.wave4)
            self.wave4 = self.canvas.create_image(self.width * 0.69, -70, image = self.wave_photo)
        else:
            self.canvas.move(self.wave1,0,0.95)
            self.canvas.move(self.wave2,0,0.95)
            self.canvas.move(self.wave3,0,0.95)
            self.canvas.move(self.wave4,0,0.95)
        #print("coords",y," windowheight:", self.height)

        # Schedule the `start()` function to be called again after 50 milliseconds
        self.canvas.after(-self.flow_speed + 100)
        print('endofwave')


        # self.start(self.time, self.flow_speed)


    def configure(self, x, y):
        self.width = x 
        self.height = y 
        self.canvas.coords(self.wave1, self.width * 0.65, (self.height + 100) * 0)
        self.canvas.coords(self.wave2, self.width * 0.7, (self.height + 100) * 0.25)
        self.canvas.coords(self.wave3, self.width * 0.65, (self.height + 100) * 0.5)
        self.canvas.coords(self.wave4, self.width * 0.7, (self.height + 100) * 0.75)
        #self.canvas.tag_lower(self.wave1)
    
    def ret(self):
        return self.wave1



# while True:
#     self.canvas.delete(self.wave1)
#     x, y = self.canvas.coords(self.wave1)
    
#     if y == self.width:
#         self.wave1 = self.canvas.create_image(self.width * 0.5, self.height * 0, image = self.wave_photo)
#     else:
#         self.wave1 = self.canvas.create_image(self.width * 0.5, y + 5)
