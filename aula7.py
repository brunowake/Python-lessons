#por convenção metodo nao tem retorno e função tem retorno
class Calculadora:
    def __init__(self, numero1, numero2):
        self.a = numero1
        self.b = numero2
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

calculadora = Calculadora(int(input('informa o valor a')),int(input('insira o valor b')))

print('valor do a {}'.format(calculadora.a))
print('valor do b {}'.format(calculadora.b))
print('valor da soma {}'.format(calculadora.soma()))
print('valor da subtração {}'.format(calculadora.subtracao()))
print('valor da multiplicação {}'.format(calculadora.multiplicacao()))
print('valor da divisão {}'.format(calculadora.divisao()))