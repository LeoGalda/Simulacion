#! usr/bin/python

class GCL:

	multiplicador = 0
	incremento = 0
	modulo = 0
	semilla = 0	
	valores = []
	base = 1

	def __init__(this,mult,incremento,modulo,semilla):
		this.multiplicador = mult
		this.incremento = incremento
		this.modulo = modulo
		this.semilla = semilla

	def getSemilla(this):
		return this.semilla

	def getMultiplicador(this):
		return this.multiplicador

	def getModulo(this):
		return this.modulo

	def getIncremento(this):
		return this.incremento

	def getValores(this):
		return this.valores

	def clearValores(this):
		this.valores = []

	def setBase(this,base_):
		this.base = base_	

	def calcularValores(this,cantidad):
		numeroR = this.semilla		
		for x in range(cantidad):			
			numeroR = (numeroR * this.multiplicador + this.incremento) % this.modulo
			this.valores.append(float(numeroR) / float(this.base))			

	def imprimirValores(this):
		print(this.valores)