from numpy import array
import random

class Boid(object):
    def __init__(self,flock,position,velocity):
        self.position = position
        self.velocity = velocity
        self.flock = flock
    
    def flight(self, target):
        position_sep = target.position - self.position
        velocity_sep = target.velocity - self.velocity
        distance = position_sep.dot(position)
        
	# Fly towards the middle
        self.velocity+=position_sep*self.flock.fly_to_mid_strength/self.flock.number_of_boids
        
        # Fly away from nearby boids
        if distance < self.flock.nearby_boid_dist*self.flock.nearby_boid_dist:
            self.velocity-=relative_position
        
        # Try to match speed with nearby boids
        if distance < self.flock.group_flying_dist*self.flock.group_flying_dist:
            self.velocity+=velocity_sep*self.flock.group_flying_weight/self.flock.number_of_boids
            
        return flight

class Flock(object):
    def __init__(self,
            number_of_boids = 50,
            flying_dist = 10000, 
            group_flying_weight = 0.125,
            nearby_boid_dist = 10,
            fly_to_mid_weight = 0.01,
            initial_position = [[-450,50],[300,600]],
            initial_velocity = [[0,10],[-20,20]]):
 
	    self.boids = [Boid(array([random.uniform(initial_position[0][0], 
                initial_position[0][1]), random.uniform(initial_position[1][0], 
                initial_position[1][1])]), array([random.uniform(initial_velocity[0][0], 
                initial_velocity[0][1]), 
	    random.uniform(initial_velocity[1][0], initial_velocity[1][1])])) 
	    for boids in range(number_of_boids)]
		
    def new_boids(self):
        for boid in self.boids:
            for target in self.boids:
                boid.flight(target)
        for boid in self.boids:
            boid.position+=boid.velocity
