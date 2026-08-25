def leitura(msg):
    valor = float(input(msg))
    return valor

def media(v1, v2, v3):
    med = (v1 + v2 + v3)/3
    return med

def resultado(m):
    print('O valor da média será: {}'.format(m))

if __name__ == '__main__':
    valor1 = leitura('Digite o primeiro valor: ')
    valor2 = leitura('Digite o segundo valor: ')
    valor3 = leitura('Digite o terceiro valor: ')

    media_calc = media(valor1, valor2, valor3)
    resultado(media_calc)
