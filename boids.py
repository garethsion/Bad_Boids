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
    
    fly_to_mid_x_weight = 0.01
    fly_to_mid_y_weight = 0.01
    nearby_boid_dist = 100
    flying_dist = 10000
    group_flying_x_weight = 0.125
    group_flying_y_weight = 0.125
    
    # Fly towards the middle
    for i in range(number_of_boids):
	for j in range(number_of_boids):
	    xvs[i]=xvs[i]+(xs[j]-xs[i])*fly_to_mid_x_weight/number_of_boids
    for i in range(number_of_boids):
	for j in range(number_of_boids):
	    yvs[i]=yvs[i]+(ys[j]-ys[i])*fly_to_mid_y_weight/number_of_boids
    
    # Fly away from nearby boids
    for i in range(number_of_boids):
	for j in range(number_of_boids):
	    if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < nearby_boid_dist:
		xvs[i]=xvs[i]+(xs[i]-xs[j])
		yvs[i]=yvs[i]+(ys[i]-ys[j])
    
    # Try to match speed with nearby boids
    for i in range(number_of_boids):
	for j in range(number_of_boids):
	    if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < flying_dist:
		xvs[i]=xvs[i]+(xvs[j]-xvs[i])*group_flying_x_weight/number_of_boids
		yvs[i]=yvs[i]+(yvs[j]-yvs[i])*group_flying_y_weight/number_of_boids
    
    # Move according to velocities
    for i in range(number_of_boids):
	xs[i]=xs[i]+xvs[i]
	ys[i]=ys[i]+yvs[i]

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
   
