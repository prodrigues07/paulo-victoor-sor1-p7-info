# 1. Dada a string “A persistência é o caminho do êxito” codifique-a utilizando UTF-8
# e UTF-16.
# 1.1.O que acontece em cada caso? Justifique.
# 1.2.Qual a diferença de tamanho entre as saídas em UTF-8 e UTF-16?
# 1.3.Tente realizar a codificação/decodificação cruzada. O que acontece?

a = "A persistência é o caminho do êxito"
b = "A persistência é o caminho do êxito"
c = a.encode()
d = b.encode('utf-16')

print (c)
print ('')
print (d)
print ('')
print (c.decode())
print ('')
print (d.decode('utf-16'))