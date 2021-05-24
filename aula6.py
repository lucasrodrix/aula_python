# #Aula 6 - Fundamentos em Python

# conjunto = {1,2,3,4}
# conjunto.add(5)
# conjunto.discard(3)
# print(conjunto)

conjunto1 = {1,2,3,4,5}
conjunto2 = {5,6,7,8,9}

conjuntoUniao = conjunto1.union(conjunto2)
print("União entre Conjunto 1 e 2: {}".format(conjuntoUniao))

conjuntoInter = conjunto1.intersection(conjunto2)
print("Intersecção entre o Conjunto 1 e 2: {}".format(conjuntoInter))

conjuntoDifer1 = conjunto1.difference(conjunto2)
conjuntoDifer2 = conjunto2.difference(conjunto1)
print("Diferença entre Conjunto 1 e 2: {}".format(conjuntoDifer1))
print("Diferença entre Conjunto 2 e 1: {}".format(conjuntoDifer2))

conjuntoDifeSimetr1 = conjunto1.symmetric_difference(conjunto2)
conjuntoDifeSimetr2 = conjunto2.symmetric_difference(conjunto1)
print("Diferença Simétrica entre Conjunto 1 e 2: {}".format(conjuntoDifeSimetr1))
print("Diferença Simétrica entre Conjunto 2 e 1: {}".format(conjuntoDifeSimetr2))

conjuntoA = {1,2,3}
conjuntoB = {1,2,3,4,5,6}

conjuntoSubset = conjuntoA.issubset(conjuntoB)
print("A é subconjunto de B: {}".format(conjuntoSubset))


conjuntoSuperset = conjuntoB.issuperset(conjuntoA)
print("B é um superconjunto de A: {}".format(conjuntoSuperset))

lista = ['cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjuntoAnimais = set(lista)
print(conjuntoAnimais)
listaAnimais = list(conjuntoAnimais)
print(listaAnimais)