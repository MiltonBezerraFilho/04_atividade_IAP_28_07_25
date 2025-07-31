'''
Escreva um programa que leia dois números e imprima o resultado da divisão inteira do 
primeiro pelo segundo, assim como o resto da divisão, usando o comando while e o 
operador aritmético de subtração. Lembre-se que podemos entender o quociente da 
divisão de dois números como a quantidade de vezes que podemos retirar o divisor do 
dividendo. Logo, 20 ÷ 4 = 5, pois podemos subtrair 4 cinco vezes de 20.  
'''

primeiro_num = int( input("Digite o primeiro número: "))
segundo_num = int( input ("Digite o segundo número: "))
resto = primeiro_num
divisoes = 0

if (segundo_num == 0):
    print("Erro matemático.")
else:
    while (resto >= segundo_num):
        resto -= segundo_num
        divisoes += 1
print(f'O resultado é {divisoes} com resto {resto}.')
