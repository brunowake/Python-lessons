from aula7_televisao import Televisao
from aula7_calculadora2 import Calculadora
from aula8_contador_letras import contador_letras,teste

if __name__ == '__main__':
    calculadora = Calculadora()
    televisao = Televisao()

    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    print(calculadora.soma(10,20))
    lista = ['cachorro', 'gato','elefante']
    print('total de letras por palavras {}'.format(contador_letras(lista)))
    teste()