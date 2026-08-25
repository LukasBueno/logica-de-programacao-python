cont = 1
neg = 0

while cont <= 5:
    var = int(input("Digite o um valor: "))

    if(var < 0):
        neg += 1

    cont += 1
print("Quantidade de valores negativos: {}".format(neg))
