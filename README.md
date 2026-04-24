Contract Manager
Web application for contract management, with automated expiration tracking and WhatsApp notifications for renewal reminders.
The project demonstrates backend concepts such as CRUD operations, data persistence, scheduled status updates, CSV import, and integration with external services.
Aplicação web para gerenciamento de contratos, com rastreamento automatizado de vencimentos e notificações via WhatsApp para lembretes de renovação.
O projeto demonstra conceitos de backend como operações CRUD, persistência de dados, atualização de status programada, importação via CSV e integração com serviços externos.

🛠 Tech Stack / Tecnologias

Python
Flask
SQLite
Jinja2
Requests (WhatsApp API integration)
HTML / CSS


✨ Features / Funcionalidades

Contract registration with client, phone, start and end dates
Dashboard with totals (active, expired, expiring soon)
CSV import for bulk contract registration
Automatic expiration check and status update
WhatsApp notifications sent to clients with expiring contracts



Cadastro de contratos com cliente, telefone, data de início e data de fim
Dashboard com totais (ativos, vencidos, próximos a vencer)
Importação de contratos em lote via CSV
Verificação automática de vencimentos e atualização de status
Envio de notificações via WhatsApp para clientes com contratos próximos ao vencimento


🎯 Purpose / Objetivo
This project was developed to practice real-world backend concepts, including CRUD operations, data modeling with SQLite, bulk data import, scheduled business rules, and integration with an external messaging API.
Este projeto foi desenvolvido com foco na prática de conceitos aplicáveis ao desenvolvimento backend, incluindo operações CRUD, modelagem de dados com SQLite, importação de dados em lote, regras de negócio programadas e integração com uma API externa de mensageria.

📂 Project Structure / Estrutura do Projeto
Contract-Manager/
├── app.py              # Main Flask application / Aplicação Flask principal
├── contratos.db        # SQLite database / Banco de dados SQLite
├── static/
│   └── style.css       # Application stylesheet / Folha de estilos da aplicação
└── templates/
    ├── index.html      # Contract list page / Página de listagem de contratos
    └── dashboard.html  # Dashboard with metrics / Dashboard com métricas

Quick Start / Início Rápido
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

Main Routes / Rotas Principais
Route / RotaMethod / MétodoDescription / Descrição/GETContract list / Listagem de contratos/dashboardGETOverview with metrics / Visão geral com métricas/cadastrarPOSTRegister new contract / Cadastrar novo contrato/upload_csvPOSTBulk import via CSV / Importação em lote via CSV/verificar_vencimentosGETCheck expirations and notify / Verifica vencimentos e notifica

WhatsApp Integration / Integração com WhatsApp
The /verificar_vencimentos endpoint checks contracts expiring within the next 3 days and sends renewal reminders through a local WhatsApp API running on port 8000.
O endpoint /verificar_vencimentos verifica contratos com vencimento nos próximos 3 dias e envia lembretes de renovação através de uma API local de WhatsApp rodando na porta 8000.

Author / Autor
Eric Simões

GitHub: @EricS227
