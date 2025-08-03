'''
Implemente um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago. Exiba na tela o número de meses em que
a dívida será paga, o total pago e o total de juros pago
'''
divida = float( input("Digite o valor inicial da dívida: "))
juro_mensal = float( input("Digite o valor da porcentagem do juro mensal: "))
valor_mensal = float( input("Digite o valor mensal que será pago: "))
juro_mensal = juro_mensal / 100
meses = 0
juro = 0
total_pago = 0
juros_total = 0
pagamento = 0

while (divida > 0.001):
    juro = divida * juro_mensal
    divida += juro
    juros_total += juro
    if (valor_mensal < divida):
        pagamento = valor_mensal
    else:
        pagamento = divida
    divida -= pagamento
    total_pago += pagamento
    meses += 1
    if (meses > 1000):
        break
print (f'A dívida foi paga em {meses} meses \n com R${total_pago} como o total pago \n e com R${juros_total} como juros total.')