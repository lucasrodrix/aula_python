# Trabalhando com Datas

from datetime import date, datetime, time, timedelta

def trabalhandoComDate():    
    dataAtual = date.today()
    dataAtualStr = (dataAtual.strftime('%A - %d.%b.%Y'))
    print(type(dataAtual))
    print(type(dataAtualStr))

def trabalhandoComTime():
    horario = time(hour=15, minute=18, second=30)
    horarioStr = horario.strftime('%H:%M:%S')
    print(type(horario))
    print(type(horarioStr))

def trabalhandoComDatetime():
    dataAtual = datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%d/%m/%y'))
    print(dataAtual.strftime('%H:%M:%S'))
    print(dataAtual.strftime('%d/%m/%Y %H:%M:%S'))
    print(dataAtual.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[dataAtual.weekday()])

    dataCriada = datetime(2018, 6, 22 , 22, 30, 40)
    print(dataCriada)
    print(dataCriada.strftime('%c'))

    dataString = '01/01/2020 12:21:22'
    dataConvertida = datetime.strptime(dataString,'%d/%m/%Y %H:%M:%S')
    print(dataConvertida)

    novaData = dataConvertida + timedelta(days=365)
    print(novaData)
    novaData = dataConvertida - timedelta(hours=2)
    print(novaData)
    



if __name__ == '__main__':
    # trabalhandoComDate()
    # trabalhandoComTime()
    trabalhandoComDatetime()