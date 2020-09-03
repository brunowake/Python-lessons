class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('entre com uma nota de 0 a 10 \n'))
        print(x)
        if x > 10:
            raise InputError('nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor invalido. Digitar somente números')
    except InputError as ex:
        print(ex)