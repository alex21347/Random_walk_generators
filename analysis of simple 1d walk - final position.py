#simple random walk - 1D - final position density
import numpy as np
import random
from matplotlib import pyplot as plt
from tqdm import tqdm
import matplotlib

posall = []

#simulate walks

for i in tqdm(range(0,10000)):   #this cell takes a while to run
    
    x = np.array([0])
    N = 1000
    
    def take_a_step(position):
        'walker takes a step'
        
        steps = [[-1],[1]]
        new_step = np.array(random.choice(steps))
        position = position + new_step
        
        return position    
    
    pos = x
    pos_track = x
    for i in range(0,N):
        pos = take_a_step(pos)
        
    posall = np.append(posall,pos)
    

#plotting results
    
font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 17}

matplotlib.rc('font', **font)    
    
plt.figure(figsize = (10,10))
plt.hist(posall, bins = 230, density = True, color = 'grey')

plt.grid(color='k', linestyle='--', linewidth=0.5,alpha = 0.3)
x = np.linspace(-150,150,N+1)
y = (2/np.sqrt(2*np.pi*N))*np.exp((-1*x**2)/(2*N))

plt.plot(x,y, linestyle = '--', color = 'k', linewidth=1.15, label = r'$\frac{2}{\sqrt{2n\pi}}\;e^{\frac{-x^2}{2n}}$')

plt.xlabel('$S_n$')
plt.legend(prop={'size': 20})
plt.ylabel('Probability Density')
plt.savefig('fignow.pdf')
plt.show()    