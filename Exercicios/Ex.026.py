import numpy as np
i, j = 0, 0
matriz_A = np.zeros([3,3], dtype= int)

for i in range(0,3):
    for j in range(0,3):
        matriz_A[i][j] = int(input('Digite o valor para a posição a{}{} da matriz A: '.format(i+1,j+1)))

print("\n"*50)
print('Matriz A:')
for i in range(0,3):
    for j in range(0,3):
        print(matriz_A[i][j],end=' ')
    print('\n')

val = int(input('Digite o valor que será procurado: '))

for i in range(0,3):
    for j in range(0,3):
        if matriz_A[i][j] == val:
            print('O valor {} foi encontrado na posição a{}{} da matriz A.'.format(val,i+1,j+1))
