a = int(input("Digite o Primeiro Valor: "))
b = int(input("Digite o Segundo Valor: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = "\nSoma: {}. \nSubtração: {}. \nMultiplicação: {}. \nDivisão: {}. \nResto: {}".format(soma, subtracao, multiplicacao, divisao, resto)
print(resultado)