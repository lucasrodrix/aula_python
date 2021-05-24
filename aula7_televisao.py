# Aula 7 - Constuindo Métodos, funções e classes
# Televisão
class Televisao:
	def __init__(self):
		self.ligada = False
		self.canal = 5

	def power(self):
		if self.ligada:
			self.ligada = False
		else:
			self.ligada = True

	def aumentaCanal(self):
		if self.ligada:
			self.canal += 1

	def diminuiCanal(self):
		if self.ligada:
			self.canal -= 1

if __name__ == '__main__':
	televisao = Televisao()
	print("A TV está Ligada: {}".format(televisao.ligada))
	televisao.power()
	print("A TV está Ligada: {}".format(televisao.ligada))
	print("Canal: {}".format(televisao.canal))
	televisao.aumentaCanal()
	televisao.aumentaCanal()
	print("Canal: {}".format(televisao.canal))
	televisao.power()
	televisao.aumentaCanal()
	print("A TV está Ligada: {}".format(televisao.ligada))
	print("Canal: {}".format(televisao.canal))