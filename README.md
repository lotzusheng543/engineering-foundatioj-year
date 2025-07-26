🚤 Riverboat Simulation App
The Riverboat Simulation App is a Python-based program designed to help users understand the principles of vectors and projectiles by simulating a boat crossing a river. Developed during our Engineering Foundation Year at the University of Southampton Malaysia, this application aims to improve understanding of how a boat's trajectory is influenced by both its own velocity and the river’s current.





🧠 Background
Inspired by challenges in maritime navigation, this simulator addresses the difficulty in accurately predicting a boat's moving direction and arrival time due to unforeseen weather and wave conditions. It provides a safe alternative to real-world experiments for analyzing the relationship between vector components of a riverboat traveling across a river with current.





The project integrates fundamental physics concepts, including:


Vectors: Quantities with both magnitude (size) and direction. In the simulator, users can control the boat's velocity and direction. The general equation used is 


v=V 
x
​
 i+V 
y
​
 j, where i and j are unit vectors in the x- and y-directions.


Vector Addition: Used to combine two or more vectors. In the simulator, the boat's velocity relative to the water and the river's velocity are added to determine the boat's overall velocity relative to the shore. The equation used is 


v 
total
​
 =v 
boat
​
 +v 
river
​
 .


Right Triangle Trigonometry: Relates the ratios of the sides of a right triangle to the angles opposite them. Functions like sine, cosine, and tangent are employed. The magnitude of a vector 


a=( 
x
y
​
 ) is calculated by ∣a∣[cite 
s
​
 tart]= 
x 
2
 +y 
2
 

​
  (Pythagoras Theorem).

🎯 Project Goals
The primary goals set for this program were:

To determine the effect of varying boat speeds on the crossing time and downstream distance for a boat heading straight across a river.

To determine the effect of varying current speeds on the crossing time of the boat and the downstream distance for a boat heading straight across a river.

To code a properly running and accurate simulation program, without incorporating air resistance.

To develop a fully functioning system that can realistically help those planning to travel via boats arrive at their destination safer and faster by viewing a trip simulation.

🖥 Features
The application provides a user-friendly interface with several key features:


Home Page: Provides access to three main sections: Simulation, Start Game, and Equations.


Simulation Page: Allows users to input and adjust values such as speed of boat, direction of boat, flow control (river speed), and river width. An animation will be stimulated, displaying resultant speed, actual angle, and time spent. Users can also toggle the visibility of vector arrows.




Start Game Page (Challenge Page): Users can click the "Challenge" button to get random values for river width and the y-coordinate of a challenge point. The goal is to calculate and adjust values to reach this point. A message box indicates success or failure after running the simulation.




Equations Page: Displays the theory and equations for Basic Trigonometric Formula, helping users understand resultant speed, actual angle, and time spent on vectors.


Help Page & Bottom-right Notebook Page: The Help Page provides answers to Frequently Asked Questions and useful tutorials. The bottom-right notebook page shows how different input values can be applied to equations.


⚙️ Installation and Setup

Download and Install: Download all essential Python files to your device.


Install Prerequisites: Before launching, ensure you install the Pillow and Fraction programs via the command prompt.


Pillow: https://www.geeksforgeeks.org/how-to-install-pil-on-windows/ 


Fraction: https://pypi.org/project/Fraction/ 


Launch: Launch the source code and utilize the interface.

👥 Team
This project was a collaborative effort by Team 9, consisting of:

Lim Kai Shan 


Yen Kai Jing 


Yap En Tong 


Lo Tzu Sheng 


Vince Graceson Victor 


The team's progression was tracked using a burndown chart.


📚 Skills Used
Python Programming

Mathematical and Physics Simulation

User Interface (UI) / User Experience (UX) Design (storyboards, personas, scenarios, user stories) 


Team Collaboration

Agile Principles (e.g., burndown chart) 


⚠️ Disclaimer
The information within this application is for general informational purposes only and was obtained from physicsclass.com. We offer no guarantees or claims as to its availability, appropriateness, completeness, correctness, reliability, or any other aspect. Users solely assume all risk if they rely on this material in any way.










please help me title become crtl+b, ppl name become crtl+i


🚤 Riverboat Simulation App
The Riverboat Simulation App is a Python-based program designed to help users, particularly 

Engineering Foundation Year students, understand the concepts of vectors and projectiles by simulating a boat crossing a river. The application aims to enhance understanding of how different forces result in varying velocities and how to predict a boat's movement and arrival time.


🧠 Background
Inspired by challenges in maritime navigation, this simulator addresses the difficulty in accurately predicting a boat's moving direction and arrival time due to unforeseen weather and wave conditions. It provides a safe alternative to real-world experiments for analyzing the relationship between vector components of a riverboat traveling across a river with current.


The project integrates fundamental physics concepts, including:


Vectors: Quantities with both magnitude (size) and direction. In the simulator, users can control the boat's velocity and direction. The general equation used is 


v=V 
x
​
 i+V 
y
​
 j, where i and j are unit vectors in the x- and y-directions.


Vector Addition: Used to combine two or more vectors. In the simulator, the boat's velocity relative to the water and the river's velocity are added to determine the boat's overall velocity relative to the shore. The equation used is 


v 
total
​
 =v 
boat
​
 +v 
river
​
 .


Right Triangle Trigonometry: Relates the ratios of the sides of a right triangle to the angles opposite them. Functions like sine, cosine, and tangent are employed. The magnitude of a vector 


a=( 
x
y
​
 ) is calculated by ∣a∣[cite 
s
​
 tart]= 
x 
2
 +y 
2
 

​
  (Pythagoras Theorem).

The program defines the top of the screen as North, with East, South, and West accordingly. The water flow direction is fixed from North to South, while the boat's moving direction and speed can be adjusted.


🎯 Project Goals
The primary goals set for this program were:

To determine the effect of varying boat speeds on the crossing time and downstream distance for a boat which heads straight across a river.

To determine the effect of varying current speeds on the crossing time of the boat and the downstream distance for a boat which heads straight across a river.

To code a properly running and accurate simulation program, without incorporating air resistance.

To develop a fully functioning system that can realistically help those planning to travel via boats arrive at their destination safer and faster by viewing a trip simulation.

🖥 Features
The application provides a user-friendly interface with several key features:


Home Page: Provides access to three main sections: Simulation, Start Game, and Equations.


Simulation Page: Allows users to input and adjust values such as speed of boat, direction of boat, flow control (river speed), and river width. An animation will be stimulated, displaying resultant speed, actual angle, and time spent. Users can also toggle the visibility of vector arrows.




Start Game Page (Challenge Page): Users can click the "Challenge" button to get random values for river width and the y-coordinate of a challenge point. The goal is to calculate and adjust values to reach this point. A message box indicates success or failure after running the simulation.




Equations Page: Displays the theory and equations for Basic Trigonometric Formula, helping users understand resultant speed, actual angle, and time spent on vectors.


Help Page & Bottom-right Notebook Page: The Help Page provides answers to Frequently Asked Questions and useful tutorials. The bottom-right notebook page shows how different input values can be applied to equations.

⚙️ Installation and Setup

Download and Install: Download all essential Python files to your device.


Install Prerequisites: Before launching, ensure you install the Pillow and Fraction programs via the command prompt.


Pillow: https://www.geeksforgeeks.org/how-to-install-pil-on-windows/ 


Fraction: https://pypi.org/project/Fraction/ 


Launch: Launch the source code and utilize the interface.

👥 Team
This project was a collaborative effort by Team 9, consisting of:


Lim Kai Shan 


Yen Kai Jing 


Lo Tzu Sheng 


Yap En Tong 


Vince Graceson Victor 

The team's progression was tracked using a burndown chart.

📚 Skills Used
Python Programming

Mathematical and Physics Simulation


User Interface (UI) / User Experience (UX) Design (storyboards, personas, scenarios, user stories) 

Team Collaboration


Agile Principles (e.g., burndown chart) 

⚠️ Disclaimer
The information within this application is for general informational purposes only and was obtained from physicsclass.com. We offer no guarantees or claims as to its availability, appropriateness, completeness, correctness, reliability, or any other aspect. Users solely assume all risk if they rely on this material in any way











