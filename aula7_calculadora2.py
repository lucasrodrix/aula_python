# Aula 7 - Constuindo Métodos, funções e classes

# #Calculadora 2
class Calculadora2:

	def __init__(self):
		pass

	def soma(self, valorA, valorB):
		return valorA + valorB

	def subtracao(self, valorA, valorB):
		return valorA - valorB

	def multitplicacao(self, valorA, valorB):
		return valorA * valorB

	def divisao(self, valorA, valorB):
		return valorA / valorB

calculadora = Calculadora2()

print(calculadora.soma(10,2))
print(calculadora.subtracao(5,3))
print(calculadora.multitplicacao(10,5))
print(calculadora.divisao(100,2))

