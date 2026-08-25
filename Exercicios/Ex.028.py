import numpy as np
i, j = 0, 0
matriz_A = np.zeros([3,3], dtype= int)
matriz_B = np.zeros([3,3], dtype= int)
matriz_C = np.zeros([3,3], dtype= int)

for i in range(0,3):
    for j in range(0,3):
        matriz_A[i][j] = int(input('Digite o valor para a posição a{}{} da matriz A: '.format(i+1,j+1)))

print("\n"*50)

for i in range(0,3):
    for j in range(0,3):
        matriz_B[i][j] = int(input('Digite o valor para a posição b{}{} da matriz B: '.format(i+1,j+1)))

print("\n"*50)
print('Matriz A:')
for i in range(0,3):
    for j in range(0,3):
        print(matriz_A[i][j],end=' ')
    print('\n')

print('\nMatriz B:')
for i in range(0,3):
    for j in range(0,3):
        print(matriz_B[i][j],end=' ')
    print('\n')
print('\nMatriz C:')
for i in range(0,3):
    for j in range(0,3):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]
        print(matriz_C[i][j], end=' ')
    print('\n')
