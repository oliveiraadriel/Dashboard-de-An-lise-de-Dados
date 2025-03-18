# 🌎 Dashboard de Análise de Dados Climáticos  

## 📋 Sobre o Projeto  

Este repositório contém minha implementação de um **Dashboard de Análise de Dados**, cujo objetivo é coletar, armazenar e visualizar informações meteorológicas de forma eficiente. Para isso, o projeto integra **coleta de dados via API, armazenamento em banco de dados, caching e exibição gráfica interativa**.

Durante o desenvolvimento, aprendi conceitos essenciais como:

- 📡 **Consumo de APIs** (OpenWeatherMap)  
- 🗄️ **Armazenamento de dados** (MySQL)  
- ⚡ **Uso de caching para otimização** (Redis)  
- 📊 **Criação de gráficos interativos** (Plotly)  

---

## 🔍 Fluxo do Sistema  

<p align="center">
  <img src="docs/dashboard-arquitetura.png" alt="Fluxo do Dashboard">
</p>  

Este diagrama representa as etapas do projeto. Cada componente tem um papel fundamental na eficiência e funcionalidade do sistema.

### 🔹 **Coleta de Dados**  
O script acessa a API do OpenWeatherMap e obtém as informações meteorológicas de uma cidade específica.  

### 🔹 **Armazenamento no Banco de Dados**  
Os dados são registrados em um banco **MySQL**, permitindo consultas futuras e análise histórica.  

### 🔹 **Caching com Redis**  
Para evitar requisições repetitivas à API, os dados são armazenados em **cache** por 1 hora.  

### 🔹 **Visualização Gráfica**  
Os dados armazenados podem ser visualizados através de gráficos interativos gerados com **Plotly**.  

---

## ⚙️ Estrutura do Código  

### 🔹 `coleta_dados.py`  
Obtém os dados climáticos da API **OpenWeatherMap** e os exibe no terminal.  

### 🔹 `armazenar_dados.py`  
Registra as informações no banco de dados **MySQL**, criando a tabela caso ainda não exista.  

### 🔹 `caching.py`  
Implementa **Redis** para armazenar dados temporariamente, reduzindo chamadas repetidas à API.  

### 🔹 `grafico.py`  
Gera gráficos interativos com os dados coletados, utilizando **Plotly** para visualização.  

---

## 💡 Como Executar  

1️⃣ **Clone o repositório**:  
```sh
git clone https://github.com/SEU_USUARIO/dashboard-clima.git
cd dashboard-clima
2️⃣ Instale as dependências:

sh
Copiar código
pip install requests mysql-connector-python redis plotly
3️⃣ Configure sua chave da API

Substitua 'sua_api_key' pelo seu token da API OpenWeatherMap nos arquivos .py.
4️⃣ Execute os scripts

Coleta de dados:
sh
Copiar código
python coleta_dados.py
Armazenamento no banco:
sh
Copiar código
python armazenar_dados.py
Cache de dados:
sh
Copiar código
python caching.py
Geração de gráficos:
sh
Copiar código
python grafico.py
🎯 O que Aprendi
✔️ Como consumir APIs públicas para obter dados dinâmicos.
✔️ Armazenamento eficiente de informações em banco de dados.
✔️ Implementação de caching para reduzir chamadas desnecessárias.
✔️ Uso de gráficos interativos para visualização de dados.

Este projeto foi uma excelente oportunidade para consolidar conhecimentos em Python, bancos de dados, otimização de performance e análise de dados. 🚀

📜 Licença
Projeto aberto para estudo e aprimoramento! Se achou útil, contribua dando uma ⭐ no repositório.
