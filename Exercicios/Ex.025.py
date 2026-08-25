import numpy as np
nomes = np.empty(5, dtype= object)
notas = np.zeros(5, dtype=float)

for n in range(0, 5):
    nomes[n] = str(input("Digite o nome do aluno(a): "))
    notas[n] = float(input("Digite a nota do(a) {}: ".format(nomes[n])))

for n in range(0, 5):
    print('A nota do(a) {} é: {}'.format(nomes[n], notas[n]))