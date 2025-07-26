from tkinter import*
from PIL import ImageTk, Image

class RiverBed:
    def __init__(self,master, canvas,x,y, width = None, height = None):
        self.canvas = canvas
        self.master = master 
        self.posi = 0

        self.left_river_bed = Image.open("@image_left_river.png")
        self.leftriver_copy = self.left_river_bed.copy()
        self.right_river_bed = Image.open("@image_big_size_trees.png")
        self.rightriver_copy = self.right_river_bed.copy()

    
        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / self.left_river_bed.size[1] * self.left_river_bed.size[0])
            if height is None:
                height = int(float(width) / self.left_river_bed.size[0] * self.left_river_bed.size[1])
            self.left_river_bed = self.left_river_bed.resize((width, height), Image.Resampling.LANCZOS)
            self.right_river_bed = self.right_river_bed.resize((width,height), Image.Resampling.LANCZOS)
            self.width = width
            self.height = height

        self.left_river_bed_image = ImageTk.PhotoImage(self.left_river_bed)
        self.right_river_bed_image = ImageTk.PhotoImage(self.right_river_bed)

        self.background1 = self.canvas.create_image(x* 0.3,y, anchor = 'nw', image = self.left_river_bed_image)
        self.background2 = self.canvas.create_image(x,y,anchor = 'ne', image = self.right_river_bed_image)

    def configure(self, x, y):
        self.canvas.coords(self.background1, x * 0.3,y*0)
        self.canvas.coords(self.background2, x * 1. + self.posi , y*0)
        self.canvas.tag_raise(self.background1)
        self.canvas.tag_raise(self.background2)
        self.canvas.tag_raise("vectors")
        self.canvas.tag_raise("animation")

    def update(self, posi):
        self.canvas.tag_raise("vectors")
        self.canvas.tag_raise("animation")
        self.posi = posi

         #Resize the background image to the current window size
    def _resize_image(self, master ):
        while True:
            self.canvas.tag_raise("buttons")
            self.canvas.tag_raise("vectors")
            self.canvas.tag_raise('animation')
            x = master.winfo_width()
            y = master.winfo_height()
            left_river = self.leftriver_copy.resize((int(x*0.2), int(y)))
            right_river = self.rightriver_copy.resize((int(x*0.2),int(y)))
            left_river_bed_image = ImageTk.PhotoImage(left_river)
            right_river_bed_image = ImageTk.PhotoImage(right_river)
            self.canvas.itemconfig(self.background1, image=left_river_bed_image)
            self.canvas.itemconfig(self.background2, image=right_river_bed_image)
            self.left_river_bed_image = left_river_bed_image
            self.right_river_bed_image = right_river_bed_image


   
    def reset(self):
        self.posi = 0
        self.canvas.coords(self.background1, self.master.winfo_width() * 0.3, 0)
        self.canvas.coords(self.background2, self.master.winfo_width(), 0)
        
        # self.canvas.coords(self.background2, 0, 165)
        # self.canvas.coords(self.background2, self.posi, 200)
