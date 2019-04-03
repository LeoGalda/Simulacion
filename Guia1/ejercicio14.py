import random
import matplotlib.pyplot as plt
import numpy as np
import sys 

if len(sys.argv) < 4:
	print("pone bien los parametros salame")
	sys.exit(0)
cantidad = int(sys.argv[1])
a = int(sys.argv[2])
c = int(sys.argv[3])
u = np.random.random(cantidad)
x = 2 * a * (u - 0.5)
y = np.random.uniform(0,c,cantidad) 
z = []
for i in range(cantidad):
	value = 0	
	if ((x[i] >= -a) and (x[i] < 0)):
		value = (c/a) * x[i] + c
	elif ((x[i] < a) and (x[i] >= 0)):
		value = c - (c/a) * x[i]
	if (y[i] < value) :
		z.append(x[i])

plt.hist(z,100)
plt.show()

