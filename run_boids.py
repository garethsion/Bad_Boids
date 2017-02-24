from .boids import Flock, Boid
from matplotlib import pyplot as plt
from matplotlib import animation
from argparse import ArgumentParser
import yaml
import os

def parse_args():
    parser = ArgumentParser(description = "Runs the program.")
    parser.add_argument('--file', type=str,
            help='YAML file to load data from')
    parser.add_argument('--size', default=50, type=int,
            help='Number of boids in flock.')
    parser.add_argument('--dist', default=100, type=float,
            help='Distance over which boids try to match speed.')
    parser.add_argument('--strength', default=0.125, type=float,
            help='How strongly boids try and match speed.')
    parser.add_argument('--avoid_dist', default=10, type=float,
            help='Distance in which boids avoid each other.')
    parser.add_argument('--mid_strength', default=0.01, type=float,
            help='How strongly boids try and flock together.')
    arguments=parser.parse_args()
    
    initial_position = [[-450,50],[300,600]] 
    initial_velocity = [[0,10],[-20,20]] 
    axis_limits = [[-500,1500],[-500,1500]] 
       
    cfgdata={"input_file":arguments.file,
             "number_of_boids":arguments.size,
             "group_flying_dist":arguments.dist,
             "group_flying_strength":arguments.strength,
             "alert_distance":arguments.avoid_dist,
             "mid_strength":arguments.mid_strength,
             "initial_position":initial_position,
             "initial_velocity":initial_velocity,
             "axis_limits":axis_limits}
    
    return cfgdata

def load_config(config_filename):
    cfgfile = open(config_filename,'r')
    cfgdata = yaml.load(cfgfile)
    cfgfile.close()
    
    cfgdata['input_file'] = config_filename
    
    return cfgdata
        
def run_boids(cfgdata):
    number_of_boids = cfgdata["number_of_boids"]
    formation_flying_distance = cfgdata["group_flying_dist"]
    formation_flying_strength = cfgdata["group_flying_strength"]
    alert_distance = cfgdata["alert_distance"]
    attraction_strength = cfgdata["mid_strength"]
    initial_position_range = cfgdata["initial_position"]
    initial_velocity_range = cfgdata["initial_velocity"]
    axis_limits = cfgdata["axis_limits"]
    
    flock = Flock(flock_size,
                  formation_flying_distance,
                  formation_flying_strength,
                  alert_distance,
                  attraction_strength,
                  initial_position_range,
                  initial_velocity_range)

    figure=plt.figure()
    axes=plt.axes(xlim=(plot_axis_limits[0][0],
                        plot_axis_limits[0][1]),
                  ylim=(plot_axis_limits[1][0],
                        plot_axis_limits[1][1]))

    x_vals = [boid.position[0] for boid in flock.boids]
    y_vals = [boid.position[1] for boid in flock.boids]
    boid_scatter = [boid.position for boid in flock.boids]

    scatter=axes.scatter(x_vals,y_vals)

    def animate(frame):
        flock.new_boids()
        scatter.set_offsets(boid_scatter)

    anim = animation.FuncAnimation(figure, animate,
                                  frames=50, interval=50)
                                  
    plt.title('Boids')
    plt.show()
