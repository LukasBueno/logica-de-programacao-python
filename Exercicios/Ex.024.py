import numpy as np

vetor_A = np.zeros(10, dtype=int)

soma = 0
neg = 0
for i in range(0, 10):
    vetor_A[i] = int(input('Digite um valor: '))
    soma += vetor_A[i]
    if vetor_A[i] < 0:
        neg += 1
print('A somatória dos valores do vetor é: {}'.format(soma))
print('A quantidade de termos negativos é: {}'.format(neg))
print("A média dos valores é: {}".format(soma / 10))
