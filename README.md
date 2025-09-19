
# obra-forecast

Previsão de custo e prazo de obras a partir de Bill of Materials (BoM) e histórico, com deploy em app interativo.

## Objetivo
Conectar experiência em planejamento e BoM com Data Science.

## Stack
- Python, pandas, scikit-learn, XGBoost/LightGBM
- Jupyter/VS Code
- Streamlit (app interativo)

## Métricas
- MAE / MAPE para custo e prazo
- Visualização de resultados e gráficos no app

## Estrutura do Projeto
```
obra-forecast/
├─ README.md
├─ requirements.txt
├─ data/                # dados de entrada (ex: obras.csv, obras_teste.csv)
├─ src/                 # scripts de pipeline e modelagem
├─ app/                 # app Streamlit para previsão
├─ notebooks/           # notebooks de EDA e análise
├─ reports/             # relatórios, dicionário de dados, checklist
└─ resumo_conversa.md   # resumo do projeto e melhorias
```

## Como rodar o projeto
1. Crie e ative um ambiente virtual:
	```powershell
	python -m venv .venv
	.venv\Scripts\Activate
	```
2. Instale as dependências:
	```powershell
	pip install -r requirements.txt
	```
3. Treine o modelo:
	```powershell
	python .\src\pipeline.py
	```
4. Rode o app Streamlit:
	```powershell
	streamlit run app/streamlit_app.py
	```
5. Faça upload de um arquivo CSV com as colunas:
	- n_itens_bom
	- pct_criticos
	- complexidade
	- lead_time_medio

## Funcionalidades
- Previsão automática de custo para múltiplas obras
- Visualização de resultados em tabela e gráficos (barras, dispersão)
- Download dos resultados em CSV
- Código modular e pronto para expansão

## Exemplos de arquivos
- [`data/obras.csv`](data/obras.csv): dados de exemplo para treino
- [`data/obras_teste.csv`](data/obras_teste.csv): dados simulados para teste

## Dicionário de Dados
Veja `reports/dicionario_dados.md` para descrição das colunas esperadas.

## Resultados
- Modelos de previsão de custo e prazo
- App interativo para estimativas
- Gráficos automáticos dos resultados
- Estudo de caso documentado

## Referências e dicas
- Projeto orientado por rotina de deep work e entregas semanais
- Métricas de acompanhamento: 1 entrega/semana, ≥3 commits/semana
- README, checklist, dicionário de dados e estudo de caso para portfólio
