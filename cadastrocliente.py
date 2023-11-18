import random
from datetime import datetime 

print('--------Olá, bem-vindo a nossa empres! -----------')

#OBTENHA NOME E IDADE DO USUÁRIO 
nome_usuario = input('Digite seu nome: ')
idade_usuario = int(input('Digite sua idade: '))

#REGISTRO AUTOMÁTICO DA DATA 
data_cadastro = datetime.now()
 
#CARTÕES SORTEADOS 
cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00', ]
cartao_sorteio = random.choice(cartoes)

#DATA DE ANIVERSÁRIO
data_aniver = datetime.strptime(input('Digite a data do seu próximo aniversário(dd-m-aaaa): '), '%d-%m-%Y')
dias_para_aniver = data_aniver - data_cadastro

#OUTPUT
print('------Dados de cadastrados!-------')
print(f'Nome: {nome_usuario}')
print(f'Idade: {idade_usuario}')
print(f'Data de cadastro: {data_cadastro}')
print(f'Cartão sorteado: {cartao_sorteio}')
print(f'Seu próximo aniversário será em: {dias_para_aniver.days} dias.')

#APRESENTAÇÃO DO USUÁRIO
print('---------Dados cadastrados corretamente!----------')
print(f'Olá {nome_usuario}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}. \
\nParabéns, houve um sorteio e você ganhou um cartão no valor de {cartao_sorteio}.')
