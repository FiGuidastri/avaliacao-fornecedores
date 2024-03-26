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


'''def avaliar_contrato(fornecedores, avaliacoes):
    contrato_SAP = 
    fornecedor_avaliado = filtrar_fornecedor()
'''
def main():
    fornecedores = []

    while True:
        opcao = menu()

        if opcao == 'i':
            cadastrar_fornecedor(fornecedores)
        if opcao == 'lc':
            listar_contratos(fornecedores)

if __name__ == '__main__':
     main()