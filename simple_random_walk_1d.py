# 1D - simple random walk

import numpy as np
import random

def take_a_step(position):
    
    #walker takes a single step
    
    steps = [[-1],[1]]
    new_step = np.array(random.choice(steps))
    position = position + new_step
    
    return position    

    
x = np.array([0])     #origin
N = 1000              #number of steps


#tracking position
pos = x
pos_track = x
for i in range(0,N):
    pos = take_a_step(pos)
    pos_track = np.vstack((pos_track,pos))