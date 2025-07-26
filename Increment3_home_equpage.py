from threading import Thread
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Widgets import CanvasButton
import gc



class EquationPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500+20+50")
        self.root.title("Equation Page")
        # self.root.resizable(False,False)
        self.root.minsize(800,500)
        self.root.maxsize(800,500)

        # create a canvas widget and add a scrollbar to it
        self.canvas = tk.Canvas(self.root, borderwidth=0, background="#ffffff")
        self.scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # add the scrollbar to the canvas
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.Width = 800
        self.Height = 500

        # Back button
        self.back_button = CanvasButton(
            self.canvas,
            self.Width * 0.08,
            self.Height * 0.8,
            "@image_back.png",
            command=self.go_back,
            width=100
        )
        self.back_button.configure(x=self.Width * 0.2, y=self.Height * 0.95)
       
        # add the pictures to the scrollable area
        for i in range(3):
            # load the image
            image = Image.open(f"@image_equa{i+1}.png")
            # resize the image to fit in the scrollable area
            width, height = image.size
            ratio = height / width
            new_height = 400
            new_width = int(new_height / ratio)
            image = image.resize((new_width, new_height))
            # create a photo object from the image
            photo = ImageTk.PhotoImage(image)
            # create a label widget to display the photo
            label = tk.Label(self.scrollable_frame, image=photo)
            label.image = photo # save a reference to the photo to prevent it from being garbage collected
            label.pack(side="left", padx=5, pady=5)

        # add the scrollable frame to the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # configure the scrollable frame to resize with the canvas
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # bind update function to window resize event
        self.root.bind("<Configure>", self.update)

        self.root.mainloop()

    def update(self, event):
        self.Width = self.root.winfo_width()
        self.Height = self.root.winfo_height()
        self.back_button.configure(x=self.Width * 0.065, y=self.Height * 0.93)

    def go_back(self):
        gc.collect()
        from Increment3_homepage import Homepage
        self.root.destroy()
        Homepage(tk.Tk())

if __name__ == "__main__":
    gc.collect()
    window = EquationPage()
