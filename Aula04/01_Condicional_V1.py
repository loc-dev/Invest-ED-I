# Estrutura Condicional If-Else
# Exemplo 01

temp = float(input('Qual é a temperatura da boca do fogão? '))
agua = False

if temp <= 90:
    agua = True
    print('O líquido está fervendo de modo médio')

if temp > 100:
    agua = True
    print('O líquido está fervendo de modo rápido')


