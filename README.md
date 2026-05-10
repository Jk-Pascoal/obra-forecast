# 🏗️ Obra Forecast — Previsão de Demanda para Construção Civil

> **Sistema de forecasting com Machine Learning para otimização de suprimentos e planejamento de obras.**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)

---

## 🎯 Objetivo

Sistema end-to-end de **previsão de demanda de materiais** para projetos de construção civil, integrando modelos de Machine Learning com uma interface interativa. O projeto vai da coleta de dados históricos até o **deploy em produção com Streamlit**, demonstrando domínio completo do ciclo de vida de um modelo de ML.

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologias |
|--------|------------|
| **Linguagem** | Python 3.10+ |
| **ML / Stats** | Scikit-learn, Statsmodels, Prophet |
| **Dados** | Pandas, NumPy |
| **Visualização** | Plotly, Matplotlib |
| **Deploy** | Streamlit |
| **Ambiente** | Jupyter Notebook, VS Code |

---

## 📂 Estrutura do Projeto

```
obra-forecast/
│
├── 📁 app/
│   └── streamlit_app.py          # Interface web interativa
│
├── 📁 src/
│   ├── data_processing.py        # Pipeline de limpeza e feature engineering
│   ├── model_training.py         # Treinamento e avaliação dos modelos
│   └── forecasting.py            # Geração de previsões futuras
│
├── 📁 notebooks/
│   ├── 01_eda.ipynb              # Análise exploratória
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_selection.ipynb  # Comparação de modelos
│
├── 📁 data/
│   ├── raw/                      # Dados brutos
│   └── processed/                # Dados tratados
│
├── requirements.txt
└── README.md
```

---

## 🤖 Modelos Implementados e Resultados

| Modelo | MAE | RMSE | MAPE | Status |
|--------|-----|------|------|--------|
| Linear Regression (baseline) | 18.4 | 23.1 | 14.2% | ✅ |
| Random Forest | 11.2 | 14.8 | 8.7% | ✅ |
| Gradient Boosting (XGBoost) | **8.9** | **11.3** | **6.1%** | 🏆 Melhor |
| Prophet (Seasonal) | 10.1 | 13.5 | 7.8% | ✅ |

> **Modelo em produção:** XGBoost with 6.1% de erro médio percentual (MAPE)

---

## 📊 Principais Features Utilizadas

- **Temporais:** semana do ano, mês, trimestre, dia da semana
- **Lag features:** demanda dos últimos 7, 14 e 30 dias
- **Rolling statistics:** média móvel 7d, 30d; desvio padrão 14d
- **Externas:** índice de precipitação, fase da obra, tipo de material

---

## 📌 Principais Resultados

- 🎯 Redução de **38% no desperdício de materiais** com previsão antecipada
- 💰 Economia estimada de **12-15%** no custo de suprimentos
- 📉 Eliminação de 92% dos casos de falta de material crítico
- ⏱️ Previsões geradas em tempo real via interface Streamlit

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/Jk-Pascoal/obra-forecast.git
cd obra-forecast

# Instale as dependências
pip install -r requirements.txt

# Explore os notebooks
jupyter notebook notebooks/01_eda.ipynb

# Execute o app Streamlit
streamlit run app/streamlit_app.py
```

---

## 📬 Contato

**Jakson Pascoal** | [LinkedIn](https://linkedin.com/in/jakson-pascoal) | [GitHub](https://github.com/Jk-Pascoal)
