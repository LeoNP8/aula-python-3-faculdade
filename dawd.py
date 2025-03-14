resultado = 10 + 20 * 30
print(resultado)

resultado2 = 42 / 30
print(resultado2)

resultado3 = (94 + 2) * 6 - 1
print(resultado3)

x = 6
print(x)
x = x + 1
print(x)

#Exemplo 01: programação que solicita a idade
# do usuário e mostra se ele pode ter CNH

idade = int(input("Digite a sua idade: "))

if idade >=18:
    print("Parabéns! Você pode ter a sua CNH")
else:
    print("Parabéns, você é um fodido e não pode ter a sua CNH")

# Exemplo 02: programa que solicita um número
# inteiro ao usuário e mostre-o caso
# o mesmo seja par

num = int(input("Entre com um número inteiro: "))
if num % 2 == 0:
    print("O número: ", num , "é par.")
else:
    print("Esse numero é ímpar")

i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print("Parabéns exibiu todos os numeros")

fruits = ["maçã", "banana", "cereja"]
for x in fruits:
    print(x)

# Exemplo 06: Cálculo da média

n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 + n2) /2
if media >= 6.0:
    print("Aprovado!!!!!")
else:
    print("Reprovado!!!!")

import math

num = int(input("Digite um número qualquer "))
if num > 0:
    raiz = math.sqrt(num)
    print("A raiz quadrada do numero digitado é:", raiz)
else:
    print("não é possivel calcular raiz quadrada de numero negativo")
