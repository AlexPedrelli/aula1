# operadores matematicos
import math

# + < - soma : soma os valores da esquerda para a direita

# - < - subtracao : subtrai o valor da esquerda pelo da direita

# * < - mutiplicacao : mutiplica o valor da esquerda com a direita

# / < - divisao : divide o valor da esquerda para a direita

# ** < - potencia < eleva o valor da esquerda pelo da direita
# math.sqrt(valor) < - raiz quadrada : tira a raiz quadrada do valor

# // < - inteiro da divisao : quanfo faz uma divisao que resulta em valor float, retorna so a parte inteira.
# 10.56 retornaria so 10.

# % < - resto da divisao : retorna o valor de resto quando a divisao
# nao e exata . 5/2 teria o resto 1. util na identificacao de valores par

valor_1 = int(input("digite o valor 1: "))
valor_2 = int(input("digite o valor 2 : "))

print(" os valores digitados sao ",valor_1,"e", valor_2)

resultado = valor_1 + valor_2

print("a soma dos dois valores é" , resultado)

resultado = valor_1 - valor_2
print("a subtracao dos dois valores é" , resultado)

resultado = valor_1 / valor_2

print("a divisao dos dois valores é", resultado)

resultado = valor_1 // valor_2
print("o resultado inteiro da divisao dos valores é" , resultado)

resultado = valor_1 % valor_2
print("o resto de divisao dos valores é" , resultado)

resultado = valor_1 ** valor_2
print("o resultado da potenciacao dos valores é" ,resultado)

resultado = math.sqrt(valor_1)
print("a raiz quadrada de" , valor_1, "e" , resultado)

