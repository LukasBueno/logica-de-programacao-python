idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 12:
    print('Você é uma criança com {} anos.'.format(idade))
elif idade > 12 and idade < 18:
    print('Você é um adolescente com {} anos.'.format(idade))
elif idade >= 18:
    print('Você é um adulto com {} anos.'.format(idade))
else:
    print('Idade inválida!')