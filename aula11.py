
lista = [1,10]
arquivo = open('teste.txt','r')
try:
    divisao = 10 / 1
    numero = lista[1]

except ZeroDivisionError:
    print('nao pode dividir por 0')
except ArithmeticError:
    print('houve um erro de matematica')
except IndexError:
    print('erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('nao tem nenhum erro')
finally:
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()