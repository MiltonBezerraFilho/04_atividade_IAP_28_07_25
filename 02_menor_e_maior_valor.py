#Faça um programa que leia números repetidamente até que o valor -1 seja digitado. 
#Quando isso ocorrer, o programa deve exibir o menor valor, o maior valor e a soma dos 
#valores.

soma = 0
menor = 25 ** 9
maior = -2

while True:
    entrada = float( input("Digite um número: "))
    if (entrada == -1):
        break
    if (entrada > maior):
        maior = entrada
    if (entrada < menor):
        menor = entrada
if (maior == -2 and menor == 25 ** 9):
    print("Nehum número válido inserido.")
else: 
    soma = maior + menor
    print(f'A soma é {soma}')