# A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:

# a) O preço final para compra à vista tem um desconto de 20%:
# b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60:

# Os percentuais de acréscimo seguem na tabela abaixo:
#  6   12   18   24   30   36   42   48   54   60
# 3%   6%   9%  12%  15%  18%  21%  24%  27%  30%

# Observação: Na saída do programa, utilize estrutura de repetição para apresentar a listagem, conforme o modelo pedido.

print("== COMPRA DE VEÍCULOS ==")

preco_carro = float(input("Qual é o valor do carro? "))

desconto_avista = preco_carro * 20 / 100
valor_avista = preco_carro - desconto_avista

print(f"\nO preço final à vista com desconto de 20% é: R${valor_avista:.2f}\n")

for i in range(6, 61, 6):

    juros = i / 2 / 100 * preco_carro
    valor_final = preco_carro + juros

    print(f"O preço final parcelado em {i}x é de R${valor_final:.2f} com parcelas de R${valor_final/i:.2f}")