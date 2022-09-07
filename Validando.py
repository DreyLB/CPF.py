from time import sleep
soma1 = 0
soma2 = 0
while True:
    cpf = str(input('Digite seu CPF (0 para sair): '))
    if cpf == '0':
        break
    for c in range(19):
        if c < 9:
            v1 = int(cpf[c]) * (10 - c)
            soma1 = soma1 + v1
        if c > 8:
            c -= 9
            v2 = int(cpf[c]) * (11 - c)
            soma2 = soma2 + v2
    
    while True:                                       #Digito 1
        if 11 - (soma1 % 11) > 9:
            if int(cpf[9]) == 0:
                print('Aguarde o fim da validação...')
            else:
                print('ERRO! CPF INVÁLIDO')
                break
        elif 11 - (soma1 % 11) == int(cpf[9]):
            print('Aguarde o fim da validação...')
        else:
            print('ERRO! CPF INVÁLIDO')
            break
        sleep(1)
        
        if 11 - (soma2 % 11) == int(cpf[10]):         #Digito 2
            print('CPF VÁLIDO')
            break
        else:
            print('ERRO! CPF INVÁLIDO')
            break
    soma1 *= 0
    soma2 *= 0
sleep(0.5)
print()
print('Fim da operação, volte sempre!')
