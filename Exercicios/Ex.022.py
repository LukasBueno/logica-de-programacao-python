import numpy as np

procurado = False
vetor_A = np.zeros(10, dtype=int)

valor = int(input('Digite um valor a ser procurado: '))

for c in range(0, 10):
    vetor_A[c] = int(input('Digite um valor para a posição {} do vetor: '.format(c)))
    if vetor_A[c] == valor:
        procurado = True

if procurado == True:
    print("Achei!")
else:
    print("Não achei!")
