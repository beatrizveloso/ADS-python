# 1- Crie um programa em Python que solicite ao usuário a sua idade e mostre se ele pode ter CNH.

idade = int(input("Qual é a sua idade? "))
if idade >= 18:
    print("Parabéns! Você já pode tirar sua CNH!")

# 2- Escreva um programa em Python que solicite um número inteiro ao usuário e mostre caso o mesmo seja par.

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(f"O número {num} é par.")

# 3- Crie um programa em Python que solicite ao usuário três valores inteiros (A, B e C) e verifica se o valor armazenado em B é o menor.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if b < a and b < c:
    print("O menor valor é B.")
else:
    print("B não é o menor valor.")

# 4- Crie um programa em Python que solicite ao usuário a sua idade e mostre se o mesmo pode ou não ter CNH.

idade = int(input("Qual é a sua idade? "))
if idade >= 18:
    print("Parabéns! Você já pode tirar sua CNH!")
else:
    print("Você ainda não pode tirar sua CNH.")

# 5- Crie um programa em Python que solicite ao usuário um número e informe se o mesmo é par ou ímpar.

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")

# 6- Crie um programa em Python que solicite duas notas de um aluno ao usuário, calcule a média e mostre se o mesmo está aprovado (média >= 6.0) ou reprovado caso contrário.

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1 + n2) / 2

if media >= 6.0:
    print(f"Aprovado com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")

# 7- Faça um programa que solicite ao usuário um número inteiro, calcule e mostre a raiz quadrada desse número. 
# O programa deverá verificar antes se o número digitado é positivo, exibindo uma mensagem de alerta caso seja negativo.

import math

num = float(input("Digite um número: "))
if num >= 0:
    r = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {r:.2f}.")
else:
    print("Não é possível calcular raiz quadrada real de números negativos.")
