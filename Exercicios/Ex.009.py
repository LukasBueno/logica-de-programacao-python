n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('='*20)
print('(+) Soma;')
print('(-) Subtrair;')
print('(*) Multiplicar;')
print('(/) Dividir;')
print('='*20)
esc = str(input('Digite a sua escolha: '))

if esc == '+':
    print('Soma: ', n1 + n2)
elif esc == '-':
    print('Subtração: ', n1 - n2)
elif esc == '*':
    print('Multiplicação: ', n1 * n2)
elif esc == '/' and n2 != 0:
    print('Divisão: ', n1 / n2)
elif esc == '/' and n2 == 0:
    print("O segundo valor não pode ser zero!")
if esc != '+' and esc != '-' and esc != '*' and esc != '/':
    print('Escolha inválida!')
