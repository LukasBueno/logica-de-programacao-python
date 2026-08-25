num = 0
def leitura(msg):
    global num
    num = int(input(msg))

def verifica(n):
    if n < 0:
        print('É negativo!')
    else:
        print('É positivo!')

if __name__ == '__main__':
    leitura('Digite um numero inteiro qualquer: ')
    verifica(num)