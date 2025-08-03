'''
Desenvolva um programa para simular um simples sistema de vendas. Você deve solicitar
ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de
códigos abaixo a seguir para obter o preço da cada produto.

    Código    Preço
    1         5,50
    2         2,30
    3         4,75
    4         6,80
    5         9,30

O programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro
código deve gerar a mensagem de erro “Código inválido”.
'''
preco_total = 0

while True:
    entrada_codigo = int( input("Digite o código do produto: "))
    if (entrada_codigo == 0):
        break
    entrada_quantidade = int( input("Digite a quantidade do produto anterior: "))
    if (entrada_codigo < 0 or entrada_codigo > 5):
        print ("Código inválido.")
        continue
    elif (entrada_quantidade == 0):
        print("Quantidade inválida.")
        continue
    elif (entrada_codigo == 1):
        preco_total += 5.50 * entrada_quantidade
    elif (entrada_codigo == 2):
        preco_total += 2.30 * entrada_quantidade
    elif (entrada_codigo == 3):
        preco_total += 4.75 * entrada_quantidade
    elif (entrada_codigo == 4):
        preco_total += 6.80 * entrada_quantidade
    elif (entrada_codigo == 5):
        preco_total += 9.30 * entrada_quantidade
print (f'O valor total das compras foi {preco_total}.')
