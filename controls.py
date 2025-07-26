import tkinter as tk
from Widgets import CanvasButton, CanvasLabel, dial, slider

class speed_control:
    def __init__(self, master, canvas, width , height):
        self.master = master
        self.canvas = canvas
        self.width = width
        self.height = height
        self.dialx = width* 0.15
        self.dialy = height * 0.21
        self.value = 1 # variable to set the initial value
        self.dial_value = self.value + 89
        
        # To show the value 
        self.label = tk.Label(self.master, text=str(self.value) + "m/s",font = ('Comic Sans MS',13,'bold'),fg = 'black', bg='white')
        self.label.pack()

        self.dial_background = CanvasLabel(
            self.canvas,
            x = self.width * 0.15,
            y = self.height * 0.21,
            image_path = "@dial_background.png",
            posi = 's',
            width = 180
        )

        self.dial = dial(
            self.canvas,
            x = self.width * 0.15,
            y = self.height * 0.21,
            image_path = "@image_dial.png",
            angle = self.dial_value,
            width = 10
        )

        
        # Button that increase the value
        self.increase_button = CanvasButton(
            self.canvas,
            self.master.winfo_width() *0.24,
            self.master.winfo_height()* 0.17,
            image_path = '@image_plus.png',
            command = self.increase, 
            width = 30
        )
        #self.increase_button.pack()
        
        # Button that decrease the value 
        self.decrease_button = CanvasButton(
            self.canvas,
            self.master.winfo_width()* 0.06,
            self.master.winfo_height()* 0.17, 
            image_path = '@image_minus.png', 
            command = self.decrease, 
            width = 30
        )
        self.dial.bind('<B1-Motion>', self.control)

    def reset(self):
        self.value = 1
        self.dial_value = -(self.value*180/100) + 90
        self.label.config(text=str(self.value) + "m/s")
        self.dial.set_angle(self.dial_value)

    def control(self, event):
        if (event.x-self.dialx)+self.dialy > event.y:
            self.increase()
        elif event.y > (event.x-self.dialx)+self.dialy:
            self.decrease() 

    def increase(self):
        self.canvas.tag_raise('animation')
        if self.value == 100:# if self.value = 100 then ignore the button pressed
            pass
        else:
            self.value += 1
            self.dial_value = -(self.value*180/100) + 90
        self.label.config(text=str(self.value) + "m/s")
        self.dial.set_angle(self.dial_value)
    
    def decrease(self):
        self.canvas.tag_raise('animation')
        if self.value == 1:# if self.value = 1 then ignore the button pressed 
            pass
        else:
            self.value -= 1
            self.dial_value = -(self.value*180/100) + 90
        self.label.config(text=str(self.value) + "m/s")
        self.dial.set_angle(self.dial_value)

    def value(self):# function that return the value when needed
        return self.value
    
    def configure(self, x,y):
        self.dialx = x * 0.15
        self.dialy = y * 0.21
        self.increase_button.configure(x * 0.24, y * 0.17)
        self.decrease_button.configure(x * 0.06, y * 0.17)
        self.dial.configure(self.dialx,self.dialy)
        self.dial_background.configure(x * 0.15, y * 0.21)


class direction_control:
    def __init__(self, master, canvas, width , height, command):
        self.master = master
        self.canvas = canvas
        self.width = width
        self.height = height  
        self.compassx = width*0.15
        self.compassy = height*.41
        self.command = command
        self.value = 0 

        self.label = tk.Label(self.master, text = str(self.value) + "deg",font = ('Comic Sans MS',13,'bold'),fg = 'black', bg='white')
        self.label.pack()
        
        self.increase_button = CanvasButton(
            self.canvas,
            self.master.winfo_width() * 0.24,
            self.master.winfo_height()* 0.4,
            image_path = '@image_plus.png',
            command = self.increase, 
            width = 30
        )
        
        self.decrease_button = CanvasButton(
            self.canvas,
            self.master.winfo_width()* 0.06,
            self.master.winfo_height()* 0.4, 
            image_path = '@image_minus.png', 
            command = self.decrease, 
            width = 30
        )

        self.compass = dial(
            self.canvas,
            x = self.compassx,
            y = self.compassy,
            image_path = "@image_compass.png",
            angle = self.value,
            width = 55
        )

        self.compass.bind('<B1-Motion>', self.control)

    def reset(self):
        self.value = 0
        self.label.config(text=str(self.value) + "deg")
        self.compass.set_angle(self.value)

    def control(self, event):
        self.canvas.tag_raise('animation')
        if (event.x-self.compassx)+self.compassy > event.y:
            self.decrease()
        elif event.y > (event.x-self.compassx)+self.compassy:
            self.increase() 
    def increase(self):
        if self.value == 89:# if value = 89 ignore button pressed
            pass
        else:
            self.value += 1
        self.label.config(text = str(self.value) + "deg")
        self.compass.set_angle(-self.value)
        self.command.rotation(-self.value)
    def decrease(self):
        if self.value == -89:# if value = -89 ignore button pressed
            pass
        else:
            self.value -= 1 
        self.label.config(text = str(self.value) + "deg")
        self.compass.set_angle(-self.value)
        self.command.rotation(-self.value)
    
    

    def value(self):
        return self.value
    
    def configure(self, x,y):
        self.compassx = x*0.15
        self.compassy = y * 0.41
        self.increase_button.configure(x * 0.24, y * 0.4)
        self.decrease_button.configure(x * 0.06, y * 0.4)
        self.compass.configure(self.compassx, self.compassy)
    

class flow_control:
    def __init__(self, master, canvas, width , height):
        self.master = master
        self.canvas = canvas
        self.width = width
        self.height = height 
        self.labelx = width * 0.15
        self.labely = height * 0.575
        self.value = 0 

        self.label = tk.Label(self.master, text = str(self.value) + "m/s",anchor = 'c',font = ('Comic Sans MS',13,'bold'),fg = 'black', bg='white')
        self.label.place(x = self.labelx,y = self.labely, anchor='c')

        self.increase_button = CanvasButton(
            self.canvas,
            self.master.winfo_width() *0.96,
            self.master.winfo_height()*1,
            image_path = '@image_plus.png',
            command = self.increase, 
            width = 30
        )
        
        self.decrease_button = CanvasButton(
            self.canvas,
            self.master.winfo_width()* 0.24,
            self.master.winfo_height()* 1, 
            image_path = '@image_minus.png', 
            command = self.decrease, 
            width = 30
        )
        self.label.bind('<B1-Motion>', self.control)
    
    def reset(self):
        self.value = 0
        self.label.config(text=str(self.value) + "m/s")
        
    def control(self, event):
        label = event.widget
        x = label.winfo_x() + event.x
        y = label.winfo_y() + event.y
        if (x-self.labelx)+self.labely > y:
            self.increase()
        elif y > (x-self.labelx)+self.labely:
            self.decrease() 


    def increase(self):
        if self.value == 100:
            pass
        else:
            self.value += 1
        self.label.config(text = str(self.value) + "m/s")
    
    def decrease(self):
        if self.value == 0:
            pass
        else:
            self.value -= 1 
        self.label.config(text = str(self.value) + "m/s")

    def value(self):
        return self.value
    
    def configure(self, x,y):
        self.labelx = x * 0.15
        self.labely = y * 0.575
        self.increase_button.configure(x * 0.24, y * 0.58)
        self.decrease_button.configure(x * 0.06, y * 0.58)
        self.label.place_configure(x = self.labelx,y = self.labely)
    
class river_width_control:
    def __init__(self, master, canvas, width , height, command):
        self.master = master
        self.canvas = canvas
        self.width = width
        self.height = height 
        self.sliderx = self.width * .15
        self.slidery = self.height * .7
        self.value = 200
        self.command = command

        self.label = tk.Label(self.canvas, text = str(self.value) + "(m)",font = ('Comic Sans MS',13,'bold'),fg = 'black', bg='white')
        self.label.pack()

        self.increase_button = CanvasButton(
            self.canvas,
            self.width *0.24,
            self.height* 0.78,
            image_path = '@image_plus.png',
            command = self.increase, 
            width = 30
        )
        
        self.decrease_button = CanvasButton(
            self.canvas,
            self.width* 0.06,
            self.height* 0.78, 
            image_path = '@image_minus.png', 
            command = self.decrease, 
            width = 30
        )

        self.slider = slider(
            self.canvas,
            self.width * .15,
            self.height * .7,
            self.value/4 
        )

        self.slider.bind('<B1-Motion>', self.control)
    
    def reset(self):
        self.value = 200
        self.label.config(text=str(self.value) + "(m)")
        self.slider.set_range(self.value/4)

    def control(self, event):
        if (event.x-self.sliderx)+self.slidery > event.y:
            self.increase()
        elif event.y > (event.x-self.sliderx)+self.slidery:
            self.decrease() 

    def increase(self):
        if self.value == 400:
            pass
        else:
            self.value += 1
        self.label.config(text = str(self.value) + "(m)")
        self.slider.set_range((self.value)/4)
        self.command.update(self.value - 200)
        self.command.configure(self.x, self.y)

    
    def decrease(self):
        if self.value == 200:
            pass
        else:
            self.value -= 1 
        self.label.config(text = str(self.value) + "(m)")
        self.slider.set_range((self.value)/4)
        self.command.update(self.value - 200)
        self.command.configure(self.x, self.y)

    def value(self):
        return self.value

    def configure(self, x,y):
        self.x = x
        self.y = y
        self.sliderx = x * .15
        self.slidery = y * .7
        self.increase_button.configure(x * 0.24, y * 0.78)
        self.decrease_button.configure(x * 0.06, y * 0.78)
        self.slider.configure(self.sliderx, self.slidery)

    def config(self, size):
        self.label.config(font = ('Comic Sans MS',size,'bold'))

    



