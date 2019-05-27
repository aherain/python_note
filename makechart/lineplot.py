import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100) #在横坐标0到2，之间绘制100个点，连成线

plt.plot(x, x, label = 'linear')
plt.plot(x, x**2, label = 'quadratic')
plt.plot(x, x**3, label = 'cubic')


plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')

plt.legend()
plt.show()
