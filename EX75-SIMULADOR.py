import os


simular = True

while simular:
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    # Apresentar Mensagem
    print("-----------------------------")
    print(" Seja bem-vindo(a) ao MyBank ")
    print("-----------------------------")

    # É cliente? Repetir até ser Sim ou Não
    eh_cliente = None
    while eh_cliente not in ["s", "n"]:
        eh_cliente = input("Você já é nosso cliente? (s/n) ").lower()

    # taxa de juros é fixa em 4% para clientes
    taxa_juros = 4
    # Caso não seja cliente
    # Deve-se consultar o score do serasa
    if eh_cliente == "n":
        serasa_score = -1
        while serasa_score < 0 or serasa_score > 1000:
            serasa_score = int(input("Digite seu Serasa Score: "))

        if serasa_score >= 700:
            taxa_juros = 5
        elif serasa_score >= 500:
            taxa_juros = 10
        elif serasa_score >= 300:
            taxa_juros = 15
        else:
            taxa_juros = 20
    print ("Taxa de juros de: ", taxa_juros)
    # Informar o valor de emprestimo
    # e quantas parcelas ele deseja dividir
    emprestimo = float(input("Valor desejado para o empréstimo: "))
    parcelas = int(input("Quantidade de parcelas: "))

    # Cálculo de Empréstimo
    tarifa = 35 if eh_cliente == "n" else 0
    imposto_iof = emprestimo * 0.38

    # Calcular Seguro Desemprego?
    incluir_seguro = None
    while incluir_seguro not in ["s", "n"]:
        incluir_seguro = input("Deseja incluir um seguro desemprego no seu empréstimo? (s/n) ")

    seguro_desemprego = 3.5 * emprestimo if incluir_seguro == "s" else 0

    custo_parcela_com_juros = (emprestimo / parcelas * (1 + taxa_juros / 100))
    custo_efetivo_total = custo_parcela_com_juros * parcelas + tarifa + imposto_iof + seguro_desemprego

    # Resultado da simulação
    print("------------------------")
    print(" RESULTADO DA SIMULAÇÃO ")
    print("------------------------")
    print("Quantidade de parcelas: ", parcelas)
    print(f"Valor das parcelas: {custo_parcela_com_juros:.2f}")
    print(f"Taxa de Juros: {taxa_juros:.1f} %")
    print(f"Custo Efetivo Total: {custo_efetivo_total:.2f}")

    realizar_simulacao = input("Deseja realizar outra simulação? (s/n) ")
    simular = realizar_simulacao == "s"
