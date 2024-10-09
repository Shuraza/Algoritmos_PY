V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 0
f = len(V) - 1
aux = 0

while i < f:
  aux = V[i]
  V[i] = V[f]
  V[f] = aux
  i += 1
  f -= 1
print(V)