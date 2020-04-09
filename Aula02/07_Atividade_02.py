# Atividade 02

# Inserir o nome e idade de 3 pessoas
# Imprimir o nome e a idade das 3 pessoas com sua data de nascimento

pessoa01 = input('Digite o nome da Pessoa 1: ')
idade_pessoa01 = int(input('Digite a idade da Pessoa 1: '))
pessoa02 = input('Digite o nome da Pessoa 2: ')
idade_pessoa02 = int(input('Digite a idade da Pessoa 2: '))
pessoa03 = input('Digite o nome da Pessoa 3: ')
idade_pessoa03 = int(input('Digite a idade da Pessoa 3: '))

ano = 2020
nasc_pessoa01 = ano - idade_pessoa01
nasc_pessoa02 = ano - idade_pessoa02
nasc_pessoa03 = ano - idade_pessoa03

print('Olá,', pessoa01,'sua idade é,', idade_pessoa01,'vocè nasceu em', nasc_pessoa01)
print('Olá,', pessoa02,'sua idade é,', idade_pessoa02,'vocè nasceu em', nasc_pessoa02)
print('Olá,', pessoa03,'sua idade é,', idade_pessoa03,'vocè nasceu em', nasc_pessoa03)


