from datetime import datetime

def menu():
    menu_text = '''
    ======================MENU======================
    [i]\tInserir Contrato
    [a]\tAvaliar Contrato
    [lc]\tListar Contratos
    [la]\tListar Avaliações
    [q]\tSair
    =>'''
    return input(menu_text)

def cadastrar_fornecedor(fornecedores):
    contratoSAP = input('Informe o contrato SAP do fornecedor: ')
    if contratoSAP in fornecedores:
        print('\nContrato já cadastrado!')
        return

    empresa = input('Informe a empresa: ')
    contratoVRD = input('Informe o número do contrato jurídico(VRD): ')
    escopo = input('Informe o escopo do contrato: ')
    vigencia_inicio = input('Informe a data de início do contrato(dd-mm-aaaa): ')
    vigencia_final = input('Informe a data final do contrato(dd-mm-aaaa): ')
    valor = float(input('Informe o valor global do contrato (R$): '))

    # Convertendo as strings de data para objetos datetime com tratamento de erros
    try:
        vigencia_inicio = datetime.strptime(vigencia_inicio, '%d-%m-%Y')
        vigencia_final = datetime.strptime(vigencia_final, '%d-%m-%Y')
    except ValueError:
        print("Formato de data inválido. Use o formato dd-mm-aaaa.")
        return

    status = 'Vencido' if datetime.today() > vigencia_final else 'Vigente'
    gestor = input('Informe o nome do gestor do contrato: ')
    gasto = input('Informe o tipo de gasto: ')

    fornecedores[contratoSAP] = {
        'Contrato Juridico': contratoVRD,
        'Empresa': empresa,
        'Escopo': escopo,
        'Valor Global': valor,
        'Vigência Inicio': vigencia_inicio,
        'Vigência Final': vigencia_final,
        'Status': status,
        'Gestor': gestor,
        'Gasto': gasto
    }
    print('=== Contrato cadastrado com sucesso! ===')

def listar_contratos(fornecedores):
    if not fornecedores:
        print("Não há contratos cadastrados.")
        return

    print("\n=== Lista de Contratos ===")
    for contrato, fornecedor in fornecedores.items():
        print('=' * 100)
        print(f"Contrato SAP: {contrato}")
        for chave, valor in fornecedor.items():
            print(f"{chave}: {valor}")

def avaliar_contrato(fornecedores, avaliacoes):
    contrato_SAP = input('Digite o número do contrato SAP: ')
    if contrato_SAP not in fornecedores:
        print("Contrato não encontrado.")
        return

    avaliacao_periodo_inicio = input('Informe a data de início do período de avaliação(dd-mm-aaaa): ')
    avaliacao_periodo_fim = input('Informe a data final do período de avaliação(dd-mm-aaaa): ')

    try:
        avaliacao_periodo_inicio = datetime.strptime(avaliacao_periodo_inicio, '%d-%m-%Y')
        avaliacao_periodo_fim = datetime.strptime(avaliacao_periodo_fim, '%d-%m-%Y')
    except ValueError:
        print("Formato de data inválido. Use o formato dd-mm-aaaa.")
        return

    for avaliacao in avaliacoes:
        periodo_inicio_existente = avaliacao['Periodo Inicio']
        periodo_fim_existente = avaliacao['Periodo Fim']

        # Verifica se há sobreposição de períodos
        if (avaliacao_periodo_inicio <= periodo_fim_existente and avaliacao_periodo_fim >= periodo_inicio_existente):
            print("Já existe uma avaliação para o período informado.")
            return

    print("\nAvaliação do Contrato:")
    print("[1] Meio Ambiente")
    print("[2] Segurança do Trabalho")
    print("[3] Qualidade do Serviço")
    tipo_avaliacao = input("Escolha o tipo de avaliação (1, 2 ou 3): ")

    criterios = {
        '1': ['Envio de manifestos e monitoramentos', 'Licença de provedores críticos', 'Acondicionamento e destinação de resíduos', 'Regularidade de áreas de apoio para obra'],
        '2': ['Precidenciário / Trabalhista', 'Documentação de saúde e segurança ocupacional', 'Participação de reuniões da CIPA integrada', 'Fiscalização de campo'],
        '3': ['Mobilização e prazos', 'Qualidade das amostras, ensaios laboratório', 'Capacidade técnica', 'Qualidade do serviço']
    }

    if tipo_avaliacao not in criterios:
        print("Opção inválida.")
        return

    print(f"\nAvaliação do Contrato - {criterios[tipo_avaliacao]}:")
    notas = {}
    for criterio in criterios[tipo_avaliacao]:
        nota = input(f"Nota para '{criterio}' (de 0 a 5), sendo 0 - não se aplica, 1 - Péssimo e 5 - Excelente: ")
        if nota.isdigit() and 1 <= int(nota) <= 5:
            notas[criterio] = int(nota)
        else:
            print("Nota inválida. Deve ser um número entre 1 e 5.")
            return

    avaliacoes.append({
        'Contrato SAP': contrato_SAP,
        'Periodo Inicio': avaliacao_periodo_inicio,
        'Periodo Fim': avaliacao_periodo_fim,
        'Tipo Avaliação': tipo_avaliacao,
        'Notas': notas
    })
    print("Avaliação registrada com sucesso.")

def listar_avaliacoes(avaliacoes):
    if not avaliacoes:
        print("Não há avaliações registradas.")
        return

    print("\n=== Lista de Avaliações ===")
    for avaliacao in avaliacoes:
        tipo_avaliacao = {
            '1': 'Meio Ambiente',
            '2': 'Segurança do Trabalho',
            '3': 'Geral'
        }.get(avaliacao['Tipo Avaliação'], 'Tipo de Avaliação Desconhecido')

        print("\nContrato SAP:", avaliacao['Contrato SAP'])
        print("Tipo de Avaliação:", tipo_avaliacao)
        print("Período de Avaliação:", avaliacao['Periodo Inicio'].strftime('%d-%m-%Y'), "-", avaliacao['Periodo Fim'].strftime('%d-%m-%Y'))
        print("Notas:")
        for criterio, nota in avaliacao['Notas'].items():
            print(f"{criterio}: {nota}")

def main():
    fornecedores = {}
    avaliacoes = []

    while True:
        opcao = menu()

        if opcao == 'i':
            cadastrar_fornecedor(fornecedores)
        elif opcao == 'lc':
            listar_contratos(fornecedores)
        elif opcao == 'a':
            avaliar_contrato(fornecedores, avaliacoes)
        elif opcao == 'la':
            listar_avaliacoes(avaliacoes)  # Chama a função para listar as avaliações
        elif opcao == 'q':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()
