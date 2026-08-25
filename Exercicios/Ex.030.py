c = 0
f = 0

def leitura():
    global c
    c = float(input('Digite a temperatura em graus Celsius: '))

def conversor():
    global f
    f = (c * 9 + 160) / 5

def resultado():
    print('A temperatura {} em graus celsius será {} graus fahrenheit.'.format(c, f))

if __name__ == '__main__':
    leitura()
    conversor()
    resultado()
