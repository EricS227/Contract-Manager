Contract Manager

Web application for contract management, with a metrics dashboard, bulk CSV import, and on-demand expiration checking with WhatsApp notifications for renewal reminders.
Aplicação web para gerenciamento de contratos, com dashboard de métricas, importação em lote via CSV e verificação de vencimentos sob demanda com notificações via WhatsApp para lembretes de renovação.

🛠 Tech Stack / Tecnologias

Python 3
Flask
SQLite (via built-in sqlite3 module)
Jinja2 (bundled with Flask / incluso no Flask)
Requests (for calling an external WhatsApp API / para chamar uma API externa de WhatsApp)
HTML, CSS
Chart.js (dashboard charts / gráficos do dashboard)


✨ Features / Funcionalidades
English

Contract registration with client, phone, start date and end date
Contract listing on the home page
Metrics dashboard with totals (active, expired, expiring within 3 days) and a bar chart
Bulk contract import via CSV upload
On-demand expiration check that marks expired contracts and triggers WhatsApp renewal reminders for contracts expiring within 3 days

Português

Cadastro de contratos com cliente, telefone, data de início e data de fim
Listagem de contratos na página inicial
Dashboard de métricas com totais (ativos, vencidos, próximos a vencer em 3 dias) e gráfico de barras
Importação de contratos em lote via upload de CSV
Verificação de vencimentos sob demanda que marca contratos vencidos e dispara lembretes de renovação via WhatsApp para contratos que vencem em até 3 dias


🎯 Purpose / Objetivo
This project was developed to practice real-world backend concepts using Flask: CRUD operations, data persistence with SQLite, bulk data import from CSV, business rules over stored data, and integration with an external HTTP API.
Este projeto foi desenvolvido para praticar conceitos reais de backend com Flask: operações CRUD, persistência de dados com SQLite, importação em lote a partir de CSV, regras de negócio sobre dados persistidos e integração com uma API HTTP externa.

📂 Project Structure / Estrutura do Projeto
Contract-Manager/
├── app.py              # Main Flask application / Aplicação Flask principal
├── contratos.db        # SQLite database / Banco de dados SQLite
├── static/
│   └── style.css       # Shared stylesheet / Folha de estilos compartilhada
└── templates/
    ├── index.html      # Home page: listing + CSV upload / Página inicial: listagem + upload CSV
    └── dashboard.html  # Dashboard with metric cards and chart / Dashboard com cards e gráfico

🗄 Database Schema / Esquema do Banco
Single table contratos / Tabela única contratos:
Column / ColunaType / TipoNotes / ObservaçõesidINTEGERPrimary key, auto-incrementclienteTEXTRequired / ObrigatóriotelefoneTEXTRequired / Obrigatóriodata_inicioTEXTFormat YYYY-MM-DDdata_fimTEXTFormat YYYY-MM-DDstatusTEXTDefault 'ativo'. Values: ativo, vencido
The table is created automatically on first run via init_db().
A tabela é criada automaticamente na primeira execução através de init_db().

🚀 Quick Start / Início Rápido
Requirements / Requisitos

Python 3.8+
pip

Installation / Instalação
bash# Clone the repository / Clone o repositório
git clone https://github.com/EricS227/Contract-Manager.git
cd Contract-Manager

# Install dependencies / Instale as dependências
pip install flask requests

# Run the application / Execute a aplicação
python app.py
The application will be available at / A aplicação estará disponível em:
http://localhost:5000

📋 Routes / Rotas
Route / RotaMethod / MétodoDescription / Descrição/GETContract list and CSV upload form / Listagem de contratos e form CSV/dashboardGETMetrics dashboard with chart / Dashboard de métricas com gráfico/cadastrarPOSTRegister a new contract / Cadastra um novo contrato/upload_csvPOSTBulk import from CSV file / Importa em lote a partir de arquivo CSV/verificar_vencimentosGETCheck expirations, update statuses and notify / Verifica vencimentos, atualiza status e notifica

📄 CSV Import Format / Formato do CSV de Importação
The CSV file must include the following column headers (first row).
O arquivo CSV deve ter os seguintes cabeçalhos de colunas (primeira linha).
csvcliente,telefone,data_inicio,data_fim
João Silva,41999990000,2025-01-01,2025-12-31
Maria Souza,41988880000,2025-03-15,2026-03-15

📨 WhatsApp Integration / Integração com WhatsApp
The /verificar_vencimentos endpoint iterates over active contracts, marks any past-due contract as vencido, and sends a renewal reminder via HTTP POST to http://localhost:8000/sendMessage for contracts expiring within the next 3 days.
O endpoint /verificar_vencimentos percorre os contratos ativos, marca contratos vencidos como vencido e envia um lembrete de renovação via HTTP POST para http://localhost:8000/sendMessage para contratos que vencem nos próximos 3 dias.

⚠️ Note / Observação: The WhatsApp API is not bundled with this project. To use the notification feature, a separate service (such as WPPConnect) must be running locally at port 8000 and expose a POST /sendMessage endpoint accepting { "phone": "...", "message": "..." }. Without it, the notification HTTP call will fail silently (the error is caught and printed), but the contract status update still runs.
A API de WhatsApp não faz parte deste projeto. Para utilizar as notificações, é necessário rodar um serviço separado (como o WPPConnect) localmente na porta 8000, expondo um endpoint POST /sendMessage que aceite { "phone": "...", "message": "..." }. Sem ele, a chamada HTTP de notificação falha silenciosamente (o erro é capturado e impresso), mas a atualização de status dos contratos continua funcionando.


👤 Author / Autor
Eric Simões

GitHub: @EricS227
