alt, larg, comp, vol = 0, 0, 0, 0
def leitura():
    global alt, larg, comp
    alt = int(input('Qual a altura (m): '))
    larg = int(input('Qual a largura (m): '))
    comp = int(input('Qual a comprimento (m): '))

def volume(a, l, c):
    global vol
    vol = a * l * c

def resultado(v):
    print('O volume será {} m³'.format(v))

if __name__ == '__main__':
    leitura()
    volume(alt, larg, comp)
    resultado(vol)
