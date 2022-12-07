# Aim of the project
the aim of the project is to generate a start and end point for the robot to move towards. In order to move the robot, a curved path is generated thst the robot will follow avoiding the wallls and obstacles encountered.

## how the robot works
Firstly, the user will have 3 choices for the journey of the robot, each choice has its own start and end coordinates. Furthermore, the polyfit function generates the curve, which is the path that the robot will follow. In addition, sensors were utilised to know the difference between the current location of the vehicle and the landmarks, which resembles the obstacles. A specified tolerance of 0.3 in distance that stops the vehicle from hitting the walls or the obstacles.

## Real life applications for the robot
Transportation: for instance, the robot may deliver a packages to certain locations like a warehouse that consists of 3 storage units. The robot may deliver the boxes to a the drop off location the user wants as shown in the below figure.

![image](https://user-images.githubusercontent.com/104323652/206169501-c55e5f73-1e10-48a4-b346-cffa58a30789.png)








## Dependencies to run the code 
Firstly, you need to download python 3.6 at least, then download robotics toolbox which gives you access to library, data, commands and visuals maps or any visual data. You also need to download visual studio or any other app that understands and can run the python code, and finally it is recommended to download Ubuntu as the operating system, but windows is also a viable option.

## Team members and their contribution
Mohamed Amr, he was responsible to import the libraries, which was vital for the animation and simulation. Not only, importing the libraries, but also printing the opening message and setting the robot's icon scale.
Omar Sherif, who had an integral role as: he made the grid size, plotted the obstacles and the map, plotted the target on the grid and setting its size and coordinate. Finally, splitting the X and Y coordinates for the polyfit function, which aids in making the path.
Ahmed Samy, had a pivotal tasks to accomplish the task, made the piece of code that moves the robot from the initial position towards the target. He coded the steering angles and, using sensors, checking the distance between the vehicle and the target to know when to stop it as well.

## User input and the foreseeable output
The code was designed to be as simple as possible for user; as 3 choices are displayed for the user and the user inputs a number between 1 and 3 to choose. The foreseeable output that the robot moves from a certain point to a certain target as shown in the figure above.
