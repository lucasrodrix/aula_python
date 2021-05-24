#Aula 5 - Python Digital Innovation One

lista = [10,32,75,7]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animais[0] = 'macaco'
print(lista_animais)

tupla = (1,10,12,14)
# tupla[0] = 2
print(len(tupla))
print(len(lista_animais))

tupla_animais = tuple(lista_animais)
print(type(tupla_animais))
print(tupla_animais)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

# lista.sort()
# lista_animais.sort()

# print(lista)
# print(lista_animais)

# lista_animais.reverse()
# print(lista_animais)

# if 'lobo' in lista_animais:
# 	print('animal existe na lista')
# else:
# 	print('animal não existe na lista')
# 	lista_animais.append('lobo')
# 	print(lista_animais)

# # lista_animais.pop(1)
# lista_animais.remove('elefante')
# print(lista_animais)