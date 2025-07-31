'''
Supondo que a população de um país X seja da ordem de 70.000 habitantes com uma taxa 
anual de crescimento de 3.5% e que a população de Y seja 180.000 habitantes com uma 
taxa de crescimento de 1.5%. Escreva um programa que calcule e escreva o número de 
anos necessários para que a população do país X ultrapasse ou iguale a população do país 
Y, mantidas as taxas de crescimento.  
'''
populacao_x = 70000
populacao_y = 180000
anos = 0
taxa_x = 0.035
taxa_y = 0.015

while (populacao_x <= populacao_y):
    anos += 1
    populacao_x += populacao_x * taxa_x
    populacao_y += populacao_y * taxa_y
print(f'Levaram {anos} anos para X superar ou igualar a Y.')
