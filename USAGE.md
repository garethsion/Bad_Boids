To install, run: sudo python setup.py install

This program has been written to run from the command line. 

To run type: good_boids [-h]
                    	[--file FILE]
                    	[--size SIZE]
                    	[--dist DIST]
                    	[--strength STRENGTH]
                    	[--avoid_dist AVOID_DIST]
                    	[--mid_strength MID_STRENGTH]

Optional arguments:
  -h, --help
                        Shows a help message and exits.
  
  --file "filename.yml"
                        YAML file to load data from.
                        
  --size [int]
                        Number of boids in flock.
  
  --dist [num]
                        Distance over which boids try to match speed.
                        
  --strength [num]
                        How strongly boids try and match speed.
                        
  --avoid_dist [num]
                        Distance in which boids avoid colliding with one another.
                        
  --d_strength [num]
                        The degree to which boids try and flock together.



This code implements an algorithm which simulates how birds fly and avoid each other
(http://dl.acm.org/citation.cfm?doid=37401.37406) . This code was written as part of 
an assignment for UCL's MPHYG001 course (http://development.rc.ucl.ac.uk/training/engineering)

The parameters of this code can be modified by specifying a YAML file using --file "filename.yml".
If one provides a config file in this way, all parameters will be modified by the values held
in the config file.

The initial_position and initial_velocity ranges axis_limits, can be specified in a YAML config also.
