import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pandas as pd

class Aplicacao:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestão de Contratos")

        # Carregar dados
        self.carregar_dados()

        # Criar o frame principal
        self.frame_principal = tk.Frame(self.master)
        self.frame_principal.pack()

        # Botões para as funcionalidades
        self.btn_inserir_contrato = tk.Button(self.frame_principal, text="Inserir Contrato", command=self.inserir_contrato)
        self.btn_inserir_contrato.grid(row=0, column=0, padx=10, pady=10)

        self.btn_listar_contratos = tk.Button(self.frame_principal, text="Listar Contratos", command=self.listar_contratos)
        self.btn_listar_contratos.grid(row=0, column=1, padx=10, pady=10)

        self.btn_avaliar_contrato = tk.Button(self.frame_principal, text="Avaliar Contrato", command=self.avaliar_contrato)
        self.btn_avaliar_contrato.grid(row=1, column=0, padx=10, pady=10)

        self.btn_listar_avaliacoes = tk.Button(self.frame_principal, text="Listar Avaliações", command=self.listar_avaliacoes)
        self.btn_listar_avaliacoes.grid(row=1, column=1, padx=10, pady=10)

        self.btn_salvar_sair = tk.Button(self.frame_principal, text="Salvar e Sair", command=self.salvar_e_sair)
        self.btn_salvar_sair.grid(row=2, columnspan=2, padx=10, pady=10)

    def carregar_dados(self):
        self.caminho_planilha_fornecedores = 'fornecedores.xlsx'
        self.caminho_planilha_avaliacoes = 'avaliacoes.xlsx'
        self.fornecedores = self.carregar_fornecedores_de_planilha(self.caminho_planilha_fornecedores)
        self.avaliacoes = self.carregar_avaliacoes_de_planilha(self.caminho_planilha_avaliacoes)

    def carregar_fornecedores_de_planilha(self, caminho_planilha):
        try:
            df = pd.read_excel(caminho_planilha, sheet_name='Fornecedores', index_col=0)
            return df.to_dict(orient='index')
        except FileNotFoundError:
            return {}

    def carregar_avaliacoes_de_planilha(self, caminho_planilha):
        try:
            df = pd.read_excel(caminho_planilha, sheet_name='Avaliacoes')
            return df.to_dict(orient='records')
        except FileNotFoundError:
            return []

    def salvar_dados(self):
        self.salvar_fornecedores_em_planilha(self.fornecedores, self.caminho_planilha_fornecedores)
        self.salvar_avaliacoes_em_planilha(self.avaliacoes, self.caminho_planilha_avaliacoes)

    def salvar_fornecedores_em_planilha(self, fornecedores, caminho_planilha):
        df = pd.DataFrame.from_dict(fornecedores, orient='index')
        df.to_excel(caminho_planilha, sheet_name='Fornecedores', index=True)

    def salvar_avaliacoes_em_planilha(self, avaliacoes, caminho_planilha):
        df = pd.DataFrame(avaliacoes)
        df.to_excel(caminho_planilha, sheet_name='Avaliacoes', index=False)

    def inserir_contrato(self):
        self.janela_inserir_contrato = tk.Toplevel(self.master)
        self.janela_inserir_contrato.title("Inserir Contrato")

        # Elementos da interface para inserção de contrato
        tk.Label(self.janela_inserir_contrato, text="Informe o contrato SAP do fornecedor: ").grid(row=0, column=0)
        self.contrato_sap_entry = tk.Entry(self.janela_inserir_contrato)
        self.contrato_sap_entry.grid(row=0, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe a empresa: ").grid(row=1, column=0)
        self.empresa_entry = tk.Entry(self.janela_inserir_contrato)
        self.empresa_entry.grid(row=1, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe o número do contrato jurídico(VRD): ").grid(row=2, column=0)
        self.contrato_vrd_entry = tk.Entry(self.janela_inserir_contrato)
        self.contrato_vrd_entry.grid(row=2, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe o escopo do contrato: ").grid(row=3, column=0)
        self.escopo_entry = tk.Entry(self.janela_inserir_contrato)
        self.escopo_entry.grid(row=3, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe a data de início do contrato(dd-mm-aaaa): ").grid(row=4, column=0)
        self.vigencia_inicio_entry = tk.Entry(self.janela_inserir_contrato)
        self.vigencia_inicio_entry.grid(row=4, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe a data final do contrato(dd-mm-aaaa): ").grid(row=5, column=0)
        self.vigencia_final_entry = tk.Entry(self.janela_inserir_contrato)
        self.vigencia_final_entry.grid(row=5, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe o valor global do contrato (R$): ").grid(row=6, column=0)
        self.valor_entry = tk.Entry(self.janela_inserir_contrato)
        self.valor_entry.grid(row=6, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe o nome do gestor do contrato: ").grid(row=7, column=0)
        self.gestor_entry = tk.Entry(self.janela_inserir_contrato)
        self.gestor_entry.grid(row=7, column=1)

        tk.Label(self.janela_inserir_contrato, text="Informe o tipo de gasto: ").grid(row=8, column=0)
        self.gasto_entry = tk.Entry(self.janela_inserir_contrato)
        self.gasto_entry.grid(row=8, column=1)

        tk.Button(self.janela_inserir_contrato, text="Salvar", command=self.salvar_contrato).grid(row=9, columnspan=2)

    def salvar_contrato(self):
        contrato_sap = self.contrato_sap_entry.get()
        empresa = self.empresa_entry.get()
        contrato_vrd = self.contrato_vrd_entry.get()
        escopo = self.escopo_entry.get()
        vigencia_inicio = self.vigencia_inicio_entry.get()
        vigencia_final = self.vigencia_final_entry.get()
        valor = self.valor_entry.get()
        gestor = self.gestor_entry.get()
        gasto = self.gasto_entry.get()

        # Validar os campos de entrada, você pode adicionar mais validações conforme necessário
        if contrato_sap and empresa and contrato_vrd and escopo and vigencia_inicio and vigencia_final and valor and gestor and gasto:
            try:
                valor = float(valor)
                vigencia_inicio = datetime.strptime(vigencia_inicio, '%d-%m-%Y')
                vigencia_final = datetime.strptime(vigencia_final, '%d-%m-%Y')
            except ValueError:
                messagebox.showerror("Erro", "Formato de entrada inválido!")
                return

            status = 'Vencido' if datetime.today() > vigencia_final else 'Vigente'

            self.fornecedores[contrato_sap] = {
                'Contrato Juridico': contrato_vrd,
                'Empresa': empresa,
                'Escopo': escopo,
                'Valor Global': valor,
                'Vigência Inicio': vigencia_inicio,
                'Vigência Final': vigencia_final,
                'Status': status,
                'Gestor': gestor,
                'Gasto': gasto
            }
            messagebox.showinfo("Sucesso", "Contrato cadastrado com sucesso!")
            self.salvar_dados()
            self.janela_inserir_contrato.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

    def listar_contratos(self):
        self.janela_listar_contratos = tk.Toplevel(self.master)
        self.janela_listar_contratos.title("Listar Contratos")

        if not self.fornecedores:
            tk.Label(self.janela_listar_contratos, text="Não há contratos cadastrados.").pack()
            return

        for contrato, fornecedor in self.fornecedores.items():
            tk.Label(self.janela_listar_contratos, text=f"Contrato SAP: {contrato}").pack()
            for chave, valor in fornecedor.items():
                tk.Label(self.janela_listar_contratos, text=f"{chave}: {valor}").pack()
            tk.Label(self.janela_listar_contratos, text="="*50).pack()

def realizar_avaliacao_contrato(self):
    contrato_sap = self.contrato_sap_avaliar_entry.get()
    periodo_inicio = self.avaliacao_periodo_inicio_entry.get()
    periodo_fim = self.avaliacao_periodo_fim_entry.get()

    if contrato_sap not in self.fornecedores:
        messagebox.showerror("Erro", "Contrato não encontrado.")
        return

    try:
        periodo_inicio = datetime.strptime(periodo_inicio, '%d-%m-%Y')
        periodo_fim = datetime.strptime(periodo_fim, '%d-%m-%Y')
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd-mm-aaaa.")
        return

    for avaliacao in self.avaliacoes:
        periodo_inicio_existente = avaliacao['Periodo Inicio']
        periodo_fim_existente = avaliacao['Periodo Fim']

        # Verifica se há sobreposição de períodos
        if (periodo_inicio <= periodo_fim_existente and periodo_fim >= periodo_inicio_existente):
            messagebox.showerror("Erro", "Já existe uma avaliação para o período informado.")
            return

    # Janela para seleção do tipo de avaliação
    self.janela_tipo_avaliacao = tk.Toplevel(self.janela_avaliar_contrato)
    self.janela_tipo_avaliacao.title("Selecionar Tipo de Avaliação")

    tk.Label(self.janela_tipo_avaliacao, text="Selecione o tipo de avaliação:").pack()
    self.tipo_avaliacao_var = tk.StringVar(self.janela_tipo_avaliacao)

    for i, (tipo, criterios) in enumerate(criterios.items(), start=1):
        tk.Radiobutton(self.janela_tipo_avaliacao, text=f"Tipo {i}: {', '.join(criterios)}", variable=self.tipo_avaliacao_var, value=tipo).pack()

    tk.Button(self.janela_tipo_avaliacao, text="Próximo", command=self.realizar_avaliacao_tipo).pack()

def realizar_avaliacao_tipo(self):
    tipo_avaliacao = self.tipo_avaliacao_var.get()

    if tipo_avaliacao not in criterios:
        messagebox.showerror("Erro", "Opção inválida.")
        return

    self.janela_tipo_avaliacao.destroy()

    # Janela para inserção de notas
    self.janela_inserir_notas = tk.Toplevel(self.janela_avaliar_contrato)
    self.janela_inserir_notas.title(f"Avaliação do Contrato - {', '.join(criterios[tipo_avaliacao])}")

    self.notas_entries = {}
    for criterio in criterios[tipo_avaliacao]:
        tk.Label(self.janela_inserir_notas, text=f"Nota para '{criterio}' (de 0 a 5), sendo 0 - não se aplica, 1 - Péssimo e 5 - Excelente:").pack()
        entry = tk.Entry(self.janela_inserir_notas)
        entry.pack()
        self.notas_entries[criterio] = entry

    tk.Button(self.janela_inserir_notas, text="Salvar", command=lambda: self.salvar_avaliacao_contrato(tipo_avaliacao)).pack()

def salvar_avaliacao_contrato(self, tipo_avaliacao):
    notas = {}
    for criterio, entry in self.notas_entries.items():
        nota = entry.get()
        if nota.isdigit() and 0 <= int(nota) <= 5:
            notas[criterio] = int(nota)
        else:
            messagebox.showerror("Erro", "Nota inválida. Deve ser um número entre 0 e 5.")
            return

    self.avaliacoes.append({
        'Contrato SAP': self.contrato_sap_avaliar_entry.get(),
        'Periodo Inicio': self.avaliacao_periodo_inicio_entry.get(),
        'Periodo Fim': self.avaliacao_periodo_fim_entry.get(),
        'Tipo Avaliação': tipo_avaliacao,
        'Notas': notas
    })
    messagebox.showinfo("Sucesso", "Avaliação registrada com sucesso.")
    self.salvar_dados()
    self.janela_avaliar_contrato.destroy()


    def listar_avaliacoes(self):
        self.janela_listar_avaliacoes = tk.Toplevel(self.master)
        self.janela_listar_avaliacoes.title("Listar Avaliações")

        if not self.avaliacoes:
            tk.Label(self.janela_listar_avaliacoes, text="Não há avaliações registradas.").pack()
            return

        for avaliacao in self.avaliacoes:
            tk.Label(self.janela_listar_avaliacoes, text=f"Contrato SAP: {avaliacao['Contrato SAP']}").pack()
            tk.Label(self.janela_listar_avaliacoes, text=f"Período de Avaliação: {avaliacao['Periodo Inicio'].strftime('%d-%m-%Y')} - {avaliacao['Periodo Fim'].strftime('%d-%m-%Y')}").pack()
            tk.Label(self.janela_listar_avaliacoes, text=f"Tipo de Avaliação: {avaliacao['Tipo Avaliação']}").pack()
            tk.Label(self.janela_listar_avaliacoes, text="Notas:").pack()
            for criterio, nota in avaliacao['Notas'].items():
                tk.Label(self.janela_listar_avaliacoes, text=f"{criterio}: {nota}").pack()
            tk.Label(self.janela_listar_avaliacoes, text="="*50).pack()

    def salvar_e_sair(self):
        self.salvar_dados()
        self.master.quit()

def main():
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()

if __name__ == "__main__":
    main()
