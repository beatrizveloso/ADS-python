# Faça um programa em Python que solicite um número binário, faça a conversão e exiba o número digitado na base decimal

binario = input("Digite um número binário: ")
potencia = len(binario) - 1
decimal = 0
for digito in binario:
  decimal = decimal + int(digito) * 2 ** potencia
  potencia = potencia - 1
print("A conversão do binário %s para decimal e %d." % (binario, decimal))

# Faça um algoritmo que calcula e mostra a média entre duas notas de 10 alunos

contador = 1
while contador <= 10:
  nota1= float(input("Digite a primeira nota do aluno %d: " % contador))
  nota2= float(input("Digite a segunda nota do aluno %d: " % contador))
  media = (nota1 + nota2) / 2
  print("A média do aluno é %d é %.1f." % (contador, media))
  contador += 1


contador = 1
mediaDaSala = 0
while contador <= 10:
  nota1= float(input("Digite a primeira nota do aluno %d: " % contador))
  nota2= float(input("Digite a segunda nota do aluno %d: " % contador))
  media = (nota1 + nota2) / 2
  mediaDaSala += media
  print("A média do aluno é %d é %.1f." % (contador, media))
  contador += 1
mediaDaSala /= contador - 1
print("A média da sala é %.1f." % mediaDaSala)


contador = 0
soma = 0
resp = "s"
while resp =="s" or resp =="S":
  numero = float(input("Digite um número: "))
  soma += numero
  contador += 1
  resp = input("Deseja continuar (S/N)? ")
media = soma / contador
print("A média dos números digitados é %f." % media)


#Exemplo prof
contador = 0
soma = 0
numero = 0
while numero != -1:
  numero = float(input("Digite um número: (-1 para terminar) "))
  if numero != -1:
    soma += numero
    contador += 1
media = soma / contador
print("A média dos números digitados é %f. " % media)