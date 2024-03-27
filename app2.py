from datetime import datetime
import pandas as pd

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


def cadastrar_fornecedor(fornecedores, arquivo_csv):
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

    novo_fornecedor = {'Contrato SAP': contratoSAP, 'Contrato Jurídico': contratoVRD, 'Empresa': empresa, 'Escopo':  escopo, 'Valor Global': valor, 'Vigência Início': vigencia_inicio, 'Vigência Final': vigencia_final, 'Status': status, 'Gestor': gestor, 'Gasto': gasto}

    # Adicionando o novo fornecedor ao DataFrame
    fornecedores = fornecedores.append(novo_fornecedor, ignore_index=True)

    # Salvando o DataFrame atualizado em um arquivo CSV
    fornecedores.to_csv(arquivo_csv, index=False)

    print('=== Contrato cadastrado com sucesso! ===')


def filtrar_fornecedor(contratoSAP, fornecedores):
    for fornecedor in fornecedores:
        if fornecedor['Contrato SAP'] == contratoSAP:
            return fornecedor
    return None

def listar_contratos(fornecedores):
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


def avaliar_contrato(avaliacoes, num_avaliacao, arquivo_csv):
    contrato_SAP = input('Informe o contrato SAP a ser avaliado: ')
    medicao_inicio = input('Insira a data de início da medição (dd-mm-aaaa): ')
    medicao_final = input('Insira a data final da medição (dd-mm-aaaa): ')
    nota1 = int(input('Insira a nota do requisito 1(1 a 5): '))
    nota2 = int(input('Insira a nota do requisito 2(1 a 5): '))
    nota3 = int(input('Insira a nota do requisito 3(1 a 5): '))
    nota4 = int(input('Insira a nota do requisito 4(1 a 5): '))
    nota5 = int(input('Insira a nota do requisito 5(1 a 5): '))
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    
    # Convertendo as strings de data para objetos datetime
    medicao_inicio = datetime.strptime(medicao_inicio, '%d-%m-%Y')
    medicao_final = datetime.strptime(medicao_final, '%d-%m-%Y')
    
    avaliacao = {'Contrato SAP': contrato_SAP, 'Numero Avaliacao': num_avaliacao, 'Período Medição - Início': medicao_inicio, 'Período Medição - Fim': medicao_final, 'Nota 1': nota1, 'Nota 2': nota2, 'Nota 3': nota3, 'Nota 4': nota4, 'Nota 5': nota5, 'Média': media}
    
    avaliacoes.append(avaliacao)
    
    # Criando um DataFrame pandas com a nova avaliação e salvando-o em um arquivo CSV
    df_avaliacoes = pd.DataFrame(avaliacoes)
    df_avaliacoes.to_csv(arquivo_csv, index=False)
    
    print(f'\n=== Avaliação do contrato {contrato_SAP} realizada com sucesso! ===')


def listar_avaliacoes(avaliacoes):
    for avaliacao in avaliacoes:
        linha = f'''
            Contrato SAP:\t{avaliacao['Contrato SAP']}
            Período Medição - Início:\t{avaliacao['Período Medição - Início']}
            Período Medição - Fim:\t{avaliacao['Período Medição - Fim']}
            Média:\t{avaliacao['Média']}
        '''
        print('=' * 100)
        print(linha)
        

def main():
    # Solicitando o caminho para salvar o arquivo CSV
    caminho_arquivo = input("Informe o caminho completo para salvar o arquivo CSV (ou pressione Enter para usar o caminho padrão): ").strip()
    if not caminho_arquivo:
        caminho_arquivo = 'fornecedores.csv'

    # Carregando o DataFrame inicial, se o arquivo CSV existir
    try:
        fornecedores = pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        fornecedores = pd.DataFrame(columns=['Contrato SAP', 'Contrato Jurídico', 'Empresa', 'Escopo', 'Valor Global', 'Vigência Início', 'Vigência Final', 'Status', 'Gestor', 'Gasto'])

    # Solicitando o caminho para salvar o arquivo CSV de avaliações
    caminho_arquivo_avaliacoes = input("Informe o caminho completo para salvar o arquivo CSV das avaliações (ou pressione Enter para usar o caminho padrão): ").strip()
    if not caminho_arquivo_avaliacoes:
        caminho_arquivo_avaliacoes = 'avaliacoes.csv'

    # Carregando o DataFrame inicial de avaliações, se o arquivo CSV existir
    try:
        df_avaliacoes = pd.read_csv(caminho_arquivo_avaliacoes)
        avaliacoes = df_avaliacoes.to_dict('records')
    except FileNotFoundError:
        avaliacoes = []

    while True:
        opcao = menu()

        if opcao == 'i':
            cadastrar_fornecedor(fornecedores, caminho_arquivo)
            
        if opcao == 'a':
            num_avaliacao = len(avaliacoes) + 1
            avaliar_contrato(avaliacoes, num_avaliacao, caminho_arquivo_avaliacoes)
                        
        elif opcao == 'lc':
            listar_contratos(fornecedores)
            
        elif opcao == 'la':
            listar_avaliacoes(avaliacoes)

if __name__ == '__main__':
    main()
