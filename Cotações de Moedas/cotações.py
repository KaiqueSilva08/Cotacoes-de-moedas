import requests

#Cores para melhorar o visual.
cores = ['\033[m',          #0 - NDA
         '\033[30;46m',     #1 - PRETO E CIANO
         '\033[30;47m'      #2 - PRETO E BRANCO
         ]

#Tentando consumir os valores das moedas por meio de uma API.
try:
    moedas = requests.get('https://economia.awesomeapi.com.br/json/last/USD,EUR,BTC')

except:
    print('Erro, site awesomeAPI está fora do ar! :(')

else:
    moedas = moedas.json()          #Transformando em valores manipulaveis.

    #Filtrando cada moeda e transformando em float.
    usd = moedas['USDBRL']['bid']
    usd = float(usd)

    eur = moedas['EURBRL']['bid']
    eur = float(eur)

    btc = moedas['BTCBRL']['bid']
    btc = float(btc)

    #Filtrando data e hora para pegar apenas a data.
    date = moedas['USDBRL']['create_date']
    date = date.split(' ')
    date = date[0]

    #Tranformando a formatação da data no modelo que conhecemos ex: dia/mês/ano.
    date = date.split('-')
    data = list()

    cont = 2
    while cont >= 0:
        data.append(date[cont])
        cont -= 1

    #Deletando variavel date após data receber dia/mês/ano.
    del date
    data = '/'.join(data)

    #Titulo
    print(cores[2], end='')
    print('=' * 45)
    print('Cotações De Moedas'.center(45))
    print('=' * 45)

    #Conteúdo do programa formatado.
    print(f'Ultima atualização: {data:>25} \n')
    print(f'Dollar = {f"R${usd:.2f}":<}')
    print(f'Euro = {f"R${eur:.2f}":<}')
    print(f'Bitcoin = {f"R${btc:.2f}":<}')
    print('=' * 45)
    print(cores[0], end='')
