#ver porque no parece una gaussiana
import random
import matplotlib.pyplot as plt
import numpy as np
import math

cantidad = 500
u = np.random.random(cantidad)
u2 = np.random.random(cantidad)
z = []
for i in range(cantidad):
	x = -math.log(u[i])
	if (u2[i] < (math.e**(-((x - 1)**2)))):
		if (u[i] < 0.5):
			z.append(-x)
		else:
			z.append(x)
plt.hist(z,100)
plt.show()