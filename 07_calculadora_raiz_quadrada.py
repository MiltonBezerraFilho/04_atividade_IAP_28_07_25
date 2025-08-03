'''
Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de
Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada,
considere o valor inicial para a base b = 2 e calcule p usando a fórmula p = (b + n/b)/2. A
cada passo, faça b = p e recalcule p usando a fórmula apresentada. Pare quando a
diferença absoluta entre b e p for menor que 0,0001. Os valores de b e p representam o
valor da raiz quadrada do número informado. Exiba-os na tela. Dica: A função abs()
calcula o valor absoluto de um número passado por parâmetro. Ex.: abs(-10) resulta
em 10.
'''

n = float( input("Digite o número que será colocado na raiz quadrada: "))
b = 2
p = 02

while abs(b - p > 0.0001):
    p = (b + n/b)/2
    b = p
print (f"O resultado é {b}.")