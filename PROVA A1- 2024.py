n = int(input("Digite um número inteiro de 1 e 5: "))
x = 0
if n > 0:
  if n > 1:
    if n > 2:
      if n > 3:
        if n > 4:
          x = x + 16
        x = x + 8
      x = x + 4
    x = x + 2
  x = x + 1
print(" A sáida é %d" %x)


lista1 = [0, 1]
for i in range (2, 10):
  lista1.append(lista1[i - 1]+ lista1[i - 2])
print(lista1)


lista1 = []
n = 0
i = 0
while i < 10:
  n = n + 1
  propriedade = True
  for j in range(2, i):
    if n % j == 0:
      propriedade = False
  if propriedade:
      lista1.insert(i, n)
      i = i + 1
print(lista1)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
lista3 = []
for i in range(len(lista1)):
  if lista1[i] % 3 == 0:
    lista2.append(lista1[i])
  else:
    lista3.append(lista1[i])
print(lista1)
print(lista2)
print(lista3)


num = 0
while 1 > num or 100 <= num:
  num = int(input("Digite um número de 1 a 100: "))
  cont = 2
  tomatinho = True
while cont < num:
  if num % cont == 0:
    tomatinho = False
    cont = cont + 1
if tomatinho:
  print("O número %d apresenta a propriedade tomatinho." %num)
else:
  print("O número %d não apresenta a propriedade tomatinho." %num)
  
  
texto = input("Digite algumas palavras: ")
texto = texto.upper()
while texto != "":
  print(texto[0] + " - " + str(texto.count(texto[0])))
texto = texto.replace(texto[0], "")


preco = float(input("Qual o valor da compra? "))
prestacoes = int(input("Qual o número de prestações? "))
if prestacoes < 1 or prestacoes > 12:
  print("Número inválido de prestações.")
else:
  print("Cada parcela será de R$.2f" (preco / prestacoes))