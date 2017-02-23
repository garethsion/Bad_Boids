from matplotlib import pyplot as plt
from matplotlib import animation
import random
from numpy import array

number_of_boids = 50

x_pos_bounds = array([-450, 50.0])
y_pos_bounds = array([300.0, 600.0])

x_vel_bounds = array([0, 10.0])
y_vel_bounds = array([-20.0, 20.0])

x_axis_limits = [-500,1500]
y_axis_limits = [-500,1500]

anim_frame_rate = 50
anim_interval = 50

fly_to_mid_weight = 0.01
nearby_boid_dist = 100
flying_dist = 10000
group_flying_weight = 0.125
    
class Boid(object):
    def __init__(self, owner, position, velocity):
        self.position = position
        self.velocity = velocity
        self.flock = owner
		
    def flight(self, target):
        flight = array([0.0,0.0])
		
	x_seperation = target.pos[0] - self.pos[0]
	y_seperation = target.pos[1] - self.pos[1]
	x_vel_seperation = target.vel[0] - self.vel[0]
	y_vel_seperation = target.vel[1] - self.vel[1]
		
	# Fly towards the middle
        flight[0]+=x_seperation*self.flock.fly_to_mid_weight/self.flock.number_of_boids
        flight[1]+=y_seperation*self.flock.fly_to_mid_weight/self.flock.number_of_boids
   
        # Fly away from nearby boids
        if x_seperation**2 + y_seperation**2 < self.flock.nearby_boid_dist:
            flight[0]-=x_seperation
            flight[0]-=y_seperation
     
        # Try to match speed with nearby boids
	if x_seperation**2 + x_seperation**2 < self.flock.flying_dist:
            flight[0]+=x_velocity_seperation*self.flock.group_flying_weight/
                self.flock.number_of_boids
	    flight[1]+=y_velocity_seperation*self.flock.group_flying_weight/
                self.flock.number_of_boids
		
	return flight 

class Flock(object):
    def __init__(self,number_of_boids,flying_dist,group_flying_weight,nearby_boid_dist,
        fly_to_mid_weight:
		
        self.number_of_boids = number_of_boids
        self.flying_dist = flying_dist
	self.group_flying_weight = flying_weight
	self.nearby_boid_dist = nearby_boid_dist
	self.fly_to_mid_weight = fly_to_mid_weight
		
	self.boids = [Boid(array([random.uniform(x_pos_bounds[0], x_pos_bounds[1]),
	    random.uniform(y_pos_bound[0], y_pos_bounds[1])]), 
	    array([random.uniform(x_vel_bounds[0], x_vel_bounds[1]), 
	    random.uniform(y_vel_bounds[0], y_vel_bounds[1])])) 
	    for boids in range(number_of_boids)]
		
    def update_boids(self):
	for boid in self.boids:
            flight = array([0.0,0.0])
	    for target in self.boids:
		flight+=boid.flight(target)
		boid.velocity+=boid.velocity # right way around?
		boid.position+=flight

flock = Flock(50)

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
