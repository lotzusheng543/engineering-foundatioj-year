from tkinter import *
import gc
from Widgets import CanvasLabel, CanvasButton
from controls import *
from Increment3_simulation import*
import sys
from increment3_eq import equations

class EquationPage:
    def __init__(self, flow_speed, direction_of_boat, speed_of_boat, river_width, height):
        self.root = tk.Tk()
        self.root.geometry("800x500+20+50")
        self.root.title("Equation Page")
        self.root.resizable(False,False)

        self.root.aspect(
            self.root.winfo_screenwidth(),#width of user's screen
            self.root.winfo_screenheight(),#height of user's screen
            self.root.winfo_screenwidth(),
            self.root.winfo_screenheight())
        
        self.Width = 800
        self.Height = 500

        self.canvas = tk.Canvas(
            self.root,
            height = self.root.winfo_height(),
            width = self.root.winfo_width(),
            bd = 0,
            highlightthickness=0,
            bg= 'white')
        self.canvas.place(x = 0, y = 0, relheight = 1, relwidth = 1)

        # Different input values 
        
        self.flow_speed = flow_speed
        self.direction_of_boat = direction_of_boat 
        self.speed_of_boat = speed_of_boat 
        self.river_width = river_width
        self.command = equations(self.flow_speed,self.river_width,self.speed_of_boat, self.direction_of_boat, height)
        self.r_flowspeed = tk.Label(self.canvas, text=f"= [{self.flow_speed}\u00B2 +", font=('DM Sans', 16, 'bold'), fg='black', bg='#bdc5e6')
        self.r_flowspeed.place(relx = .2, rely = .26)
        self.r_boatspeed = tk.Label(self.canvas, text =f"{self.speed_of_boat}\u00B2", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.r_boatspeed.place(relx = .3, rely = .26)
        self.r_flowspeed2 = tk.Label(self.canvas, text=f"-2*{self.flow_speed}", font=('DM Sans', 16, 'bold'), fg='black', bg='#bdc5e6')
        self.r_flowspeed2.place(relx = .36, rely = .26)
        self.r_boatspeed2 = tk.Label(self.canvas, text =f"*{self.speed_of_boat}", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.r_boatspeed2.place(relx = .44, rely = .26)
        self.r_direction_of_boat = tk.Label(self.canvas, text =f"*cos(90\u00B0 + {round(self.direction_of_boat,4)}\u00B0)]\xb9\u2044 \xb2", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.r_direction_of_boat.place(relx = .22, rely = .308)
        self.r_resultant_speed = tk.Label(self.canvas, text =f"{round(self.command.actual_velocity(),2)}", font = ('DM Sans',23,'bold'),fg = 'black', bg='#f4f4f4')
        self.r_resultant_speed.place(relx = .68, rely = .255)
        self.a_direction_of_boat = tk.Label(self.canvas, text=f"= sin\u207B\u00B9[sin(90\u00B0 + {self.direction_of_boat}\u00B0)", font=('DM Sans', 16, 'bold'), fg='black', bg='#bdc5e6')
        self.a_direction_of_boat.place(relx = .2, rely = .49)
        self.a_boatspeed = tk.Label(self.canvas, text =f"*{self.speed_of_boat}", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.a_boatspeed.place(relx = .45, rely = .49)
        self.a_resultant_speed = tk.Label(self.canvas, text =f"/{round(self.command.actual_velocity(),2)}]", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.a_resultant_speed.place(relx = .52, rely = .49)
        self.a_actual_angle = tk.Label(self.canvas, text=f"{round(self.command.actual_angle(),2)}", font=('DM Sans', 23, 'bold'), fg='black', bg='#f4f4f4')
        self.a_actual_angle.place(relx = .67, rely = .46)
        self.t_river_width = tk.Label(self.canvas, text =f"= {self.river_width}/", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.t_river_width.place(relx = .2, rely = .695)
        self.t_resultant_speed = tk.Label(self.canvas, text =f"({round(self.command.actual_velocity(),2)}*", font = ('DM Sans',16,'bold'),fg = 'black', bg='#bdc5e6')
        self.t_resultant_speed.place(relx = .28, rely = .695)
        self.t_actual_angle = tk.Label(self.canvas, text=f"sin{round(self.command.actual_angle(),2)})", font=('DM Sans', 16, 'bold'), fg='black', bg='#bdc5e6')
        self.t_actual_angle.place(relx = .38, rely = .695)
        self.t_time = tk.Label(self.canvas, text =f"{round(self.command.time(),2)}", font = ('DM Sans',23,'bold'),fg = 'black', bg='#f4f4f4')
        self.t_time.place(relx = .68, rely = .662)
        
        # Back button
        self.back_button = CanvasButton(
            self.canvas,
            self.Width * 0.08,
            self.Height * 0.8,
            "@image_back.png",
            command=self.go_back,
            width=100)
        self.back_button.configure(x=self.Width * 0.2, y=self.Height * 0.95)

        self.equ = CanvasLabel(
            self.canvas,
            self.Width * 0.5,
            self.Height * 0.5,
            "@image_equ_slide_simu.png", 
            width=550)
        self.equ.configure(x=self.Width * 0.5, y=self.Height * 0.5)
        
        self.root.bind("<Configure>", self.update)
        self.root.mainloop()

    def update(self, event):
        self.Width = self.root.winfo_width()
        self.Height = self.root.winfo_height()
        self.back_button.configure(x=self.Width * 0.21, y=self.Height * 0.93)
        self.equ.configure(x=self.Width * 0.5, y=self.Height * 0.45)

    def go_back(self):
        gc.collect()
        self.root.destroy()

if __name__ == '__main__':
    height = int(sys.argv[5])
    flow_speed = int(sys.argv[1])
    direction_of_boat = int(sys.argv[2])
    speed_of_boat = int(sys.argv[3])
    river_width = int(sys.argv[4])
    EquationPage(flow_speed, direction_of_boat, speed_of_boat, river_width, height)