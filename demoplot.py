

import numpy as np
import matplotlib.pyplot as plt

# make some data
x = np.linspace(0, 2*np.pi)

y1 = np.sin(x)
y2 = np.cos(x)

# plot sin(x) and cos(x)
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(x, y1, c='b', label='y1')
ax.plot(x, y2, c='r', label='y2')

leg = plt.legend()
# get the lines and texts inside legend box
leg_lines = leg.get_lines()
leg_texts = leg.get_texts()
# bulk-set the properties of all lines and texts
plt.setp(leg_lines, linewidth=4)
plt.setp(leg_texts, fontsize='x-large')
plt.savefig('leg_example')
plt.show()

















