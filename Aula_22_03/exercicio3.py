# Escrever um programa que informe ao usuário o maior e o menor elemento de uma
# lista e o valor médio dos elementos da lista. Utilize uma lista com 10 números.

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89, 88]
sampleList_inOrder = sorted(sampleList)

x = 0
i = 0

while i < len(sampleList_inOrder):
    x = x + sampleList_inOrder[i]
    i += 1

print (f'O maior valor é: {sampleList_inOrder[9]}')
print (f'O menor valor é: {sampleList_inOrder[0]}')
print (f'O valor médio da lista é: {x/2}')