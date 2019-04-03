#preguntar porque no se resolverlo
import random
import matplotlib.pyplot as plt
import numpy as np

cantidad = 200
alfa = np.random.random(cantidad)
beta = np.random.random(cantidad)
u = np.random.random(cantidad)
y = alfa * u + beta
yValido = []
alfaValido = []
betaValido = []
for i in range(cantidad):
	if ( (y[i] > -5) and (y[i] < 15)):
		yValido.append(y[i])
		alfaValido.append(alfa[i])
		betaValido.append(beta[i])
# 	media = getMedia(x,n[j])
# 	varianza = getVarianza(x,n[j])
