#por convenção metodo nao tem retorno e função tem retorno
class Calculadora:
    # def __init__(self):
    #     pass
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b
if __name__ == '__main__':

    calculadora = Calculadora()


    print('valor da soma {}'.format(calculadora.soma(10,2)))
    print('valor da subtração {}'.format(calculadora.subtracao(10,2)))
    print('valor da multiplicação {}'.format(calculadora.multiplicacao(50,50)))
    print('valor da divisão {}'.format(calculadora.divisao(100,3)))