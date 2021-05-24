a = int(input("Entre com o Primeiro Valor: "))
b = int(input("Entre com o Segundo Valor: "))

soma = a + b
sub = a - b
multi = a*b
divi = a/b
resto = a%b

resultado = ('Soma: {}. '
      '\nSubtração: {}. '
      '\nMultiplicação: {}. '
      '\nDivisão: {}.'
      '\nResto: {}'.format(soma, sub, multi, divi, resto))

print(resultado)
