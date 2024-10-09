
A = [1, 3, 5, 6, 7, 9, 13]
B = [0, 2, 4, 8, 10, 11, 12]
C = []
i = 0
j = 0
acontece = True
aux = ""

while i < len(A) and j < len(B):
  if A[i] < B[j]:
    C.append(A[i])
    i += 1
  else:
    C.append(B[j])
    j += 1

while i < len(A):
  C.append(A[i])
  i += 1
while j < len(B):
  C.append(B[j])
  j += 1

print(C)
