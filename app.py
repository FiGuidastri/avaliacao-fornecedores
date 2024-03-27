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

    fornecedores.append({'Contrato SAP': contratoSAP, 'Contrato Juridico': contratoVRD, 'Empresa': empresa, 'Escopo':  escopo, 'Valor Globarl': valor,'Vigência Inicio': vigencia_inicio, 'Vigência Final': vigencia_final, 'Status': status, 'Gestor': gestor, 'Gasto': gasto})

    print('=== Contrato cadastrado com sucesso! ===')

def filtrar_fornecedor(contratoSAP, fornecedores):
    fornecedores_filtrados =  [fornecedor for fornecedor in fornecedores if fornecedores[contratoSAP] == contratoSAP]
    return fornecedores_filtrados[0] if fornecedores_filtrados else None

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


def avaliar_contrato(fornecedores, avaliacoes, num_avaliacao):
    contrato_SAP = input('Informe o contrato SAP a ser avaliado: ')
    fornecedor = filtrar_fornecedor(contrato_SAP, fornecedores)
    medicao_inicio = input('Insira a data de início da mediação (dd-mm-aaaa): ')
    medicao_final = input('Insira a data final da medição(dd-mm-aaaa): ')
    nota1 = int(input('Insira a nota do requisito 1(1 a 5): '))
    nota2 = int(input('Insira a nota do requisito 2(1 a 5): '))
    nota3 = int(input('Insira a nota do requisito 3(1 a 5): '))
    nota4 = int(input('Insira a nota do requisito 4(1 a 5): '))
    nota5 = int(input('Insira a nota do requisito 5(1 a 5): '))
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    
    # Convertendo as strings de data para objetos datetime
    medicao_inicio = datetime.strptime(medicao_inicio, '%d-%m-%Y')
    medicao_final = datetime.strptime(medicao_final, '%d-%m-%Y')
    
    if fornecedor:
        print(f'\n=== Avaliação do fornecedor {fornecedor} realizada com sucesso! ===')
        
        avaliacoes.append({'Contrato SAP': contrato_SAP, 'Empresa': fornecedor, 'Numero Avaliacação': num_avaliacao,'Período medição - Início': medicao_inicio, 'Período medição - Fim': medicao_final, 'Nota 1': nota1, 'Nota 2': nota3, 'Nota 3': nota3, 'Nota 4': nota4, 'Nota 5': nota5, 'Média': media})
        
    print('Contrato não encontrado, operação encerrada!')

def listar_avaliacoes(avaliacoes):
    for avaliacao in avaliacoes:
        linha = f'''
            Fornecedor:\t{avaliacoes['Empresa']}
            Contrato SAP:\t{avaliacoes['Contrato SAP']}
            Período Medição - Início:\t{avaliacoes['Período medição - Início']}
            Perído Medição - Fim:\t{avaliacoes['Período medição - Fim']}
            Média:\t{avaliacoes['Média']}
        '''
        print('=' * 100)
        print(linha)
        
        

def main():
    fornecedores = []
    avaliacoes = []

    while True:
        opcao = menu()

        if opcao == 'i':
            cadastrar_fornecedor(fornecedores)
            
        elif opcao == 'a':
            num_avaliacao = len(avaliacoes) + 1
            avaliar_contrato(avaliacoes)
                        
        elif opcao == 'lc':
            listar_contratos(fornecedores)
            
        elif opcao == 'la':
            listar_avaliacoes(avaliacoes)

if __name__ == '__main__':
     main()