# Lidando com Módulos, importação de classes, métodos e construção de funções anonimas

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora1
from aula8_contador_letras import contador_letras, teste

if __name__ == "__main__":
        
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora1(5,10)
    print(calculadora.soma())

    lista = ["Renata", "Lucas", "Bezinha", "Fuinha", "Nega"]
    print(contador_letras(lista))
    print(teste())