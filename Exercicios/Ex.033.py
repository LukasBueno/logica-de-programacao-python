idade = 0
def leitura(msg):
    global idade
    idade = int(input(msg))

def verifica(n):
    if 0 <= n <= 12:
        print('É criança!')
    elif 12 <= n <= 17:
        print('É adolescente!')
    elif n >= 18:
        print('É adulto!')
    else:
        print('Idade invalida!')

if __name__ == '__main__':
    leitura('Digite uma idade: ')
    verifica(idade)