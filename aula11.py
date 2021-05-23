#Aula 11 - Gerenciando e criando exceções customizadas com try, except, else e finally

lista = [1,10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    div = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por Zero')
except ArithmeticError:
    print("Houve um erro ao realizar uma operação aritmética")
except IndexError:
    print('Erro ao Acessar um Índice Inválido da Lista')
except Exception as ex:
    print('Erro Desconhecido: {}'.format(ex))
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre Executa")
    print('Fechando o Arquivo')
    arquivo.close()
