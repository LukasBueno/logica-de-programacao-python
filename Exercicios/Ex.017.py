esc = 'S'

while esc == 'S':
    larg = float(input('Digite o valor da largura (m): '))
    alt = float(input('Digite o valor da altura (m): '))
    comp = float(input('Digite o valor do comprimento (m): '))
    print('O volume será {} m³'.format(comp*larg*alt))
    esc = str(input('Pressione "S" para continuar ou qualquer tecla para sair...')).strip().upper()[0]