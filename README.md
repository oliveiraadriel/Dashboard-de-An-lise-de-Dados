🌎 Dashboard de Análise de Dados Climáticos
Este repositório contém um Dashboard de Análise de Dados desenvolvido em Python. O objetivo do projeto é coletar informações de APIs públicas (como clima), armazená-las e exibi-las em gráficos interativos, utilizando caching para otimização.

📌 Tecnologias Utilizadas
Python 🐍
Requests (Coleta de dados via API)
MySQL (Armazenamento de dados)
Redis (Cache de dados)
Plotly (Visualização de gráficos)
📂 Estrutura do Projeto
📥 Coleta de Dados (coleta_dados.py)

Obtém informações de clima da API OpenWeatherMap.
Exibe os dados diretamente no terminal.
🗄️ Armazenamento de Dados (armazenar_dados.py)

Salva os dados climáticos no banco de dados MySQL.
Se a tabela ainda não existir, ele a cria automaticamente.
⚡ Caching de Dados (caching.py)

Utiliza Redis para armazenar em cache os dados climáticos, evitando consultas repetidas à API.
O cache expira em 1 hora para garantir informações atualizadas.
📊 Visualização Gráfica (grafico.py)

Exibe gráficos interativos utilizando Plotly.
Simula a visualização de dados coletados.
🚀 Como Executar
Clone o repositório

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências

bash
Copiar código
pip install requests mysql-connector-python redis plotly
Configure sua chave da API

Substitua 'sua_api_key' pelo seu próprio token da API OpenWeatherMap nos arquivos .py.
Execute os scripts

Coleta de dados:
bash
Copiar código
python coleta_dados.py
Armazenamento de dados:
bash
Copiar código
python armazenar_dados.py
Cache de dados:
bash
Copiar código
python caching.py
Geração de gráficos:
bash
Copiar código
python grafico.py
📢 Contribuição
Sinta-se à vontade para abrir issues ou enviar um pull request caso tenha sugestões de melhorias! 🚀
