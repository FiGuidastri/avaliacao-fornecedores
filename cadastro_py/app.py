from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Define o caminho para a planilha Excel
PLANILHA_PATH = 'dados.xlsx'

# Verifica se a planilha existe, se não existir, cria uma nova
if not os.path.exists(PLANILHA_PATH):
    df = pd.DataFrame(columns=['Numero do Contrato Juridico', 'Numero do Contrato SAP', 'Razao Social', 'VigenciaInicio', 'VigenciaFim', 'Valor Global', 'Gestor', 'Grupo'])
    df.to_excel(PLANILHA_PATH, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_registro', methods=['POST'])
def criar_registro():
    data = {
        'Numero do Contrato Juridico': request.form['contrato_juridico'],
        'Numero do Contrato SAP': int(request.form['contrato_sap']),
        'Razao Social': request.form['razao_social'],
        'VigenciaInicio': datetime.strptime(request.form['vigencia_inicio'], '%Y-%m-%d'),
        'VigenciaFim': datetime.strptime(request.form['vigencia_fim'], '%Y-%m-%d'),
        'Valor Global': float(request.form['valor_global']),
        'Gestor': request.form['gestor'],
        'Grupo': request.form['grupo']
    }
    df = pd.read_excel(PLANILHA_PATH)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_excel(PLANILHA_PATH, index=False)
    return jsonify({'mensagem': 'Registro criado com sucesso!'})

@app.route('/listar_registros')
def listar_registros():
    df = pd.read_excel(PLANILHA_PATH)
    registros = df.to_dict('records')
    return render_template('registros.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)
