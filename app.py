from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime, timedelta
import requests
import csv
import os
import json


app = Flask(__name__)

DB_NAME = "contratos.db"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
                     CREATE TABLE IF NOT EXISTS contratos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        data_inicio TEXT,
                        data_fim TEXT,
                        status TEXT DEFAULT 'ativo'
                     );  
             ''')
        

def enviar_mensagem(numero, mensagem):
    url = "http://localhost:8000/sendMessage"
    payload = {
        "phone": numero,
        "message": mensagem
    }

    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

@app.route('/')
def index():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM contratos")
        contratos = cursor.fetchall()
    return render_template('index.html', contratos=contratos)


@app.route('/dashboard')
def dashboard():
    with sqlite3.connect(DB_NAME) as conn:
        total = conn.execute("SELECT COUNT(*) FROM contratos").fetchone()[0]
        ativos = conn.execute("SELECT COUNT(*) FROM contratos WHERE status='ativo'").fetchone()[0]
        vencidos = conn.execute("SELECT COUNT(*) FROM contratos WHERE status='vencido'").fetchone()[0]
        proximos = conn.execute("SELECT COUNT(*) FROM contratos WHERE status='ativo' AND date(data_fim) <= date('now', '+3 day')").fetchone()[0]

    chart_data = {
        'labels': ['Ativos', 'Vencidos', 'Próximos a vencer'],
        'values': [ativos, vencidos, proximos]
    }

    return render_template('dashboard.html', total=total, ativos=ativos, vencidos=vencidos, proximos=proximos, chart_data=json.dumps(chart_data))


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    cliente = request.form['cliente']
    telefone = request.form['telefone']
    data_inicio = request.form['data_inicio']
    data_fim = request.form['data_fim']

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO contratos (cliente, telefone, data_inicio, data_fim) VALUES (?, ?, ?, ?)", (cliente, telefone, data_inicio, data_fim))
    return redirect('/')



@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            with sqlite3.connect(DB_NAME) as conn:
                for row in reader:
                    conn.execute("""
                                 INSERT INTO contratos (cliente, telefone, data_inicio, data_fim)
                                 VALUES (?, ?, ?, ?)
                                 
                                 
                                 """, (row['cliente'], row['telefone'], row['data_inicio'], row['data_fim']))
            os.remove(filepath)
        return redirect('/')

@app.route('/verificar_vencimentos')
def verificar_vencimentos():
    hoje = datetime.now().date()
    aviso_dias = 3
    data_limite = hoje + timedelta(days=aviso_dias)


    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT cliente, telefone, data_fim FROM contratos WHERE status='ativo'")
        for id_, cliente, telefone, data_fim in cursor:
            if data_fim:
                vencimento = datetime.strptime(data_fim, '%Y-%m-%d').date()
                if hoje > vencimento:
                    conn.execute("UPDATE contratos SET status='vencido' WHERE id=?", (id_,))
                elif hoje <= vencimento <= data_limite:
                    mensagem = f"Olá {cliente}, seu contrato vence em {vencimento}. deseja Renovar?"
                    enviar_mensagem(telefone, mensagem)

    return "Mensagens de vencimento enviadas."


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

