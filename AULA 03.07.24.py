# Aula do curso de python
   
# 1. Primeiros Passos   
print("Sua idade é 18 anos")
print("Sua altura é 1,60 cm")

nome = "Beatriz Veloso"
idade = 18  # Integer
altura = 1.60  # Float

print("Olá, " + nome + "!")
print("Sua idade é " + str(idade) + " anos")
print("Sua altura é " + str(altura) + " cm")

print(f"Olá, {nome}!")
print(f"Sua idade é {idade} anos")
print(f"Sua altura é {altura} cm")

# 2. Declaração de Variáveis
nome = "Beatriz Veloso"  # String
idade = 18  # Integer
altura = 1.60  # Float

print(nome)
print(idade)
print(altura)

# Type serve para saber que tipo de dado ele é
print(type(nome))
print(type(idade))
print(type(altura))

# Recebendo dados dos usuários
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Olá, {nome}!")
print(f"Sua idade é {idade} anos")
print(f"Sua altura é {altura} cm")

novaidade = idade - 9
novaaltura = altura - 0.13

print(f"{nome}, sua nova idade é: {novaidade} e sua altura agora é: {novaaltura}")

x, y, z, w = 10, 20, 30, 40
print(x, y, z, w)

# 3. Operadores Numéricos

# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Divisão inteira //
# Resto da Divisão %
# Exponenciação **

matine = 150.00
consumacao = 120.00
cocaCola = 9.00
xBaconBurguer = 30.00
batatinha = 10.00
milkshake = 25.00
uber = 20.00
agua = 1.50

esquenta = cocaCola + xBaconBurguer + batatinha
print(f"Esquenta: R$ {esquenta:.2f}")

diversao = matine + consumacao - (esquenta + milkshake + batatinha + 2 * agua) + uber
print(f"Você gastou R$: {diversao:.2f}")

# 4. Strings
nome = "SENAI Suíço-Brasileira - Paulo Ernesto Tolle"

print(nome[0])  # Primeiro caractere
print(nome[0:5])  # Do índice 0 ao 4
print(nome[6:])  # Do índice 6 até o final
print(nome[0:22])  # Do início ao índice 21
print(nome[0:22:2])  # Pulando de 2 em 2 caracteres

print(len("Dobby"))  # Conta a quantidade de caracteres

a = "Python World"
print("Python" in a)  # Verifica se "Python" está dentro da string

print(nome.lower())  # Transforma em minúsculas
print(nome.upper())  # Transforma em maiúsculas

espaco = "   Python World   "
print(espaco.strip())  # Remove espaços em branco no início e no fim

nome = "senai suíço-brasileira - paulo ernesto tolle"
print(nome.title())  # Primeira letra de cada palavra maiúscula

# 5. Operadores Relacionais

# Comparação entre condições (==, >, >=, <, <=, !=)
print(cocaCola == milkshake)  # False
print(xBaconBurguer != uber)  # True
print(matine > esquenta)  # True
print(esquenta <= diversao)  # True
print(consumacao >= agua)  # True
