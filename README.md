# 🧰 Sistema de Gestão de Estoque

Este projeto foi desenvolvido como parte da **atividade de Desenvolvimento de Sistema de Gestão de Estoque**, com o objetivo de informatizar o controle de entrada e saída de materiais de uma fabricante de ferramentas e equipamentos manuais.

O sistema permite o **cadastro de produtos**, **gerenciamento de estoque**, **registro de movimentações** e **autenticação de usuários**, oferecendo uma interface simples, intuitiva e segura.

---

## 🚀 Funcionalidades Principais

* Autenticação de usuários (login e logout)
* Cadastro, edição e exclusão de produtos
* Busca por produtos
* Controle de estoque mínimo com alertas automáticos
* Registro de movimentações de entrada e saída
* Histórico completo de movimentações (com data, tipo e responsável)

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Django**
* **Django Allauth**
* **SQLite**
* **HTML / CSS**
* **Bootstrap (opcional)**

---

## ⚙️ Instalação e Execução do Projeto

Siga os passos abaixo para rodar o projeto localmente:

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/sistema-estoque.git
cd sistema-estoque
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

### 3️⃣ Instalar as bibliotecas necessárias

```bash
pip install django
pip install django-allauth
```

### 4️⃣ Criar o banco de dados e aplicar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Criar um superusuário (admin)

```bash
python manage.py createsuperuser
```

➡️ Siga as instruções no terminal para definir usuário e senha.

### 6️⃣ Executar o servidor local

```bash
python manage.py runserver
```

➡️ Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## 🧩 Estrutura do Projeto (Exemplo Simplificado)

```
sistema_estoque/
│
├── manage.py
├── db.sqlite3
├── venv/
│
├── usuarios/           # App responsável pela autenticação
├── produtos/           # App de cadastro e listagem de produtos
└── estoque/            # App de controle de entrada e saída
```

---

## 🧪 Testes e Validação

Os casos de teste estão descritos conforme o item **ENTREGA 8** da documentação do projeto, incluindo ambiente, ferramentas e resultados esperados para cada funcionalidade.

---

## 👤 Autores

**Rian Silva** <br>
**Lucas Beni**  

Desenvolvedores Full Stack Django 
<br>

📧 Contato: rianprates894@gmail.com <br>
📧 Contato: lucgarcbeni@gmail.com



## 📄 Licença

Este projeto é de uso **educacional** e pode ser utilizado livremente para fins de estudo e aprendizado.
