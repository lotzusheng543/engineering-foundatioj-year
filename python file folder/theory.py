from tkinter import *
import gc


class theory:
   def __init__(self):
      self.win = Tk()
      self.win.geometry("550x320+0+0")
      self.win.geometry("850x350")
      self.win.title("Theory & Equation")
      self.backbutton = Button(self.win, text ='Back', command = self.go_back)
      self.backbutton.place(relx = 0, rely = 1, anchor = 'sw')
      Label(self.win, text="""
   Vectors are quantities that have both magnitude (size) and direction (Britannica, 2020). 
   In the Riverboat Simulator, users can control the boat's velocity and direction using vectors. 
   The equation used: v = v_x i + v_y j 
   where i and j are unit vectors in the x- and y-directions, respectively.

   When two or more vectors are combined, their effects can be added together using vector addition (Weisstein, Eric W.).
   In the simulator, the boat's velocity relative to the water 
   and the velocity of the river are added together to determine the boat's overall velocity relative to the shore. 
   The equation used: v_total = v_boat + v_river 

   where v_boat is the velocity vector of the boat relative to the water, and v_river is the velocity vector of the river. 

   
   A right triangle has three sides, which can be uniquely identified as the hypotenuse, adjacent to a given angle θ, or opposite θ. 
   In right triangle trigonometry, there are six trigonometric functions: sine (sin), cosine (cos), tangent (tan), cosecant (csc), secant (sec), and cotangent (cot). 
   These functions relate the ratios of the sides of a right triangle to the angles opposite them. 
   The equations used: 
   sin θ     = opposite/ hypotenuse 

   cos θ    = adjacent/ hypotenuse 

   tan θ    = opposite/ adjacent """, font=('Arial 11 bold') ,).place(relx =.5 ,rely = .5, anchor ='c')

      self.win.mainloop()

   def go_back(self):
      from Homepage_v5 import Homepage 
      self.win.destroy()
      gc.collect()
      Homepage(Tk())

if __name__ == '__main__':
   theory()