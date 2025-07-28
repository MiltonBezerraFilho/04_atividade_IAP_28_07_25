# Escreva um programa que efetue a soma de todos os números ímpares que são múltiplos 
# de três e que se encontram no conjunto dos números de 1 até 500.

numero = 1
soma = 0

while (numero < 501):
    numero += 1
    if (numero % 2 != 0):
        soma = soma + numero
print(f'A soma é {soma}')