import random
import matplotlib.pyplot as plt
import numpy as np

cantidad = 1000
x = np.random.rand(cantidad)
y = np.random.rand(cantidad)
colors = (0,0,0)	
area = np.pi * 3
plt.scatter(x, y, s = area, c = colors, alpha = 0.5)
plt.title('prueba de que es uniforme')
plt.show()
