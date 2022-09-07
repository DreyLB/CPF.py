import random
#from Avançando import linha
#from time import sleep
#linha('GERANDO UM NOVO CPF')
#sleep(0.5)
soma1 = 0
soma2 = 0
cont = 0
while True:
    cpf = str(random.randint(10000000000, 99999999999))
    novo = cpf[:-2]
    for c in range(19):
        if c < 9:
            v1 = int(cpf[c]) * (10 - c)
            soma1 = soma1 + v1
        if c > 8:
            c -= 9
            v2 = int(cpf[c]) * (11 - c)
            soma2 = soma2 + v2
    #Digito 1
    if 11 - (soma1 % 11) > 9:
        novo += '0'
    elif 11 - (soma1 % 11) <= 9:
        novo += str(11 - (soma1 % 11))
    #Digito 2
    novo += str(11 - (soma2 % 11))
    soma1 *= 0
    soma2 *= 0
    cont += 1
    if novo == cpf:
#        linha(f'CPF VÁLIDO: {cpf}')
        print(f'CPF VÁLIDO: {cpf}')
        break
#linha(f'{cont} TENTATIVAS')
print(f'{cont} Tentativas')