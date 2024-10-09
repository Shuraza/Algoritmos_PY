V = []
nomes = open('Atividade_1/nomes.txt')
for i in nomes:
  V.append(i.strip())
nomes.close()

acontece = True
aux = ""

while acontece:
  acontece = False
  for i in range(len(V) -1):
    if V[i] > V[i + 1]:
      aux  = V[i]
      V[i] = V[i + 1]
      V[i + 1] = aux
      acontece = True
print (V)
