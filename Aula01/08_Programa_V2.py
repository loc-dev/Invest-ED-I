# Faça o seguinte programa receber os dados do usuário
# O usuário deve escrever o seu nome e os valores de (A) e (B)
# Realizar uma operação aritmética dos valores (A) e (B) com a sua idade
# Imprimir o valor da operação e nome do usuário

print("=======||=======||=======||=======")
print("")

nome = input("Nome do usuário: ")
idade = int(input("Idade do usuário: "))

print("")

valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))

print("")

op = valor_a + valor_b + idade

print("Olá,", nome,"o resultado da operação é:", op)

