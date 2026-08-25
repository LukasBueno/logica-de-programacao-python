neg = 0

for cont in range(1,6):
    val = int(input('Digite um valor: '))
    if val < 0:
        neg = neg + 1
print('A quantidade de valores negativos é: {}'.format(neg))
