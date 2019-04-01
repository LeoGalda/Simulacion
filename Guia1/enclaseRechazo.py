import random
import matplotlib.pyplot as plt
import numpy as np

c = 2.11
cantidad = 500000
u = np.random.rand(cantidad)
x = 20 * u * ((1 - u)**3)
y = 1
p = x/(c * y)
z = []
for i in range(cantidad):
	r = random.random()
	if r < p[i]: #acepto		
		z.append(u[i])

plt.hist(z,100)
plt.show()