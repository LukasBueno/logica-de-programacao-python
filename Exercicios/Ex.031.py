tempo, velocidade, dist, lit = 0, 0, 0, 0
def leitura():
    global tempo, velocidade
    tempo = int(input('Tempo de viagem (h): '))
    velocidade = int(input('Velocidade média (km/h): '))

def distancia():
    global velocidade, dist
    dist = velocidade * tempo
def litros():
    global dist, lit
    lit = dist / 12

def resultado():
    print('Velocidade média: {} km/h'.format(velocidade))
    print('Tempo: {} h'.format(tempo))
    print('Distância: {} km'.format(dist))
    print('Litros: {} L'.format(lit))

if __name__ == '__main__':
    leitura()
    distancia()
    litros()
    resultado()