#F(x) = { -5/4x^-1 + 5/4}
import random
import matplotlib.pyplot as plt
import numpy as np

cantidad = 50000
u = np.random.rand(cantidad)
x = 1/((-0.8) * u + 1)

plt.hist(x)
plt.show()