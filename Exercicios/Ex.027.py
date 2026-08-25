import numpy as np
i, j = 0, 0
soma_linha, soma_coluna, soma_total = 0, 0, 0
matriz_A = np.zeros([4,4], dtype= int)

for i in range(0,4):
    for j in range(0,4):
        matriz_A[i][j] = int(input('Digite o valor para a posição a{}{} da matriz A: '.format(i+1,j+1)))
        soma_total += matriz_A[i][j]

print("\n"*50)
print('Matriz A:')
for i in range(0,4):
    for j in range(0,4):
        print(matriz_A[i][j],end=' ')
    print('\n')

for i in range(0,4):
    soma_linha += matriz_A[1][i]
    soma_coluna += matriz_A[i][1]

print('A somatória total dos elementos de A é: {}'.format(soma_total))
print('A somatória dos elementos da linha 2 de A é: {}'.format(soma_linha))
print('A somatória dos elementos da coluna 2 de A é: {}'.format(soma_coluna))
