#***Imprimindo com aspas simples, duplas e triplas***
#%d=  é inteiro %s=  string e %f = ponto flutuante
print('Imprimindo com aspas simples')
print("Imprimindo com aspas duplas")
print("""Imprimindo com aspas
Assim eu posso
pular linhas,
várias linhas!""")
print("Com aspas duplas ou simples podemos usar o barra-n \n para pular linha.")
fruta = 'banana'
letra = fruta[1]
print('O caractere na posição 1 de banana é ', letra)
#O zero é a posição 1 - referente ao B


# Exemplo 1
texto = input("Digite um número inteiro: ")
tamanho = len(texto)
print("O número informado em %d dígitos" % tamanho)

numero = int(texto)
tamanho = len(str(numero))
print("O número informado em %d dígitos" % tamanho)

# Exemplo 2 - leia uma string e imprima a inversa dela

texto = input("Digite um texto: ")
invertida = ""
for letra in texto:
  invertida = letra + invertida
print(invertida)

# Exemplo 3

s = "ALE"
b = "LU"
print(s + b + "IA")
idade = 18
print("João tem %d anos de idade " % idade)
print("João tem %5d anos de idade " % idade)
# O número antes do "d" significa o espaçamento
numero = 12.34
print("%f" % numero)
print("%.3f" % numero)
print("%8.3f" % numero)
print("%08.3f" % numero)

# Exemplo 4

nome = "Wagner Moura"
idade = 47
print("%s tem %d anos de idade " % (nome , idade))
print(f"{nome} tem {idade} anos de idade.")
print("{} tem {} anos de idade".format(nome, idade))

# Exemplo 5- Faça um programa que solicite o valor de um produto e exiba o valor acrescido de 5%. A saída deverá exibir o valor no formato: R$ xx.xx

valor = float(input("Qual o valor do produto em reais? "))
percentual = float(input("Qual o percentual de acréscimo? "))
valorNovo = valor * (1 + percentual / 100)
print("O valor total da compra é R$%.2f com acréscimo de %.1f%% é R$%.2f" % (valor , percentual, valorNovo))
print(f"O valor R${valor:.2f} com acréscimo de {percentual:.1f}% é R${valorNovo:.2f}")
print("O valor R${:.2f} com acréscimo de {:.1f}%% é R${:.2f}".format(valor , percentual, valorNovo))

# Exemlo 6-Crie um programa que leia um úmero inteiro digitado pelo usuário e imprima seu inverso

numero = input("Digite algo: ")
print(numero[::-1])

# Exemplo 7

a = "Fizeram a atividade? "
print(a.replace("atividade","exercício"))
print(a)
a = a.replace("atividade", "tarefa")
print(a)
print(a.lower()) #tudo minúsculo
print(a.upper()) #tudo maíusculo

# Exemplo 8

texto = input("Digite uma frase: ")
lista = texto.split()
print(lista)
print("A frase tem %d palavras." % len(lista))






