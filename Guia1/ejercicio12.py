import random
import matplotlib.pyplot as plt
import numpy as np

cantidad = 500000
x = np.random.rand(cantidad)
z = []
for i in range(cantidad):
	y = random.random()
	if y < x[i]: #acepto		
		z.append(x[i])

plt.hist(z,100)
plt.show()