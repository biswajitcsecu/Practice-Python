
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

N = 500

def main():
    try:
        x = np.linspace(0,1,N)
        y =[]
        
        for i in x:
            y.append(np.sin(np.pi*i) /
                     + np.cos(np.pi*i)*(1+np.exp(i)/N))
        
        y = np.array(y)
        fig = plt.figure(figsize=(8,5), dpi=120)
        plt.plot(x,y, 'k', linewidth=2)
        plt.xlabel('$f_0$')
        plt.ylabel('$\sigma_{a_0}$')
        plt.grid(True)
        plt.show()
        plt.close(fig)
        
        
        
    except ZeroDivisionError:
        print('Error found')
        pass
    
    


if __name__ == "__main__":
    main()
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        