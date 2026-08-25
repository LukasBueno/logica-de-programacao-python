def leitura(msg):
    valor = float(input(msg))
    return valor
def distancia_calc (v, t):
    d = v * t
    return d

def litros_calc(di):
    l = di/12
    return l

def resultado(ve, te, de, li):
    print('\nVelocidade: {} Km/h'.format(ve))
    print('Tempo: {} h'.format(te))
    print('Distância: {} km'.format(de))
    print('Litros: {}'.format(li))

if __name__ == '__main__':
    velocidade = leitura('Digite a velocidade (km/h): ')
    tempo = leitura('Digite o tempo (h): ')
    distancia = distancia_calc(velocidade, tempo)
    litros = litros_calc(distancia)
    resultado(velocidade, tempo, distancia, litros)