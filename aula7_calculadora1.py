# Aula 7 - Constuindo Métodos, funções e classes

class Calculadora1:

	def __init__(self, n1, n2):
		self.valorA = n1
		self.valorB = n2

	def soma(self):
		return self.valorA + self.valorB

	def subtracao(self):
		return self.valorA - self.valorB

	def multitplicacao(self):
		return self.valorA * self.valorB

	def divisao(self):
		return self.valorA / self.valorB

calculadora = Calculadora1(10,5)

print(calculadora.valorA)
print(calculadora.valorB)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multitplicacao())
print(calculadora.divisao())