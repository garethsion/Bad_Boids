#from Flock import new_boids
#from nose.tools import assert_almost_equal
#import os
#import yaml

from ..boids import Flock, Boid
from nose.tools import assert_almost_equal, assert_raises
from numpy.testing import assert_array_equal, assert_allclose
from numpy import array
import os
import yaml

def test_boid_init():
    flock = Flock(50,20.0,30.0,40.0,50.0)
    # Check boid links properly to flock
    assert_almost_equal(flock.boids[0].flock.number_of_boids,50,delta=0.01)
    assert_almost_equal(flock.boids[0].flock.group_flying_dist*flock.group_flying_dist,
            400,delta=0.01)
    assert_almost_equal(flock.boids[0].flock.group_flying_weight,
            30,delta=0.01)
    assert_almost_equal(flock.boids[0].flock.nearby_boid_dist*flock.nearby_boid_dist,
            1600,delta=0.01)
    assert_almost_equal(flock.boids[0].flock.mid_strength,
            50,delta=0.01)
    for boid in flock.boids:
        # Check that position and velocity are correct
        assert_allclose(boid.position,(-200,450),atol=250)
        assert_allclose(boid.velocity,(5,0),atol=20)

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)