from datetime import date,datetime,time, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:30:32'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))
    nova_dadta = data_convertida - timedelta(days=365, hours=2, minutes=5)
    print(nova_dadta)


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A-%B-%Y')
    print(data_atual_str)
    print(type(data_atual))

def trabalhando_com_time():
    horario = time(hour=15,minute=18,second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(type(horario))
    print(horario_str)
    print(type(horario_str))
if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()