

import numpy as np
from matplotlib import*
import matplotlib.pyplot as plt


def sincdemo(t):
    x=[];
    for i in t:
        x=0.5*np.sin(t)**2 + 2*np.cos(t)
    return np.array(x);

def main():
    t=np.linspace(-1,1,5000)
    y = []
    y=sincdemo(t);
    plt.figure(figsize=(20,10))
    plt.plot(t,y,'*')
    plt.grid(True)
    plt.show()
    plt.savefig("plot.png")
    
    
    
    
    
if __name__=="__main__":
    main()
    