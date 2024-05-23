# A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de receitas, gastos, dívidas e investimentos.  Ela precisa realizar uma votação para escolher qual dia da semana é o melhor para a realização das lives com o time da mentoria financeira. Desenvolva um programa em que os colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos colaboradores.

# Observação: Verifique o número de colaboradores que irão participar da votação para programar sua estrutura de repetição."

print("== LIVES COM O TIME DA MENTORIA FINANCEIRA ==")

segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

colaboradores = int(input("Digite o número de colaboradores que irão votar: "))

for i in range(1, colaboradores + 1, 1):
    print("""
    SELECIONE O NÚMERO QUE REPRESENTA O DIA DA SEMANA DE SUA PREFERÊNCIA PARA PARTICIPAR:
    2- Segunda-feira
    3- Terça-feira
    4- Quarta-feira
    5- Quinta-feira
    6- Sexta-feira
    """)

    voto = int(input("DIGITE O SEU VOTO: "))

    while voto < 2 or voto > 6:
        print("Resposta inválida!")
        voto = int(input("DIGITE O SEU VOTO: "))

    if voto == 2:
        segunda += 1
        print("Voto computado com sucesso!")
    elif voto == 3:
        terca += 1
        print("Voto computado com sucesso!")
    elif voto == 4:
        quarta += 1
        print("Voto computado com sucesso!")
    elif voto == 5:
        quinta += 1
        print("Voto computado com sucesso!")
    elif voto == 6:
        sexta += 1
        print("Voto computado com sucesso!")

vencedor = "segunda-feira"
mais_votado = segunda

if terca > mais_votado:
    vencedor = "terça-feira"
    mais_votado = terca
if quarta > mais_votado:
    vencedor = "quarta-feira"
    mais_votado = quarta
if quinta > mais_votado:
    vencedor = "quinta-feira"
    mais_votado = quinta
if sexta > mais_votado:
    vencedor = "sexta-feira"
    mais_votado = sexta



print(f"""
===================================================================

RESULTADO: O dia que mais foi votado foi a {vencedor} com {mais_votado} votos!

===================================================================""")