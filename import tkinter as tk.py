from tkinter import*
from PIL import Image, ImageTk
from tkinter.constants import *
from time import sleep
from Widgets import CanvasButton, CanvasLabel



x,y = 20,250
vx,vy = 40,-30

mainwindow=Tk()
canvas = Canvas(width=1600, height=1000, bg='white')
canvas.pack(expand=YES, fill=BOTH)
Img_wave = Image.open('@image_wave.png')
Img = Image.open("@image_river_background.png")


lmg2 = CanvasLabel(canvas,x=800,y=300, image_path = '@image_river_background.png',width=700)
label_wave1 = CanvasLabel(canvas,x=800,y=400, image_path='@image_wave.png',width=350)
label_wave2 = CanvasLabel(canvas,x=800,y=175, image_path='@image_wave.png',width=350)

def start():
    global canvas,x,y,vx,vy
    while True:
        #label_boat = CanvasLabel(canvas,x=30,y=20, image_path='@image_boat.png',width=50)
        canvas.after(70)
        #canvas.delete(label_boat)

        x=x+vx
        y=y+vy
        print(x, y)

        canvas.delete(label_wave1,x,y)
        canvas.delete(label_wave2,x,y)
        canvas.update()
       
        if x>=4000 or y>=2500:
            break

startbutton=Button(mainwindow,text='start',command=start)
startbutton.place(relx = 0.5, rely = 0.8, anchor=NE)


mainwindow.mainloop()





# import tkinter as tk
# from PIL import Image, ImageTk

# # Open the GIF image
# with Image.open('animated_image.gif') as gif_image:
#     # Create a list of individual frames from the GIF image
#     frames = []
#     try:
#         while True:
#             frames.append(gif_image.copy())
#             gif_image.seek(len(frames))  # skip to next frame
#     except EOFError:
#         pass

# # Create a Tkinter window
# root = tk.Tk()

# # Create a Label widget to display the GIF image
# label = tk.Label(root)
# label.pack()

# # Define a function to update the displayed image
# def update(frame_number):
#     # Get the current frame from the list of frames
#     frame = frames[frame_number % len(frames)]
#     # Convert the frame to a PhotoImage object and set it as the label's image
#     image = ImageTk.PhotoImage(frame)
#     label.config(image=image)
#     # Schedule the next update after a delay of 50 milliseconds
#     root.after(50, update, frame_number + 1)

# # Start the animation by calling the update function with frame number 0
# update(0)

# # Run the Tkinter event loop
# root.mainloop()

