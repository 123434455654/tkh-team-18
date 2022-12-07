from roboticstoolbox import Bicycle, RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
print("the values should be to one decimal place")
#enter the intial and target points in the grid
print("1. starting point(-1,-1) and final point(7,7)")
print("2. starting point(6,-6) and final point(0,5)")
print("3. starting point(7.5,7.5) and final point(-7,3)")
choice=int(input("enter the number:"))



#set vehcile type
anim = VehicleIcon('robo', scale=1.5)
goal_arr=[]
#choice in a list
if choice==1:
    goal_arr=[[-1,-1],[6.5,5],[7,6],[7,7]]
elif choice ==2:
    goal_arr=[[6,-6],[5,1],[-7,-7],[0,5]]
elif choice ==3:
    goal_arr=[[7.5,7.5],[0,3],[3,4],[-7,3]]
while choice>3 or choice<0:
    print("error didnt enter a valid number, choose 1 or 2 or 3")
    choice=int(input("enter the number:"))
    if choice==1:
        goal_arr=[[-1,-1],[6.5,5],[7,6],[7,7]]
    elif choice ==2:
        goal_arr=[[6,-6],[5,1],[-7,-7],[0,5]]
    elif choice ==3:
        goal_arr=[[7.5,7.5],[0,3],[3,4],[-7,3]]

# setting the type of vehcile and grid size
veh = Bicycle(
    animation=anim,
    control=(RandomPath),
    dim=10,
    x0=[goal_arr[0][0],goal_arr[0][1],0],

)
#map and obsicles
veh.init(plot=True)
map = LandmarkMap(20,10)
map.plot()
mapx = mpimg.imread("map.png")
plt.imshow(mapx,extent=[-10,10,-10,10])
sensor=RangeBearingSensor(robot=veh,map=map,animate=True)



#target place and size


target_marker_style = {
 'marker': 'D',
 'markersize': 7,
 'color': 'r',
}
#ploting the target on the grid
plt.plot(goal_arr[-1][0], goal_arr[-1][1], **target_marker_style)
plt.plot(goal_arr[-1][0], goal_arr[-1][1], **target_marker_style)

#split x and y to use in polyfit
x_arr=[i[0] for i in goal_arr]
y_arr=[i[1] for i in goal_arr]

z = np.polyfit(x_arr, y_arr, len(goal_arr)-1)
p = np.poly1d(z)
# index1 = x_arr.index(min(x_arr))
# index2 = x_arr.index(max(x_arr))
t = np.linspace(x_arr[0],x_arr[-1], 50)
plt.plot(t,p(t),'-')

 
#looping points
for i in range(len(t)-1):
    run=True
    target=[t[i+1],p(t)[i+1]]
    while(run):
        for i in sensor.h(veh.x):
            if (i[0] < 2) and (abs(i[1]) < pi/4):
                break

        # moving the robot to goal from the intial position
        goal_heading = atan2(
        target[1] - veh.x[1],
        target[0] - veh.x[0]
            )
        # checking if the the angle of steer is bigger than pi
        steer = goal_heading-veh.x[2]
        if steer>pi:
            steer = steer-2*pi
        veh.step(2,steer)
        #check if the robot is close enough the the goal to stop
        if( (abs(target[0]-veh.x[0]) >0.3) or (abs(target[1] -veh.x[1]) >0.3) ):
            run=True
        else:
            run=False
        veh._animation.update(veh.x)
        plt.pause(0.0005)
plt.pause(200)