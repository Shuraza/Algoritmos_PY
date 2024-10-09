import math

numeros = []

n = (int(input("Digite até que numero deseja a busca: "))) + 1

for i in range(n):
  numeros.append(True)
numeros[0] = False
numeros[1] = False

raiz = math.ceil(n**0.5)

for i in range(raiz):
  if numeros[i]:
    for j in range(i + i, n, i):
      numeros[j] = False

primos = []
for i in range(n):
  if numeros[i]:
    primos.append(i)

print(primos)
