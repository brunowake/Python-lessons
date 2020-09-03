#lambda é uma função anonima
contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro','gato','elefante']
print(contador_letras(lista_animais))

soma = lambda a,b: a + b
subtracao = lambda a,b: a-b

print(soma(5,10))
print(subtracao(10,5))

calculadora = {
    'soma': lambda a, b: a+b,
    'subtracao': lambda a, b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisa': lambda a,b: a/b,
}
print(type(calculadora))
soma = calculadora['soma']
# soma = lambda a,b: a+b
print(soma(10,5))