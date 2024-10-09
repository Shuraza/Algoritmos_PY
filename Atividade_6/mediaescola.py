
V = [9.9, 9.7, 9.8, 10, 10]

V.pop(V.index(max(V)))
V.pop(V.index(min(V)))

soma = sum(V)

media = (soma / len(V))

print(media)
print(V)
print(soma)
