# Realizar um código para calcular as raízes de uma Equação 2º Grau

valor_a = int(input('Qual é o valor do coeficiente principal (a): '))
valor_b = int(input('Qual é o valor do coeficiente secundário (b): '))
valor_c = int(input('Qual é o valor do termo independente (c): '))
print('')
print('A seguinte equação: ')
print('({}x²) + ({}x) + ({}) = 0'.format(valor_a, valor_b, valor_c))
print('')

# Fórmula de Bhaskara

valor_delta = float((valor_b ** 2) - (4 * valor_a * valor_c))
print('O valor de Δ: ', valor_delta)
print('')

if valor_delta >= 0:
    valor_a = (2 * valor_a)
    x1 = ((0 - (valor_b)) + (valor_delta ** (1/2)))
    x1 = (x1 / valor_a)
    x2 = ((0 - (valor_b)) - (valor_delta ** (1/2)))
    x2 = (x2 / valor_a)
    print('Ao analisar em relação ao sinais de + e - : ')
    print('O valor de X1: ', x1)
    print('O valor de X2: ', x2)
else:
    print('O valor de delta é negativo, portanto, não possui uma solução real')

    
    
