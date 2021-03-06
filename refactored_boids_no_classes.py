"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
from numpy import array

# Deliberately terrible code for teaching purposes

number_of_boids = 50 # removed unnecessary repetition of this number

x_pos_bounds = array([-450, 50.0])
y_pos_bounds = array([300.0, 600.0])

x_vel_bounds = array([0, 10.0])
y_vel_bounds = array([-20.0, 20.0])

x_axis_limits = [-500,1500]
y_axis_limits = [-500,1500]

anim_frame_rate = 50
anim_interval = 50

boids_x=[random.uniform(x_pos_bounds[0],x_pos_bounds[1]) for x in range(number_of_boids)]
boids_y=[random.uniform(y_pos_bounds[0],y_pos_bounds[1]) for x in range(number_of_boids)]
boid_x_velocities=[random.uniform(x_vel_bounds[0],x_vel_bounds[1]) for x in range(number_of_boids)]
boid_y_velocities=[random.uniform(y_vel_bounds[0], y_vel_bounds[1]) for x in range(number_of_boids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    
    fly_to_mid_weight = 0.01
    fly_to_mid_weight = 0.01
    nearby_boid_dist = 100
    flying_dist = 10000
    group_flying_weight = 0.125
    group_flying_weight = 0.125
    
   
    for i in range(number_of_boids):
        for j in range(number_of_boids):
            x_seperation = (xs[j] - xs[i])
            y_seperation = (ys[j] - ys[i])
            
            # Fly towards the middle
            xvs[i]+=x_seperation*fly_to_mid_weight/number_of_boids
            yvs[i]+=y_seperation*fly_to_mid_weight/number_of_boids
   
            # Fly away from nearby boids
            if x_seperation**2 + y_seperation**2 < nearby_boid_dist:
                xvs[i]-=x_seperation
		yvs[i]-=y_seperation
     
            # Try to match speed with nearby boids
            x_velocity_seperation = (xvs[j]-xvs[i]) 
            y_velocity_seperation = (yvs[j]-yvs[i]) 
	    if x_seperation**2 + x_seperation**2 < flying_dist:
		xvs[i]+=x_velocity_seperation*group_flying_weight/number_of_boids
		yvs[i]+=y_velocity_seperation*group_flying_weight/number_of_boids
    
    # Move according to velocities
    for i in range(number_of_boids):
	xs[i]+=xvs[i]
	ys[i]+=yvs[i]

figure=plt.figure()
axes=plt.axes(xlim=(x_axis_limits[0],x_axis_limits[1]), ylim=(y_axis_limits[0],y_axis_limits[1]))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0],boids[1]))

anim = animation.FuncAnimation(figure, animate,
                               frames=anim_frame_rate, interval=anim_interval)

if __name__ == "__main__":
    plt.show()
   
