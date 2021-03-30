# Escrever um programa para somar todos os elementos de uma lista de números.

l = [10, 20, 30]

x = 0
y = 0

while y < len(l):
    x = x + l[y]
    y += 1

print (f'A soma total da Lista é: {x}')