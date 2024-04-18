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
    fornecedor = filtrar_fornecedor(contratoSAP, fornecedores)

    if fornecedor:
        print('\nContrato já cadastrado!')
        return

    empresa = input('Informe a empresa: ')
    contratoVRD = input('Informe o número do contrato jurídico(VRD): ')
    escopo = input('Informe o escopo do contrato: ')
    vigencia_inicio = input('Informe a data de início do contrato(dd-mm-aaaa): ')
    vigencia_final = input('Informe a data final do contrato(dd-mm-aaaa): ')
    valor = float(input('Informe o valor global do contrato (R$): '))

    # Convertendo as strings de data para objetos datetime
    vigencia_inicio = datetime.strptime(vigencia_inicio, '%d-%m-%Y')
    vigencia_final = datetime.strptime(vigencia_final, '%d-%m-%Y')

    if datetime.today() > vigencia_final:
        status = 'Vencido'
    else:
        status = 'Vigente'

    gestor = input('Informe o nome do gestor do contrato: ')
    gasto = input('Informe o tipo de gasto: ')

    fornecedores.append({'Contrato SAP': contratoSAP, 'Contrato Juridico': contratoVRD, 'Empresa': empresa, 'Escopo':  escopo, 'Valor Global': valor,'Vigência Inicio': vigencia_inicio, 'Vigência Final': vigencia_final, 'Status': status, 'Gestor': gestor, 'Gasto': gasto})

    print('=== Contrato cadastrado com sucesso! ===')

def filtrar_fornecedor(contratoSAP, fornecedores):
    fornecedores_filtrados =  [fornecedor for fornecedor in fornecedores if fornecedor['Contrato SAP'] == contratoSAP]
    return fornecedores_filtrados[0] if fornecedores_filtrados else None


def listar_contratos(fornecedores):
    if not fornecedores:
        print("Não há contratos cadastrados.")
        return

    else:
        for fornecedor in fornecedores:
            linha = f'''
                Fornecedor:\t{fornecedor['Empresa']}
                Contrato SAP:\t{fornecedor['Contrato SAP']}
                Valor Global:\t{fornecedor['Valor Global']}
                Status:\t{fornecedor['Status']}
                Gestor:\t{fornecedor['Gestor']}
                Gasto:\t{fornecedor['Gasto']}
            '''
            print('=' * 100)
            print(linha)

def avaliar_contrato(fornecedores, avaliacoes):
    contrato_SAP = input('Digite o número do contrato SAP: ')
    fornecedor_avaliado = filtrar_fornecedor(contrato_SAP, fornecedores)
    if not fornecedor_avaliado:
        print("Contrato não encontrado.")
        return

    avaliacao_periodo_inicio = input('Informe a data de início do período de avaliação(dd-mm-aaaa): ')
    avaliacao_periodo_fim = input('Informe a data final do período de avaliação(dd-mm-aaaa): ')

    avaliacao_periodo_inicio = datetime.strptime(avaliacao_periodo_inicio, '%d-%m-%Y')
    avaliacao_periodo_fim = datetime.strptime(avaliacao_periodo_fim, '%d-%m-%Y')

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
    print("[3] Geral")
    tipo_avaliacao = input("Escolha o tipo de avaliação (1, 2 ou 3): ")

    criterios = {
        '1': ['Emissões', 'Resíduos', 'Conservação de Energia', 'Uso de Recursos Naturais'],
        '2': ['EPIs', 'Treinamentos', 'Prevenção de Acidentes', 'Procedimentos de Emergência'],
        '3': ['Qualidade do Serviço', 'Cumprimento de Prazos', 'Relacionamento', 'Custo-Benefício']
    }

    if tipo_avaliacao not in criterios:
        print("Opção inválida.")
        return

    print(f"\nAvaliação do Contrato - {criterios[tipo_avaliacao]}:")
    notas = {}
    for criterio in criterios[tipo_avaliacao]:
        nota = input(f"Nota para '{criterio}' (de 1 a 5): ")
        if nota.isdigit() and 1 <= int(nota) <= 5:
            notas[criterio] = int(nota)
        else:
            print("Nota inválida. Deve ser um número entre 1 e 5.")
            return

    avaliacoes.append({'Contrato SAP': contrato_SAP, 'Tipo Avaliação': tipo_avaliacao, 'Notas': notas})
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
        print("Notas:")
        for criterio, nota in avaliacao['Notas'].items():
            print(f"{criterio}: {nota}")


def main():
    fornecedores = []
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
