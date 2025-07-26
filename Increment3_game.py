import tkinter as tk
from increment3_eq import equations
import controls
from random import randint
from tkinter import messagebox as mb
from Widgets import CanvasLabel, CanvasButton
from boat import boat 
from threading import Thread
import queue
from Waves import wave
from Riverbed import RiverBed
import os

class Window:
    def __init__(self, master):
        self.root = master
        self.root.geometry("800x500+0+0")
        self.root.title("Game")
        self.root.minsize(800,500)
        self.river_width = 200
        self.size = 0

    #setting up the ratio of the window
        self.root.aspect(
            self.root.winfo_screenwidth(),#width of user's screen
            self.root.winfo_screenheight(),#height of user's screen
            self.root.winfo_screenwidth(),
            self.root.winfo_screenheight()
        )

        self.canvas = tk.Canvas(
            self.root,
            height = self.root.winfo_height(),
            width = self.root.winfo_width(),
            bd = 0,
            highlightthickness=0,
            bg= 'white'
        )
        self.canvas.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        self.river = self.canvas.create_rectangle(self.root.winfo_width()*0.3,0,self.root.winfo_height(),self.root.winfo_width(), fill="#145DA0")

        self.riverbed = RiverBed(
            self.root,
            self.canvas,
            self.root.winfo_width(),
            0,
            165
        )
        self.canvas.lift(self.riverbed)
    #setting up controls 
        self.Width = 800
        self.Height = 500
        self.root.bind("<Configure>", self.update)

    # Labels of the challenge details(y-coor, width of river which is randomly set)
        self.challengewidth_label = tk.Label(self.root, font = ('Comic Sans MS',int(self.root.winfo_height() * 0.03),'bold'),fg = 'black', bg='#82bfe0')
        self.challengewidth_label.place(relx = .21, rely = .675, anchor = 's')
        self.challenge_label = tk.Label(self.root, font = ('Comic Sans MS',int(self.root.winfo_height() * 0.03),'bold'),fg = 'black', bg='#82bfe0')
        self.challenge_label.place(relx = .22, rely = .769, anchor = 'c')

        # self.label1 = tk.Label()
        # self.label1.place(relx  = 0.6, rely = 0.3, anchor = 'c')
        # self.label2 = tk.Label()
        # self.label2.place(relx = 0.6, rely = 0.4, anchor = 'c')
        # self.label3 = tk.Label()
        # self.label3.place(relx = 0.6, rely = 0.5, anchor = 'c')
    
        self.boat = boat(self.canvas, self.Width, self.Height, 80)

    # Speed of boat

        # tk.Label(text = 'Speed of Boat').place(relx = .15, rely = .15, anchor = 'c')
        # self.speed_of_boat = controls.speed_control(self.root)
        self.sobtitle = CanvasLabel(
            self.canvas,
            self.Width * 20,
            self.Height * 20,
            "@image_speed_of_boat.png", 
            width=200
        )
        self.speed_of_boat = controls.speed_control(
            self.root,
            self.canvas,
            self.Width,
            self.Height,
        )
        self.speed_of_boat.label.place(relx = .15, rely =.1, anchor = 'c')
        # self.speed_of_boat.increase_button.place(relx =.22, rely = .2, anchor = 'c')
        # self.speed_of_boat.decrease_button.place(relx =.08, rely = .2, anchor = 'c')
    
    # Direction of boat   
        # tk.Label(text = 'Direction of Boat').place(relx = .15, rely = .25, anchor = 'c')
        self.dobtitle = CanvasLabel(
            self.canvas,
            self.Width * 20,
            self.Height * 20,
            "@image_direction_of_boat.png", 
            width=200
        )
        self.direction_of_boat = controls.direction_control(self.root,
            self.canvas,
            self.Width,
            self.Height,
            self.boat
        )
        self.direction_of_boat.label.place(relx = .15, rely = .33, anchor = 'c')

    # Flow control 
        self.fstitle = CanvasLabel(
            self.canvas,
            self.Width * 20,
            self.Height * 20,
            "@image_flow_control.png", 
            width=200)
        
        self.flow_speed = controls.flow_control(
            self.root,
            self.canvas,
            self.Width,
            self.Height,
        )
        #self.flow_speed.label.place (relx = .15, rely = .575, anchor = 'c')
       
    # Back button
        self.back_button = CanvasButton(
            self.canvas,
            self.Width * 0.2,
            self.Height * 0.95,
            "@image_back.png",
            command=self.go_back,
            posi = 'ne',
            width = 100)
        #self.back_button = tk.Button(self.root, text="Back", command=self.go_back)
        #self.back_button.place(relx = 0, rely = 1, anchor = 'sw')

        self.eqn = equations(self.flow_speed.value,self.river_width,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)

        # Run button
        self.run_button = CanvasButton(
            self.canvas,
            self.Width * 0.2,
            self.Height * 0.95,
            "@image_run.png",
            command=self.run,
            posi = 'nw',
            width = 100)
        #self.run_button = tk.Button(self.root, text = 'Run', command= self.run )
        #self.run_button.place(relx = .09, rely = .5, anchor = 'c')

        # Challenge button that randomly generates river width and y-coor values
        self.challenge_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.91,
            "@image_challenge.png",
            command=self.challenge,
            width = 200)
        
        # Help page
        self.help_page_button = CanvasButton(
            self.canvas,
            self.Width * 0.8,
            self.Height * 0.8,
            "@image_help_page.png",
            command=self.show_help_page,
            width = 50)
        
        # Equation page
        self.equation_page_button = CanvasButton(
            self.canvas,
            self.Width * 0.8,
            self.Height * 0.8,
            "@image_equation_page.png",
            command=self.show_equation_page,
            width = 50)
        
        self.wfr = CanvasLabel(
            self.canvas,
            x = self.Width * 0.1,
            y = self.Height * 0.1,
            image_path = "@image_wfr_game.png",
            posi = 'c',
            width = 200
        )

        self.y_co = CanvasLabel(
            self.canvas,
            x = self.Width * 0.1,
            y = self.Height * 0.1,
            image_path = "@image_y_co_game.png",
            posi = 'c',
            width = 200
        )

        self.reset_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.89,
            "@image_reset.png",
            command=self.reset,
            width = 200)
        
        self.q = queue.Queue()
        self.q2 = queue.Queue()
        self.thread_waves = Thread(target = self.allwaves, args=(self.q,))
        # self.thread_waves.daemon = True
        self.thread_waves.start()


        self.thread_riverbed = Thread(target = self.riverbed._resize_image, args = (self.root,))
        self.thread_riverbed.start()

        self.q.put(0)
        self.root.mainloop()
    


    def allwaves(self, queue):
        while True:
            queues = queue.get()
            print("q=",queues)
            try:
                self.temp = self.eqn1.challenge_check(self.challenge_point)
                print(self.temp)
                
            except AttributeError:
                pass
            if queues == 0:
                queue.put(2)
                print('createwave')
                self.waves = wave(self.canvas, self.Width, self.Height, 300)
                queue.task_done()
            elif queues == 1:
                if flow > 0:
                    queue.put(1)
                    print('wavemotion')
                    self.waves.start(flow)
                    print('startmove')
                    self.boat.move(self.eqn1, self.q, self.q2)
                    #queue.task_done()
                else:
                    self.boat.move(self.eqn1, self.q, self.q2)
                    queue.put(1)
                    queue.task_done() 
            else:
                flow = self.flow_speed.value
                try:
                    if self.temp:
                        mb.showinfo("Congratulation", "Great")# show a messagebox when get the value required to pass the game
                except AttributeError:
                    pass
                with queue.mutex:
                    queue.queue.clear()

    #update the width and height data of the window and re
    def update(self, event):
        self.Width = self.root.winfo_width()
        self.Height = self.root.winfo_height()
        
        self.speed_of_boat.configure(self.Width, self.Height)
        self.direction_of_boat.configure(self.Width, self.Height)
        self.flow_speed.configure(self.Width,self.Height)

        self.run_button.configure(self.Width * 0.15, self.Height * 0.932)
        self.challenge_button.configure(self.Width * 0.15, self.Height * 0.85)
        self.back_button.configure(self.Width * 0.15, self.Height * 0.932)
        self.help_page_button.configure(self.Width * 0.965, self.Height * 0.05)
        self.equation_page_button.configure(self.Width * 0.965, self.Height * 0.92)
        self.boat.configure(self.Width, self.Height, self.river_width)
        self.canvas.coords(self.river, self.Width * 0.3,0, self.Width, self.Height)
        self.reset_button.configure(self.Width * 0.152, self.Height * 0.905)
        self.riverbed.configure(self.Width, self.Height)
        size = int(self.Width * 0.25)
        if size <= 300:
            self.size = size
            print(size)
        elif self.Width == self.root.winfo_screenwidth():
            print('larged')
            self.size = 300
        else:
            pass
        self.sobtitle.configure(self.Width * 0.15, self.Height * 0.05, width = self.size)
        self.dobtitle.configure(self.Width * 0.15, self.Height * 0.28, width = self.size)
        self.fstitle.configure(self.Width * 0.15, self.Height * 0.5, width = self.size)
        self.wfr.configure(x = self.Width * 0.155,y = self.Height * 0.65, width = self.size)
        self.y_co.configure(self.Width * 0.155, self.Height * 0.75, width = self.size)
        self.challengewidth_label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        self.challenge_label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        self.speed_of_boat.label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        self.direction_of_boat.label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        self.flow_speed.label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        
        try:
            self.challenge_boat.configure(self.eqn.horizontal_distance(self.Width), self.challenge_point)
        except AttributeError:
            pass
        try:
            self.waves.configure(self.Width,self.Height)
        except AttributeError:
            pass

    #randomly generates value within range and show up in window 
    def challenge(self):
        self.river_width = randint(200, 350)
        self.temp = False
        self.challenge_point = randint(0,500)
        self.riverbed.update(self.river_width - 200)
        self.eqn = equations(self.flow_speed.value,self.river_width,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
        self.eqn.actual_velocity()
        self.eqn.actual_angle()
        self.eqn.time()
        self.eqn.vertical_distance()
       
        self.challengewidth_label.config(text = str(self.river_width))
        self.challenge_label.config(text = str(self.challenge_point))
        print(self.eqn.horizontal_distance(self.Width))
        self.challenge_boat = CanvasLabel(
            self.canvas,
            self.eqn.horizontal_distance(self.Width),
            self.challenge_point,
            "@image_transparent_boat.png",
            width = 80,
            tag = 'buttons'
        )

    def go_back(self):
        self.root.destroy()
        os.system('python Increment3_homepage.py')
    
    #similar to simulation but checks if the value challenge is succeeded
    def run(self):
        self.update(None)
        try:
            self.arrow.remove()
        except AttributeError:
            pass

        self.eqn1 = equations(self.flow_speed.value,self.river_width,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
        # self.label1.config(text = "Actual velocity(m/s): " + str(round(self.eqn.actual_velocity(),2)))
        # self.label2.config(text = "Actual angle(deg): " + str(round(self.eqn.actual_angle(),2)))
        # self.label3.config(text = "Time(s): " + str(round(self.eqn.time(),2)))
        self.eqn1.actual_velocity()
        self.eqn1.actual_angle()
        self.eqn1.time()
        self.eqn1.vertical_distance()
        print('hi')
        from vectors_arrow import arrow
        self.eqn1.actual_velocity()
        self.eqn1.actual_angle()
        self.eqn1.time()
        self.arrow = arrow(self.canvas,self.Width*0.5, self.Height*0.5, self.eqn1.horizontal_distance(self.Width), self.eqn1.vertical_distance(), self.flow_speed.value,self.Height)
        
        self.q.put(1)
        self.q2.put(1)
        print('pressed')
        print('config')

    # Show help page 
    def show_help_page(self):
        
        # self.root.destroy() 
        os.system('python Increment3_help_page.py')
       

    # Show equation page 
    def show_equation_page(self):
        
        # self.root.destroy() 
        from increment3_equpage_game import EquationPage
        try:
            EquationPage(self.eqn, self.flow_speed.value,self.direction_of_boat.value, self.speed_of_boat.value,self.river_width, self.challenge_point, self.temp)
        except AttributeError:
            mb.showerror("missing value", "it did not run properly")

    def reset(self):
        self.speed_of_boat.reset()
        self.direction_of_boat.reset()
        self.flow_speed.reset()
        self.boat.reset()
        self.q.put(3)
        self.arrow.remove()

if __name__ == "__main__":
    window = Window(tk.Tk())
    
    
