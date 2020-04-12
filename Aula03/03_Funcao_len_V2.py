# Método de string len()
# Exemplo 02 com o cálculo de IMC, convertendo o valor do tipo float para string

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/(altura**2)
print('O seu IMC é {}'.format(imc))

texto = str(imc)

print('Comprimento do valor dado a variável tipo string é', len(texto))
