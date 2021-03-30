# Escrever um programa em Python em que dada uma lista com números inteiros,
# retorna uma nova lista com os números ímpares (ou pares) contidos nesta lista.

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89, 88]
sampleList_even = []
sampleList_odd = []

i = 0
resto = 0

while i < len(sampleList):
    if sampleList[i] % 2:
        sampleList_odd.append(sampleList[i])
    else:
        sampleList_even.append(sampleList[i])
    i += 1

even_inOrder = sorted(sampleList_even)
odd_inOrder = sorted(sampleList_odd)

print(f'Lista Par: {even_inOrder}')
print(f'Lista Ímpar: {odd_inOrder}')