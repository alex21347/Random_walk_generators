#2D simple random walk - square lattice
import numpy as np
import random
from matplotlib import pyplot as plt

x = np.array([0,0])
N = 100


def take_a_step(position):
    
    #walker takes one step
    
    steps = [[-1,0],[1,0],[0,1],[0,-1]]
    new_step = np.array(random.choice(steps))
    position = position + new_step
    
    return position    


#taking N steps and tracking position
    
pos = x
pos_track = x
for i in range(0,N):
    pos = take_a_step(pos)
    pos_track = np.vstack((pos_track,pos))
    
#plotting result
pt = pos_track
plt.figure(figsize = (6,6))
for i in range(1,len(pt[:,0])):
    plt.plot([pt[i-1,0],pt[i,0]],[pt[i-1,1],pt[i,1]],color = 'k')
plt.axis('equal')
plt.grid(color='k', linestyle='--', linewidth=0.5,alpha = 0.4)
plt.show()