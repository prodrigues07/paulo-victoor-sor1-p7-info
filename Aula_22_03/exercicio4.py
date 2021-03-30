# Escrever um programa em Python que remove os elementos duplicados de uma lista.

sampleList = [11, 22, 8, 23, 14, 11, 23, 14, 12, 78, 45, 88, 88]
print (sampleList)

i = 0
x = 1

while i < len(sampleList):
    while x < len(sampleList):
        if sampleList[i] == sampleList[x]:
            del sampleList[x]
        x += 1
    i += 1
    x = i + 1

print (sampleList)