import numpy as np
i = 0
vetor_A = np.zeros(10, dtype=int)

val = int(input('Digite um valor a ser procurado: '))

for i in range(0, 10):
    vetor_A[i] = int(input('Digite um valor para a posição {} do vetor: '.format(i)))
for i in range(0, 10):
    if vetor_A[i] == val:
        print('O valor procurado {} foi encontrado na posição: {}'.format(val, i))
