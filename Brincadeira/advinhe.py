import math
import random

minimo = int(input("Qual o mínimo?:\n"))
maximo = int(input("Qual o máximo?:\n"))

x = random.randint(minimo, maximo)
print("\n\tVocê tem apenas ", round(math.log(maximo - minimo + 1, 2)),
      " chances de acertar!\n")

tentativas = 0

while tentativas < math.log(maximo - minimo + 1, 2):
  tentativas += 1
  chute = int(input("Qual o seu chute?:\n"))
  if x == chute:
    print("Parabéns você acertou em", tentativas, "tentativas!!")
    break
  elif x > chute:
    print("Você chutou muito baixo!")
  elif x < chute:
    print("Você chutou muito alto!")

if tentativas > math.log(maximo - minimo + 1, 2):
  print("\nO número era %d" % x)
  print("\tTente novamente!")