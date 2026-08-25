med = 0.0
cont = 1

while cont <= 2:
    if cont == 1:
        n1 = float(input('Digite a primeira nota: '))

        if 0 <= n1 <= 10:
            cont += 1
    if cont == 2:
        n2 = float(input('Digite a segunda nota: '))

        if 0 <= n2 <= 10:
            cont += 1
med = (n1 + n2) / 2
print('A média será: ', med)