# Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota de imposto de renda (IR) que deve ser aplicada sobre aquele resgate, levando em consideração o número de dias que o valor permaneceu aplicado, de acordo com a tabela abaixo:

# Até 180 dias = alíquota de 22,5% de IR.
# De 181 a 360 dias = alíquota de 20% de IR.
# De 361 a 720 dias = alíquota de 17,5% de IR.
# Acima de 720 dias = alíquota de 15% de IR.

# É o que acontece, por exemplo, com o CDB - Certificado de Depósito Bancário, uma aplicação de renda fixa comumente oferecida pelas Fintechs. Outros investimentos em renda fixa, como LCI e LCA, respectivamente, Letra de Crédito Imobiliário e Letra de Crédito do Agronegócio são isentos de imposto de renda. 

# Escreva um programa que receba o tipo de investimento do qual se deseja realizar um resgate (1 para CDB, 2 para LCI e 3 para LCA), o valor a ser resgatado e o número de dias que esse valor permaneceu investido e, se for o caso, calcule o valor referente ao imposto de renda.

# Atenção! O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.

print("""============== CALCULADORA DE IR ==============

    1 - CDB
    2 - LCI
    3 - LCA
""")

selecao = int(input("Selecione o tipo de investimento: "))

while selecao < 1 or selecao > 3:
    print("VALOR INVÁLIDO!")
    selecao = int(input("Selecione o tipo de investimento: "))

valor = float(input("Digite o valor a ser resgatado: R$"))

dias_investido = int(input("Digite o número de dias investido: "))

while dias_investido < 0:
    print("VALOR INVÁLIDO!")
    dias_investido = int(input("Digite o número de dias investido: "))

ir = float(0)

if selecao == 1:
    if dias_investido <= 180:
        ir = valor * 22.5 / 100
    elif dias_investido <= 360:
        ir = valor * 20 / 100
    elif dias_investido <= 720:
        ir = valor * 17.5 / 100
    elif dias_investido > 720:
        ir = valor * 15 / 100

valor_total = valor - ir

print(f"\nO valor do imposto de renda será de R${ir:.2f}")
print(f"Valor a ser resgatado: R${valor_total:.2f}")