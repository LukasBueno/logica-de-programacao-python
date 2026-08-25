qtd_total = float(input('Digite a quantidade total de parcelas: '))
qtd_paga = float(input('Digite a quantidade de parcelas pagas: '))
valor = float(input('Digite o valor da parcela: '))

total_pago = qtd_paga * valor
saldo = (qtd_total - qtd_paga) * valor

print('O valor pago até o momento é R$ {:.2f}'.format(total_pago))
print('O saldo devedor é R$ {:.2f}'.format(saldo))