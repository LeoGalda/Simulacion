import matplotlib.pyplot as plt
from GCL import GCL

modulo = 2**32
multiplicador = 1013904223
incremento = 1664525
padrones = [92060,92974,95358]
pesos = [0.15,0.25,0.6]
semilla = int(( pesos[0] * padrones[0] + pesos[1] * padrones[1] + pesos[2] * padrones[2]) / sum(pesos))
cantidadDeNumerosAMostrar = 5
gcl = GCL(multiplicador,incremento,modulo,semilla)

#punto A
gcl.calcularValores(cantidadDeNumerosAMostrar)	
gcl.imprimirValores()

#punto B
cantidadDeNumerosParaHistograma = 100000
gcl.setBase(modulo)
gcl.clearValores()
gcl.calcularValores(cantidadDeNumerosParaHistograma)
plt.hist(gcl.getValores())
plt.show()