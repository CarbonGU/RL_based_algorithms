import numpy
import random as ran

#random policy
def random_pi():
    actions     = ['n', 'e', 's', 'w']
    random_index = int(ran.random()*4)
    return actions[random_index]

def compute_random_pi_state_value():
    value = [0.0 for r in xrange(9)]
