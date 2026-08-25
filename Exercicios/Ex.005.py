tempo = int(input('Digite o tempo gasto na viagem (h): '))
vel = int(input('Digite a velocidade média (km/h): '))

dist = vel * tempo
litros = dist / 12

print('Velocidade média: {} km/h'.format(vel))
print('Tempo: {} h.'.format(tempo))
print('Distância: {} km.'.format(dist))
print('Quantidade de litros: {} L'.format(litros))