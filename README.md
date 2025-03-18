🌎 Dashboard de Análise de Dados Climáticos
📋 Sobre o Projeto
Este repositório contém meu projeto de Dashboard de Análise de Dados, desenvolvido para coletar informações meteorológicas, armazená-las de forma eficiente e exibi-las por meio de gráficos interativos. O objetivo principal é integrar coleta de dados via API, armazenamento em banco de dados, caching e visualização gráfica, otimizando a performance da aplicação.

Durante o desenvolvimento, aprendi sobre:

📡 Consumo de APIs (OpenWeatherMap)
🗄️ Armazenamento de dados (MySQL)
⚡ Caching para otimização (Redis)
📊 Criação de gráficos interativos (Plotly)
🔍 Visão Geral da Arquitetura
<p align="center"> <img src="docs/dashboard-arquitetura.png" alt="Fluxo do Dashboard"> </p>
Este fluxo representa as principais etapas do projeto:

1️⃣ Coleta de Dados: O script consulta a API de clima e obtém os dados da cidade escolhida.
2️⃣ Armazenamento no Banco: Os dados são registrados em um banco MySQL para futuras análises.
3️⃣ Caching com Redis: Para evitar chamadas desnecessárias à API, os dados são armazenados em cache por 1 hora.
4️⃣ Visualização Gráfica: Os dados são processados e exibidos de forma interativa usando Plotly.

⚙️ Estrutura do Código
🔹 coleta_dados.py
Script responsável por obter os dados climáticos da API OpenWeatherMap e exibi-los no terminal.

🔹 armazenar_dados.py
Armazena os dados coletados no banco MySQL. Se a tabela não existir, ela será criada automaticamente.

🔹 caching.py
Implementa um cache com Redis, evitando requisições repetitivas à API e melhorando a eficiência da aplicação.

🔹 grafico.py
Utiliza Plotly para gerar gráficos interativos com os dados coletados.

🚀 Como Executar
1️⃣ Clone o repositório

sh
Copiar código
git clone https://github.com/SEU_USUARIO/dashboard-clima.git
cd dashboard-clima
2️⃣ Instale as dependências

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
