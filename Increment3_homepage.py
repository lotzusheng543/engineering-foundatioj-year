import tkinter as tk
from PIL import ImageTk
from Homepage_Background import Image_crop
from threading import Thread
from Widgets import CanvasButton, CanvasLabel
import os 
# %%
from fractions import Fraction


class Homepage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x500+0+0")# 800 is the width of the window, 500 is the height of the window and 0s are the position of the window
        self.master.title('Homepage')
        self.master.minsize(800, 500)# setting the min size the window can be resized to

        #setting up the ratio of the window
        self.master.aspect(
            self.master.winfo_screenwidth(),#width of user's screen
            self.master.winfo_screenheight(),#height of user's screen
            self.master.winfo_screenwidth(),
            self.master.winfo_screenheight()
        )
        
        
        #Background Image section
        self.image = Image_crop(self.master, "@image_homepage_background.png").ret()# Using the Image crop to crop the background image to screen's aspect ratio size 
        self.image_copy = self.image.copy() # copy the image to a variable
        self.background_image = ImageTk.PhotoImage(self.image)

        #create canvas for background
        self.canvas = tk.Canvas(
            self.master,
            height=self.master.winfo_height(),
            width=self.master.winfo_width(),
            bd=0,
            highlightthickness=0,
        )
        self.background = self.canvas.create_image(0, 0,anchor = 'nw', image=self.background_image)
        self.canvas.place(x=0, y=0, relheight=1, relwidth=1)


        #setting the resizing of background image
        #start thread for image resizing (using another thread of the cpu to run this process so the process is smoother)
        self.thread = Thread(target=self._resize_image, args=(self.master,))
        self.thread.daemon = True
        self.thread.start()

        
        #Setting up the Contents
                
        #setting up the resizing of the button
        self.Width = 800 #setting window width default value
        self.Height = 500 #setting window height default value
        self.master.bind("<Configure>", self.update) #When window is adjusted do self.update

        #Setting up the label for title
        self.title = CanvasLabel(
            self.canvas,
            self.Width * 0.5,
            self.Height * 0.2,
            "@image_river_boat.png", 
            width=500)
        
        #simulation button
        self.simu = CanvasButton(
            self.canvas,
            self.Width * 0.5,
            self.Height * 0.4,
            "@image_simulation.png", 
            command=self.simulation,
            width=300,
        )

        #StartGame button
        self.chall = CanvasButton(
            self.canvas,
            self.Width * 0.5,
            self.Height * 0.6,
            "@image_startGame.png",
            command=self.game,
            width = 300
        )

        #Theory button
        self.the = CanvasButton(
            self.canvas,
            self.Width * 0.5,
            self.Height * 0.8,
            "@image_equations.png",
            command = self.theory,
            width = 300
        )

        self.master.mainloop()

    def show_win(self):
        print('1')
        self.master.deinconcify()

    #update the width and height data of the window and re
    def update(self, event):
        self.Width = self.master.winfo_width()
        self.Height = self.master.winfo_height()
        self.simu.configure(x = self.Width * 0.5, y = self.Height * 0.4)
        self.chall.configure(x = self.Width * 0.5, y = self.Height * 0.6)
        self.the.configure(x = self.Width * 0.5, y = self.Height * 0.8)
        self.title.configure(x = self.Width * 0.5, y = self.Height * 0.2)

    #Resize the background image to the current window size
    def _resize_image(self, master):
        while True:
            new_width = master.winfo_width()
            new_height = master.winfo_height()
            image = self.image_copy.resize((new_width, new_height))
            background_image = ImageTk.PhotoImage(image)
            self.canvas.itemconfig(self.background, image=background_image)
            self.background_image = background_image

    # THe functons to respective pages 
    def simulation(self):
        self.master.destroy()
        os.system('python Increment3_simulation.py')

    def game(self):
        self.master.destroy()
        os.system('python Increment3_game.py')

    def theory(self):
        self.master.destroy()
        os.system('python Increment3_home_equpage.py')

if __name__ == "__main__":

    app = Homepage(tk.Tk())
