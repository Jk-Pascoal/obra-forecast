import streamlit as st
import pandas as pd
import joblib

def main():
    st.title('Previsão de Custo e Prazo de Obras')
    st.write('Faça upload do seu arquivo BoM (CSV) para estimar o custo total da obra.')

    uploaded_file = st.file_uploader('Escolha o arquivo CSV', type='csv')
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write('Prévia dos dados:', df)
        # Ajuste os nomes das features conforme seu pipeline
        features = ['n_itens_bom', 'pct_criticos', 'complexidade', 'lead_time_medio']
        X = df[features]
        X = pd.get_dummies(X, columns=['complexidade'])
        model = joblib.load('src/model.joblib')
        preds = model.predict(X)
        df['custo_previsto'] = preds

        st.write('Resultados:', df[['custo_previsto']])

        # Gráfico de barras dos custos previstos
        st.subheader('Gráfico de Custos Previstos')
        st.bar_chart(df['custo_previsto'])

        # Gráfico de dispersão: lead_time_medio vs custo_previsto
        st.subheader('Lead Time Médio vs Custo Previsto')
        st.scatter_chart(df, x='lead_time_medio', y='custo_previsto')

        st.download_button('Baixar resultados', df.to_csv(index=False), file_name='previsao_obras.csv')

if __name__ == '__main__':
    main()
