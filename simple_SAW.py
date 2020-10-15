#Simulating a self-avoiding walk on 2D square lattice

import numpy as np
import random
from matplotlib import pyplot as plt

def take_a_step(position):
    
    #walker takes a step
    
    steps = [[-1,0],[1,0],[0,1],[0,-1]]
    new_step = np.array(random.choice(steps))
    new_pos = position + new_step
    
    return new_pos  


N = 30 #number of steps

steps_til_trap = np.array([])
for j in range(0,1): #this line allows for multiple SAWs to be produced at once

    x = np.array([[0,0]])
    pos = x
    pos_track = x
    a = 0
    for i in range(0,N):
        pos = pos_track[-1,:]
        pos = take_a_step(pos)
        
        #SELF - AVOIDANCE CONSTRAINT
        if np.any(np.all(pos_track == pos ,axis = 1) == True):
            continue
        else:
            pos_track = np.vstack((pos_track,pos))

plt.figure(figsize = (6,6))
for i in range(1,len(pos_track[:,0])):
   plt.plot([pos_track[i-1,0],
             pos_track[i,0]],
            [pos_track[i-1,1],
             pos_track[i,1]],
             color = 'k',
             linewidth = 2.5)
plt.axis('equal')
plt.grid(color='k', linestyle='--', linewidth=0.5,alpha = 0.4)
plt.show()