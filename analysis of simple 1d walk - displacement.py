#simple random walk - Tracking displacement in 1 dimension
import numpy as np
import random
from tqdm import tqdm
from matplotlib import pyplot as plt

def take_a_step(position):
    
    #walker takes a step
    
    steps = [[-1],[1]]
    new_step = np.array(random.choice(steps))
    position = position + new_step
    
    return position    

plt.figure(figsize = (8,5))

for i in tqdm(range(0,4)):
    
    x = np.array([0])
    N = 1000
    pos = x
    pos_track = x
    
    for i in range(0,N):
        pos = take_a_step(pos)
        pos_track = np.vstack((pos_track,pos))
        
    plt.plot(range(0,N+1),pos_track, alpha = 1, linewidth = 0.6)


plt.grid(color='k', linestyle='--', linewidth=0.5,alpha = 0.3)

x = np.linspace(0,N,N+1)
y1 = 1.25*np.sqrt(x)
y2 = -1*y1
y3 = 2.5*np.sqrt(x)
y4 = -1*y3

plt.plot(x,y1, linestyle = '--', color = 'k', linewidth=1.15, label = '$C_{1,2}\sqrt{n}$')
plt.plot(x,y2, linestyle = '--', color = 'k', linewidth=1.15)
plt.plot(x,y3, linestyle = '--', color = 'k', linewidth=1.15)
plt.plot(x,y4, linestyle = '--', color = 'k', linewidth=1.15)

plt.xlabel('n')
plt.ylabel(r'$S_n$')
plt.savefig("brownian_examples1.pdf")
plt.show()    