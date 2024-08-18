salario_base = 2259.20
try:
    salario = float(input('Digite seu salario: '))

    if salario <= salario_base:
        print('Isento de imposto')
    elif salario <= 2826.65:
        print('Imposto de 7,5% ')
    elif salario <= 3751.05:
        print('Imposto de 15% ')
    elif salario <= 4664.68:
        print('Imposto de 22,5% ')
    elif salario >= 4664.68:
        print('Imposto de 27,5% ')
except ValueError:
    print('Você não digitou em numeros.')