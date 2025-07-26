import tkinter as tk
from increment3_eq import equations
import controls
from Widgets import CanvasLabel, CanvasButton
from Riverbed import RiverBed
from threading import Thread, Event
import queue
from Waves import wave
from boat import boat 
import os
from vectors_arrow import arrow

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500+0+0")
        self.root.title("Simulation")
        self.root.minsize(800,500)
        self.flag = True
        # Setting up the ratio of the window
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

        # Setting up controls 
        self.Width = 800
        self.Height = 500
        self.root.bind("<Configure>", self.update)
    
        self.boat = boat(self.canvas, self.Width, self.Height, 80)

    # Speed of boat's controls setup 
        #tk.Label(text = 'Speed of Boat').place(relx = .15, rely = .05, anchor = 'c')
        self.sobtitle = CanvasLabel(
            self.canvas,
            self.Width * 20,
            self.Height * 20,
            "@image_speed_of_boat.png", 
            width=200)
        self.speed_of_boat = controls.speed_control(self.root,
            self.canvas,
            self.Width,
            self.Height,
        )
        self.speed_of_boat.label.place(relx = .15, rely =.1, anchor = 'c')

    # Direction of boat's control setup
        self.dobtitle = CanvasLabel(
            self.canvas,
            self.Width * 20,
            self.Height * 20,
            "@image_direction_of_boat.png", 
            width=200)
        self.direction_of_boat = controls.direction_control(self.root,
            self.canvas,
            self.Width,
            self.Height,
            self.boat
        )
        self.direction_of_boat.label.place(relx = .15, rely =.33, anchor = 'c')

    # River flow speed's control setup 
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


    # River width's control setup 
        self.rwtitle = CanvasLabel(
            self.canvas,
            self.Width * 20,
            self.Height * 20,
            "@image_river_width.png", 
            width=200)
        self.river_width = controls.river_width_control(
            self.root,
            self.canvas,
            self.Width,
            self.Height,
            self.riverbed,
        )
        # self.riverbed.update(self.river_width.value-200)
        self.river_width.label.place(relx = .15, rely =.78, anchor = 'c')


        self.eqn = equations(self.flow_speed.value,self.river_width.value,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
        # Run button that gives out calculated values

        self.run_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.89,
            "@image_run.png",
            command=self.run,
            posi= 'nw',
            width = 100)
        #self.run_button.place(relx = .15, rely = .9, anchor = 'c')

        self.reset_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.89,
            "@image_reset.png",
            command=self.reset,
            posi= 'c',
            width = 200)
  
        
        self.hide_vectors_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.89,
            "@image_hide_vectors.png",
            command=self.show_vectors,
            posi='c',
            width = 200)
        # Show vectors button
        self.show_vectors_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.89,
            "@image_show_vectors.png",
            command=self.show_vectors,
            posi='c',
            width = 200)
        # Back button
        self.back_button = CanvasButton(
            self.canvas,
            self.Width * 0.15,
            self.Height * 0.89,
            "@image_back.png",
            command=self.go_back,
            posi = 'ne',
            width = 100)
        
         # Help page
        self.help_page_button = CanvasButton(
            self.canvas,
            self.Width * 0.8,
            self.Height * 0.8,
            "@image_help_page.png",
            command=self.show_help_page,
            width = 50
        )
        
        
        # Equation page
        self.equation_page_button = CanvasButton(
            self.canvas,
            self.Width * 0.8,
            self.Height * 0.8,
            "@image_equation_page.png",
            command=self.show_equation_page,
            width = 50
        )
        
        # self.thread_waves = Thread(target = self.waves)
        # self.thread_waves.daemon = True

        
        #river animation
        
        self.q = queue.Queue()
        self.q2 = queue.Queue()
        self.q3 = queue.Queue()
        self.event = Event()
        self.event2 = Event()
        self.thread_waves = Thread(target = self.allwaves, args=(self.q,))
        # self.thread_waves.daemon = True
        self.thread_waves.start()


        self.thread_riverbed = Thread(target = self.riverbed._resize_image, args = (self.root,))
        self.thread_riverbed.start()

        self.thread_vectors = Thread(target = self.vectors, args = (self.q3,))
        self.thread_vectors.start()

        self.q.put(0)
        self.q3.put(3)

        self.root.mainloop()
    
    def vectors(self, queue):
        while True:
            self.eqn_v = equations(self.flow_speed.value,self.river_width.value,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
            queues = queue.get()
            #print('vectors')
            if queues == 3:
                #print('skip')
                print('waiting')
                self.event.wait()
                self.event.clear()

            #print('doing')
            # self.show_vectors()
            queue.put(0)
           
            self.eqn_v.actual_velocity()
            self.eqn_v.actual_angle()
            self.eqn_v.time()
            self.arrow.configure(self.eqn_v.horizontal_distance(self.Width), self.eqn_v.vertical_distance(),self.flow_speed.value, self.Height)
            #self.arrow = arrow.show(self.Width*0.5, self.Height*0.5, self.eqn_v.horizontal_distance(self.Width), self.eqn_v.vertical_distance(), self.flow_speed.value, self.Height)

    def allwaves(self, queue):
        while True:
            queues = queue.get()
            print("q=",queues)
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
                    self.boat.move(self.eqn, self.q, self.q2)
                    #queue.task_done()
                else:
                    self.boat.move(self.eqn, self.q, self.q2)
                    queue.put(1)
                    #queue.task_done()
            elif queues == 3:
                print('break')
                self.event2.wait()
                self.event2.clear()
            else:
                flow = self.flow_speed.value
                print('else')
                with queue.mutex:
                    queue.queue.clear()

            


    # Update the width and height data of the window and re
    def update(self, event):
        print('update')
        # self.arrow = arrow(self.canvas,self.Width*0.5, self.Height*0.5, self.eqn_v.horizontal_distance(self.Width), self.eqn_v.vertical_distance(), self.flow_speed.value,self.Height)
        self.Width = self.root.winfo_width()
        self.Height = self.root.winfo_height()
        self.speed_of_boat.configure(self.Width, self.Height)
        self.direction_of_boat.configure(self.Width, self.Height)
        self.flow_speed.configure(self.Width,self.Height)
        self.river_width.configure(self.Width,self.Height)
        self.run_button.configure(self.Width * 0.15, self.Height * 0.932)
        self.show_vectors_button.configure(self.Width * 0.15, self.Height * 0.85)
        self.hide_vectors_button.configure(self.Width * 0.15, self.Height * 0.85)
        self.back_button.configure(self.Width * 0.15, self.Height * 0.932)
        self.reset_button.configure(self.Width * 0.15, self.Height * 0.908)
        self.riverbed.configure(self.Width, self.Height)
        self.help_page_button.configure(self.Width * 0.965, self.Height * 0.05, "raise")
        self.equation_page_button.configure(self.Width * 0.965, self.Height * 0.92, layer = "raise")
        self.boat.configure(self.Width,self.Height, self.river_width.value)
        self.canvas.coords(self.river,self.Width*0.3,0,self.Width,self.Height)
        self.eqn.horizontal_distance(self.Width)
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
        self.rwtitle.configure(self.Width * 0.15, self.Height * 0.66, width = self.size)
        self.speed_of_boat.label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        self.direction_of_boat.label.config(font = ('Comic Sans MS',int(self.size/20),'bold'))
        self.flow_speed.label.config(font = ('Comic Sans MS',int(self.size/20),'bold')) 
        self.river_width.label.config(font = ('Comic Sans MS',int(self.size/20),'bold')) 
        try:
            self.waves.configure(self.Width,self.Height)
        except AttributeError:
            pass
        try:
            self.eqn_v = equations(self.flow_speed.value,self.river_width.value,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
            #self.show_vectors()
            self.eqn_v.actual_velocity()
            self.eqn_v.actual_angle()
            self.eqn_v.time()
            self.arrow.configure(self.eqn_v.horizontal_distance(self.Width), self.eqn_v.vertical_distance(),self.flow_speed.value, self.Height)
        except AttributeError:
            pass
        
    def reset(self):
        self.speed_of_boat.reset()
        self.direction_of_boat.reset()
        self.flow_speed.reset()
        self.river_width.reset()
        self.boat.reset()
        self.riverbed.reset()
        self.q.put(3)
        

    # Run function that uses equation python file to calculate the values
    def run(self):
        self.event2.set()
        self.event.set()
        self.update(None)
        self.eqn = equations(self.flow_speed.value,self.river_width.value,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
        self.eqn.actual_velocity()
        self.eqn.actual_angle()
        self.eqn.time()
        print(self.thread_waves.is_alive())
        self.q.put(1)
        self.q2.put(1)
        self.q3.put(1)


        print("pressed")
        # print(self.flow_speed.value,self.Width, self.Height)
        # self.waves.start(self.eqn.time(), self.flow_speed.value)


    # Destroy current window and create a new homepage 
    def go_back(self):
        self.root.destroy()
        os.system('python Increment3_homepage.py')

    # Show vector button
    def show_vectors(self):
        self.eqn_v = equations(self.flow_speed.value,self.river_width.value,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
        if self.flag == True:
            print('config')
            self.show_vectors_button.configure(self.Width * 0.15, self.Height * 0.85, 'lower')
            self.hide_vectors_button.configure(self.Width * 0.15, self.Height * 0.85, 'raise')
            self.flag = False
            self.eqn_v.actual_velocity()
            self.eqn_v.actual_angle()
            self.eqn_v.time()
            self.arrow = arrow(self.canvas, self.Width*0.5, self.Height*0.5, self.eqn_v.horizontal_distance(self.Width), self.eqn_v.vertical_distance(), self.flow_speed.value,self.Height)
            
            self.event.set()
        else:
            self.q3.put(3)
            self.event.set()
            self.show_vectors_button.configure(self.Width * 0.15, self.Height * 0.85, 'raise')
            self.hide_vectors_button.configure(self.Width * 0.15, self.Height * 0.85, 'lower')
            self.flag = True
            try:
                self.arrow.remove()
            except AttributeError:
                pass


    # Show help page 
    def show_help_page(self):
        # self.q.put(3)
        # self.q3.put(3)
        os.system('python Increment3_help_page.py')
        # from Increment3_help_page import HelpPage
        # HelpPage() 
       

    # Show equation page 
    def show_equation_page(self):
        #self.eqn = equations(self.flow_speed.value,self.river_width.value,self.speed_of_boat.value, self.direction_of_boat.value, self.Height)
        os.system(f'python increment3_equpage_simu.py  {self.flow_speed.value} {self.direction_of_boat.value} {self.speed_of_boat.value} {self.river_width.value} {self.Height}')
        # from increment3_equpage_simu import EquationPage
        # EquationPage(self.eqn, self.flow_speed.value,self.direction_of_boat.value, self.speed_of_boat.value,self.river_width.value)
        
        
if __name__ == "__main__": # if this is the main python file running:
    window = Window()

