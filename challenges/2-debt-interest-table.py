# Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente: valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:

# -  Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela:

# 1   3   6   9  12
# 0  10  15  20  25

# Na saída do programa, utilize estrutura de repetição para apresentar a listagem, conforme o modelo acima.

valor_divida = float(input("Digite o valor da dívida: R$"))

print(f"\nTotal: R${valor_divida:.2f} - Juros: R$0.00 - Número de parcelas: 1 - Valor da Parcela: R${valor_divida:.2f}")

juros = 10

for i in range(3, 13, 3):
    valor_total = valor_divida + (valor_divida * juros / 100)

    print(f"Total: R${valor_total:.2f} - Juros: R${(valor_divida * juros / 100):.2f} - Número de parcelas: {i} - Valor da Parcela: R${valor_total/i:.2f}")
    juros += 5