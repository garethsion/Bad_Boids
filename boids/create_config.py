"""Generates a config yaml file containing the default parameters for boids"""

import yaml
import os

write_file = 'config.yml'

number_of_boids = 50
fly_to_mid_weight = 0.01
nearby_boid_dist = 100 
flying_dist = 10000
group_flying_weight = 0.125
alert_distance = 10 

initial_position = [[-450,50],[300,600]] 
initial_velocity = [[0,10],[-20,20]] 
axis_limits = [[-500,1500],[-500,1500]]

cfgdata={"number_of_boids":number_of_boids,"flying_dist":flying_dist,"group_flying_weight":group_flying_weight,"nearby_boid_dist":nearby_boid_dist,"fly_to_mid_weight":fly_to_mid_weight,"initial_position":initial_position,"initial_velocity":initial_velocity,"axis_limits":axis_limits}

config_file=open(write_file,'w')
config_file.write(yaml.dump(cfgdata))
config_file.close()

print 'Config data written to file '+write_file


