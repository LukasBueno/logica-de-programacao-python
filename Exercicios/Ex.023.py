import numpy as np

vetor_A = np.zeros(10, dtype=int)
vetor_B = np.zeros(10, dtype=int)

for i in range(0, 10):
    vetor_A[i] = input('Digite um valor para a posição {} do vetor: '.format(i))
    vetor_B[i] = vetor_A[i]**3

print("Primeiro vetor: ", vetor_A)
print("Segundo vetor: ", vetor_B)
