def leitura():
    v = int(input('Digite um numero inteiro qualquer: '))
    return v

def verifica(n):
    if n > 0:
        return True
    else:
        return False
if __name__ == '__main__':
    valor = leitura()
    cond = verifica(valor)
    print("O número é positivo? {}".format(cond))
