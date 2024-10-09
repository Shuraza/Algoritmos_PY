V = []

for i in range(0 ,602, 2):
  V.append(i)
n = int(input('Buscar qual valor?'))
tentativa = 0
ini = 0
fim = len(V)
achou = False
meio = 0

while ini <= fim and not achou:
  tentativa += 1
  meio = (fim + ini) // 2
  if V[meio] == n:
    achou = True
  elif V[meio] < n:
   ini = meio + 1
  else:
   fim = meio - 1
 
print(meio, tentativa)
