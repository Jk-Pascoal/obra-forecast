# pipeline.py
"""
Pipeline de modelagem para previsão de custo e prazo de obras.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def fit(X, y, model_path='src/model.joblib'):
    """Treina e salva o modelo."""
    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)
    joblib.dump(model, model_path)
    return model

def predict(X, model_path='model.joblib'):
    """Carrega o modelo e faz previsões."""
    model = joblib.load(model_path)
    return model.predict(X)

if __name__ == "__main__":
    # Exemplo de uso
    df = pd.read_csv('data/obras.csv')
    features = ['n_itens_bom', 'pct_criticos', 'complexidade', 'lead_time_medio']
    # Converter coluna categórica 'complexidade' em variáveis dummies
    X = df[features]
    X = pd.get_dummies(X, columns=['complexidade'])
    y = df['custo_total']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    fit(X_train, y_train, model_path='src/model.joblib')
    preds = predict(X_test, model_path='src/model.joblib')
    print('Previsões:', preds)
